import pandas as pd

class EconDataFrame(pd.DataFrame):
    
    def __init__(self, **kwargs):
        super(EconDataFrame, self).__init__(**kwargs)
        self._init_edf()
    
    def _init_edf(self):
        self.attr = 0
    
    @classmethod
    def from_df(cls, df):
        '''Transform DataFrame into EconDataFrame'''
        edf = df.copy()
        edf.__class__ = cls # is there a better way?
        edf._init_edf()
        return edf
    
    def to_df(self):
        df = self.copy()
        df.__class__ = pd.DataFrame
        return df

    def doSomething(self):
        localVariable = self.attr
        print(localVariable)


class Helper(object):
    
    def __init__(self):
        super(Helper, self).__init__()
        
        
def try_decode_str(st, st_format='utf-8'):
        try:
            return str(st).decode(st_format)
        except AttributeError:
            return str(st)
        
# def find_word(sentence, word, exact=True, lowercase=True, str_format='utf-8'):
#     sentence = try_decode_str(sentence)
#     word = try_decode_str(word)
    
#     if lowercase:
#         sentence = sentence.lower()
#         word = word.lower()
    
#     if exact:
#         pos = 1
#         for s in sentence.split():
#             if s == word:
#                 return pos
#             pos += len(s) + 1 # more or less
#         return -1
#     else:
#         return sentence.find(word)
    

def get_indicators(strings, sources='World Development Indicators', fields='all', exact=False, sep=None, verbose=False):
    '''
    * returns: 
        list of ids for the search string
        
    * prints:
        name strings for the returned fields
        
    * arguments:    
    strings=string: if exact=True: search for entire string
                    if exact=False: search for individual words
    
    strings=[array]: if exact=True: search for first entire string OR search for second entire string...
                     if exact=False: search for individual words in string OR search for individual words in second string...
    
    source:
    
    fields='all': searches in all fields
    
    field=[array]
        
    exact=True:
        search for exact string
    exact=False:
        search for words individually
    
    
    '''
    
    if isinstance(strings, str):
        strings = [strings]
    
    if isinstance(sources, str):
        if sources == 'all':
            data = wb.search('')
        else:
            data = wb.search(sources, field='source')
    else:
        data = pd.DataFrame()
        for source in sources:
            data = data.append(wb.search(source, field='source'))
    
    if isinstance(fields, str):
        if fields == 'all':
            fields = list(indicators.columns)
        else:
            fields = [fields]
    
    data_out = pd.DataFrame()
    if exact:
        for f in fields:
            for string in strings:
                rows = data[data[f].apply(lambda x: try_decode_str(x).lower().find(string.lower())) != -1]
                if len(rows) == 0:
                    print('Warning: Nothing found for {}'.format(string))
                else:
                    data_out = data_out.append(rows)
#                 data_out['input'] = string
        data_out.drop_duplicates(inplace=True)

    else:
        for string in strings:
            string_list = string.split(sep=sep)
            for f in fields:
                for s in string_list:
                    rows = data[data[f].apply(lambda x: try_decode_str(x).lower().find(s.lower())) != -1]
                    if len(rows) == 0:
                        print('Warning: Nothing found for {}'.format(string))
                    else:
                        data_out = data_out.append(rows)
#                     data_out['input'] = s
        data_out.drop_duplicates(inplace=True)
        
    if verbose:
        display(data_out)
        
    return data_out[['id', 'name']]


def get_countries(strings, country_data=None, fields='name', exact=True, sep=None, verbose=False):

    if country_data is None:
        data = wb.get_countries()
    else:
        data = country_data

    
    if isinstance(strings, str):
        strings = [strings]
    
    if isinstance(fields, str):
        if fields == 'all':
            fields = list(data.columns)
        else:
            fields = [fields]
    
    data_out = pd.DataFrame()
    if exact:
        for f in fields:
            for string in strings:
                rows = data[data[f].apply(lambda x: try_decode_str(x).lower().find(string.lower())) != -1]
                if len(rows) == 0:
                    print('Warning: Nothing found for {}'.format(string))
                else:
                    data_out = data_out.append(rows)
        data_out.drop_duplicates(inplace=True)

    else:
        for string in strings:
            string_list = string.split(sep=sep)
            for f in fields:
                for s in string_list:
                    rows = data[data[f].apply(lambda x: try_decode_str(x).lower().find(s.lower())) != -1]
                    if len(rows) == 0:
                        print('Warning: Nothing found for {}'.format(string))
                    else:
                        data_out = data_out.append(rows)
        data_out.drop_duplicates(inplace=True)
    
    if verbose:
        display(data_out)
        
    return list(data_out['iso3c'])


def import_edf(indicators, countries='all', trange=[2000,2000], country_data=None, dropna=True, **kwargs):
    
    if isinstance(indicators, list):
        indicators = pd.DataFrame([indicators,indicators], columns=['id','name'])
        print(indicators)
                
    if isinstance(countries, str):
        countries = [countries]
        
    if len([True for country in countries if len(country) > 3]) > 0:
        if country_data is None:
            country_data = wb.get_countries()
        countries = get_countries(countries, country_data=country_data)
            
    if isinstance(trange,int):
        trange = [trange, trange]
        
    df = wb.download(country=countries,indicator=indicators['id'], start=trange[0], end=trange[1])
    df.columns = indicators['name']
    
    if dropna:
        return df.dropna()
    else:
        return df