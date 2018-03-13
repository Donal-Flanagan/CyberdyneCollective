import os
import dotenv
import psycopg2 as ps

import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing, feature_extraction, feature_selection, model_selection, metrics
import scikitplot.plotters as skplt
import xgboost as xgb
from imblearn.combine import SMOTETomek

import matplotlib.pyplot as plt
import seaborn as sns

import utils


class ML(object):
    def __init__(self, df, x_columns=None, y_column=None, convert_dict=None, keep_dict=None,
                 drop_dict=None, replace_dict=None, feature_dict=None,
                 method=None, vectorizer=None, model_params={}, *args, **kwargs):
        super(ML, self).__init__()
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
        self.eval_metric = 'error'
        self.eval_set = None
        self.vectorizer = vectorizer
        self.y_prob = None

    ### preprocessing

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

    def split_train_test(self, n_splits=6):
        # not general!!!
        time_split = model_selection.TimeSeriesSplit(n_splits=n_splits)
        # get last element of iterator:
        train_idx, test_idx = list(time_split.split(self.df))[-1]
        self.df_train = self.df.iloc[train_idx]
        self.df_test = self.df.iloc[test_idx]

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

    def get_X(self, vectorizer=None, sparse=True, train_test=True):
        # refactor with get_y
        if vectorizer is not None:
            self.vectorizer = vectorizer

        if train_test:
            df_train_dict = self.df_train[self.x_columns].to_dict(orient='records')
            df_test_dict = self.df_test[self.x_columns].to_dict(orient='records')
        else:
            df_dict = self.df[self.x_columns].to_dict(orient='records')

        if not self.vectorizer:
            self.vectorizer = feature_extraction.DictVectorizer(sparse=sparse)
            if train_test:
                self.vectorizer.fit(df_train_dict)
            else:
                self.vectorizer.fit(df_dict)
            self.feature_columns = self.vectorizer.vocabulary_

        if train_test:
            self.X_train = self.vectorizer.transform(df_train_dict)
            self.X_test = self.vectorizer.transform(df_test_dict)
            return self.X_train, self.X_test
        else:
            self.X = self.vectorizer.transform(df_dict)
            return self.X

    def get_y(self, train_test=True):
        # add categorical enconding
        self.n_classes = self.df[self.y_column].nunique()

        if train_test:
            self.y_train = np.array(self.df_train[self.y_column])
            self.y_test = np.array(self.df_test[self.y_column])
            return self.y_train, self.y_test
        else:
            self.y = np.array(self.df[self.y_column])
            return self.y

    def create_eval_set(self):
        # refactor into get_X,y
        self.eval_set = [(self.X_train, self.y_train), (self.X_test, self.y_test)]

    ### machine learning

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
        self.X_train, self.y_train = self.sampler.fit_sample(self.X_train, self.y_train)

    def cross_val(self, metric=None, cv=4, weight=None, eval_metric=None, eval_set=None, group=None):
        if metric is not None:
            self.metric = metric

        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])

        if eval_metric is not None:
            self.eval_metric = eval_metric

        if eval_set is not None:
            self.eval_set = eval_set

        if group is not None:
            groups = self.df[group]
        else:
            groups = None

        self.cross_vals = model_selection.cross_val_score(self.model, self.X_train, self.y_train, scoring=self.metric,
                                                          cv=cv, groups=groups, n_jobs=-1,
                                                          fit_params={'sample_weight': self.sample_weight,
                                                                      'eval_metric': self.eval_metric,
                                                                      'eval_set': self.eval_set,
                                                                      'verbose': False})
        return self.cross_vals

    def grid_search(self, params, metric=None, cv=4, weight=None, eval_metric=None, eval_set=None):
        # refactor with random_search
        if metric is not None:
            self.metric = metric

        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])

        if eval_metric is not None:
            self.eval_metric = eval_metric

        if eval_set is not None:
            self.eval_set = eval_set

        self.model_grid_search = model_selection.GridSearchCV(self.model, param_grid=params, scoring=self.metric, cv=cv,
                                       fit_params={'sample_weight': self.sample_weight,
                                                   'eval_metric': self.eval_metric,
                                                   'eval_set': self.eval_set,
                                                   'verbose': False},
                                       n_jobs=-1)

    def random_search(self, params, n_iter, metric=None, cv=4, weight=None, eval_metric=None, eval_set=None):
        # add eval_sets
        if metric is not None:
            self.metric = metric

        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])

        if eval_metric is not None:
            self.eval_metric = eval_metric

        if eval_set is not None:
            self.eval_set = eval_set

        self.model_random_search = model_selection.RandomizedSearchCV(self.model, param_distributions=params, n_iter=n_iter, scoring=self.metric,
                                           fit_params={'sample_weight': self.sample_weight,
                                                       'eval_metric': self.eval_metric,
                                                       'eval_set': self.eval_set,
                                                       'verbose': False},
                                           n_jobs=-1, cv=cv, error_score=-1)

    def train(self, weight=None, eval_metric=None, eval_set=None, stop_after=None):
        if weight is not None:
            self.weight = weight
            self.sample_weight = np.array(self.df[weight])

        if eval_metric is not None:
            self.eval_metric = eval_metric

        if eval_set is not None:
            self.eval_set = eval_set

        self.model.fit(self.X_train, self.y_train, sample_weight=self.sample_weight, eval_metric=self.eval_metric,
                       eval_set=self.eval_set, early_stopping_rounds=stop_after, verbose=False)

        self.feature_importances = pd.DataFrame({'feature': list(self.feature_columns.keys()),
                                                 'importance': self.model.feature_importances_}).sort_values(by='importance', ascending=False)

        return self.feature_importances

    def score(self):
        self.y_prob = self.model.predict_proba(self.X_test)
        self.y_pred = self.model.predict(self.X_test)

    ### plotting

    def plot_learning_curve(self, columns=['train', 'test']):
        try:
            errors_dict = self.model.evals_result()
            errors = pd.concat([pd.DataFrame(errors_dict['validation_' + str(i)]) for i in range(len(errors_dict))],
                               axis=1, keys=columns)
            errors.plot()
        except AttributeError:
            # takes too long
            skplt.plot_learning_curve(self.model, self.X_train, self.y_train, n_jobs=-1)
        plt.show()

    def plot_feature_importances(self):
        # feature names not working
        # skplt.plot_feature_importances(self.model, feature_names=None, max_num_features=20)
        xgb.plot_importance(self.model, importance_type='weight')
        xgb.plot_importance(self.model, importance_type='cover')
        xgb.plot_importance(self.model, importance_type='gain')
        plt.show()

    def plot_confusion_matrix(self, normalize=True):
        # add thresholding
        skplt.plot_confusion_matrix(self.y_test, self.y_pred, normalize=normalize)
        plt.show()

    def plot_roc_auc(self):
        # only for binary classification
        if self.n_classes <= 2:
            skplt.plot_roc_curve(self.y_test, self.y_prob)
            plt.show()
            # maybe implement weighted roc curve, auc score:
            # print(metrics.roc_auc_score(self.y_test, self.y_pred, average='macro', sample_weight=None))

    def plot_precision_recall(self):
        skplt.plot_precision_recall_curve(self.y_test, self.y_prob)
        plt.show()

    def plot_ks_statistic(self):
        # not working
        skplt.plot_ks_statistic(self.y_test, self.y_prob)
        plt.show()

    def describe(self):
        from IPython.display import display

        if self.df is not None:
            display(self.df.describe())

        # if self.model is not None:
        #     print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

        if self.cross_vals is not None:
            print(self.cross_vals)

        if self.y_prob is not None:
            if self.method == 'classification':
                self.plot_confusion_matrix()
                self.plot_roc_auc()
                self.plot_precision_recall()
                # self.plot_ks_statistic()
                self.plot_feature_importances()

        if self.eval_set is not None:
            self.plot_learning_curve()

