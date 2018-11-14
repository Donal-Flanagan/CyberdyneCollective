%load_ext autoreload
%autoreload 2
from utils import set_project_dir
project_dir = set_project_dir('project_3')

# import numpy as np
# import pandas as pd
# import scipy as sp
# from sklearn import preprocessing, feature_extraction, feature_selection, model_selection, metrics
# import xgboost as xgb
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# train = pd.read_csv('data/in/train.csv')
# test = pd.read_csv('data/in/test.csv')


import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

train = pd.read_csv('data/in/train.csv')
# test = pd.read_csv('data/in/test.csv')

X = np.asarray(train[['Pclass']])
y = np.asarray(train['Survived'])

clf = MultinomialNB()
clf.fit(X, y)
clf.predict_proba(X)
