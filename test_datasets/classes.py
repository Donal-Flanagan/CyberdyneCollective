import os
import dotenv
import psycopg2 as ps

import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing, feature_extraction, feature_selection, model_selection, metrics
import xgboost as xgb
from imblearn.combine import SMOTETomek

import matplotlib.pyplot as plt

import utils


class ML(object):
    def __init__(self, df=None, x_columns=None, y_column=None, convert_dict=None, keep_dict=None,
                 drop_dict=None, replace_dict=None, feature_dict=None,
                 method=None, vectorizer=None, model_params={}, *args, **kwargs):
        super(ML, self).__init__()
        if df is not None:
            self.df = df.copy()
            self.n_columns = len(self.df.columns) - 2

        self.x_columns = x_columns
        self.y_column = y_column
        self.convert_dict = convert_dict
        self.keep_dict = keep_dict
        self.drop_dict = drop_dict
        self.replace_dict = replace_dict
        self.feature_dict = feature_dict
        self.method = method
        self.model_params = model_params
        self.sample_weight = None
        self.eval_metric = None
        self.vectorizer = vectorizer

    def filter(self, filter_str=None):
        if filter_str is not None:
            self.filter_str = filter_str

        self.df.query(self.filter_str, inplace=True)
        return self.df

    def keep(self, keep_dict=None):
        if keep_dict is not None:
            self.keep_dict = keep_dict

        for column, lst in self.keep_dict.items():
            self.df = self.df[self.df[column].isin(lst)]
        return self.df

    def drop(self, drop_dict=None):
        if drop_dict is not None:
            self.drop_dict = drop_dict

        for column, lst in self.drop_dict.items():
            self.df = self.df[~self.df[column].isin(lst)]
            # for item in lst:
            #     self.df = self.df[self.df[column] != item]
        return self.df

    def replace(self, replace_dict=None):
        if replace_dict is not None:
            self.replace_dict = replace_dict

        for column, replace_item in self.replace_dict.items():
            for value, replace in replace_item.items():
                if callable(replace):
                    replace_val = replace(self.df[column])
                else:
                    replace_val = replace

                if value is np.nan:
                    self.df[column].fillna(replace_val, inplace=True)
                elif callable(value):
                    self.df.loc[value(self.df[column]), column] = replace_val
                else:
                    self.df.loc[self.df[column] == value, column] = replace_val
        return self.df

    def convert(self, convert_dict=None):
        if convert_dict is not None:
            self.convert_dict = convert_dict

        if self.convert_dict is not None:
            for column, func in self.convert_dict.items():
                self.df[column] = func(self.df[column])
        return self.df

    def feature(self, feature_dict=None):
        if feature_dict is not None:
            self.feature_dict = feature_dict

        for column, func in self.feature_dict.items():
            self.df[column] = func(self.df)
        return self.df

    def split_test(self, n_splits=6):
        # not general!!!
        time_split = model_selection.TimeSeriesSplit(n_splits=n_splits)
        # get last element of iterator:
        train_idx, test_idx = list(time_split.split(self.df))[-1]
        self.df_test = self.df.iloc[test_idx]
        self.df_train = self.df.iloc[train_idx]

    def create_mapping(self):
        self.mapping = {}
        columns = self.df[self.x_columns].select_dtypes(include=['object'])
        for column in columns:
            self.mapping[column] = list(self.df[column].unique())
        return self.mapping

    def compare_mapping(self, ext_mapping):
        """
        checks if categorical features of self correspond to features in ext_mapping.
        returns 1 if error found
        """
        columns = self.df[self.x_columns].select_dtypes(include=['object'])
        for column in columns:
            if column in ext_mapping:
                if not set(self.mapping[column]).issubset(set(ext_mapping[column])):
                    # feature entry is new, raise warning
                    return 1
            else:
                # raise warning that we have a rogue feature.
                # can only happen when training data not update after features were added
                return 1
        return 0

    def get_X(self, vectorizer=None, sparse=True):
        if vectorizer is not None:
            self.vectorizer = vectorizer

        if not self.vectorizer:
            self.vectorizer = feature_extraction.DictVectorizer(sparse=sparse)
            self.X = self.vectorizer.fit_transform(self.df[self.x_columns].to_dict(orient='records'))
        else:
            self.X = self.vectorizer.transform(self.df[self.x_columns].to_dict(orient='records'))

        self.feature_columns = self.vectorizer.vocabulary_
        return self.X

    def get_y(self):
        self.y = np.array(self.df[self.y_column])
        return self.y

    def create_model(self, method=None, model_params=None):
        if method is not None:
            self.method = method

        if model_params is not None:
            self.model_params = model_params

        if self.method == 'classification':
            if model_params:
                self.model = xgb.XGBClassifier(**self.model_params)
            else:
                self.model = xgb.XGBClassifier()
            return True
        elif self.method == 'regression':
            print('Not implemented yet')
        return self.model

    def resample(self):
        self.sampler = SMOTETomek(n_jobs=-1)
        self.X, self.y = self.sampler.fit_sample(self.X, self.y)

    def cross_val(self, scoring=None, cv=4, weight=None, eval_metric=None):
        if scoring is not None:
            self.metric = scoring

        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])
        else:
            self.sample_weight = None

        if eval_metric is not None:
            self.eval_metric = eval_metric
        else:
            self.eval_metric = 'error'

        self.cross_vals = model_selection.cross_val_score(self.model, self.X, self.y, scoring=self.metric, cv=cv,
                                                          fit_params={'sample_weight': self.sample_weight,
                                                                      'eval_metric': self.eval_metric}, n_jobs=-1)
        return self.cross_vals

    def grid_search(self, param_grid, scoring=None, cv=4, weight=None, eval_metric=None):
        if scoring is not None:
            self.metric = scoring

        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])
        else:
            self.sample_weight = None

        if eval_metric is not None:
            self.eval_metric = eval_metric
        else:
            self.eval_metric = 'error'

        grid_search_clf = model_selection.GridSearchCV(self.model, param_grid=param_grid, scoring=scoring, cv=cv,
                                       fit_params={'sample_weight': self.sample_weight, 'eval_metric': self.eval_metric},
                                       n_jobs=-1)

    def train(self, weight=None, eval_metric=None):
        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])
        else:
            self.sample_weight = None

        if eval_metric is not None:
            self.eval_metric = eval_metric
        else:
            self.eval_metric = 'error'

        self.model.fit(self.X, self.y, sample_weight=self.sample_weight, eval_metric=self.eval_metric)
        self.feature_importances = pd.DataFrame([self.feature_columns.keys(), self.model.feature_importances_],
                                           index=['feature', 'importance']).T.sort_values(by='importance',
                                                                                          ascending=False)
        return self.feature_importances

    def score(self):
        self.y_prob = self.model.predict_proba(self.X)
        self.y_pred = self.model.predict(self.X)

    def describe(self):
        from IPython.display import display

        if self.df:
            self.df.describe()

        if self.model:
            print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))