import numpy as np
import pandas as pd
import json
import joblib


num_features = 21 #len(training_data.columns)-4
x_columns = ['feature'+str(i) for i in range(1,num_features)] + ['era_int']
y_column = 'target'

drop_dict = {}
replace_dict = {}
convert_dict = {'created': pd.to_datetime,
                     'planned_installation_time': pd.to_numeric,
                     'status_type': pd.to_numeric}

def get_end_of_month(df):
    return df['created'].dt.is_month_end

def get_era(df):
    return df['era'].apply(lambda s: int(s[3:]))

feature_dict = {'era_int': get_era}



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