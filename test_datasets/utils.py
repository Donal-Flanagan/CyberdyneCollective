
import numpy as np
import pandas as pd



x_columns = []
y_column = ''

drop_dict = {}
replace_dict = {}
opps_convert_dict = {'created': pd.to_datetime,
                     'planned_installation_time': pd.to_numeric,
                     'status_type': pd.to_numeric}

def get_end_of_month(df):
    return df['created'].dt.is_month_end


feature_dict = {'month_end': get_end_of_month}


