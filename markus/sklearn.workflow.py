# workflow
from IPython.core.display import HTML
HTML("<style>.container { width:100% !important; }</style>")

import numpy as np
import pandas as pd
import sklearn as sci
import matplotlib as plt

# decision tree graphs
# $ sudo apt-get install graphviz
# $ conda install pydotplus
import pydotplus 
from IPython.display import Image 


# importing

def import_data(filename):
    features = pd.read_csv(filename, delimiter='\t', thousands=',', na_values=['n/a'], encoding='utf-8')
    # features = pd.DataFrame(np.random.randn(7,4), index=list('abcdefg'), columns=list('ABCD'))
    # print features and targets
    print('features =',iris.feature_names)
    print('targets =',iris.target_names)
    
    
def 
    # labels = index('apples', 'oranges')
    # labels = ['apples', 'oranges']

    # features.index