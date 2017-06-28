import numpy as np
import pandas as pd
from sklearn import preprocessing, feature_extraction, feature_selection, model_selection, metrics
import xgboost as xgb

import os
import dotenv
import psycopg2 as ps



class ML(object):
    def __init__(self df=None, x_columns=None, y_column=None, convert_dict=None,
                 drop_dict=None, replace_dict=None, feature_dict=None,
                 ga_metrics=None, ga_dims=None, *args, **kwargs):
        super(ML, self).__init__()
        self.df = df
        self.x_columns = x_columns
        self.y_column = y_column
        self.convert_dict = convert_dict
        self.drop_dict = drop_dict
        self.replace_dict = replace_dict
        self.feature_dict = feature_dict

    def convert(self):
        if self.convert_dict is not None:
            for column, func in self.convert_dict.items():
                self.df[column] = func(self.df[column])

    def feature(self):
        '''call feature building functions on columns'''
        for column, func in self.feature_dict.items():
            self.df[column] = func(self.df)

    def save_mapping(self):
        pass

    def load_mapping(self):
        pass

    def get_X(self, sparse=True):
        self.vectorizer_ = feature_extraction.DictVectorizer(sparse=sparse)
        self.X = self.vectorizer_.fit_transform(self.df[self.x_columns].to_dict(orient='records'))
        self.feature_columns_ = self.vectorizer_.vocabulary_

    def get_y(self):
        self.y = np.array(self.df[self.y_column])

    def create_model(self):
        if self.method == 'classification':
            self.model = xgboost.XGBClassifier(**self.model_params)
        elif self.method == 'regression':
            print('Not implemented yet')

    def train(self):
        pass

    def pickle(self):
        pass

    def unpickle(self):
        pass

    def score(self):
        pass

