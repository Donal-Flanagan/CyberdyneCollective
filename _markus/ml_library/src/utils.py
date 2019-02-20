import numpy as np
import pandas as pd
import json
import joblib


num_features = 21 #len(training_data.columns)-4
x_columns = ['feature'+str(i) for i in range(1,num_features+1)] #+ ['era_int']
y_column = 'target'

drop_dict = {}
replace_dict = {}

def get_era(df):
    return df['era'].apply(lambda s: int(s[3:]))

feature_dict = {'era_int': get_era}
convert_dict = {'target': lambda x: x.astype('category'),
                'era': lambda x: x.astype('category')}

model_params = {'base_score': 0.5,
                'colsample_bylevel': 1,
                'colsample_bytree': 1,
                'gamma': 0,
                'learning_rate': 0.1,
                'max_delta_step': 0,
                'max_depth': 2,
                'min_child_weight': 1,
                'missing': None,
                'n_estimators': 500,
                'nthread': -1,
                'objective': 'binary:logistic',
                'reg_alpha': 0,
                'reg_lambda': 1,
                'scale_pos_weight': 1,
                'seed': 0,
                'silent': True,
                'subsample': 0.5 #1
                }


def dump(obj, file):
    if file[file.rfind('.',):] == '.json':
        with open(file, 'w') as f:
            json.dump(obj, f, ensure_ascii=False)
    else:
        # with open(file, 'wb') as f:
        #     pickle.dump(obj, f)
        joblib.dump(obj, file)


def load(file):
    if file[file.rfind('.',):] == '.json':
        with open(file, 'r') as f:
            return json.load(f)
    else:
        # with open(file, 'rb') as f:
        #     return pickle.load(f)
        return joblib.load(file)