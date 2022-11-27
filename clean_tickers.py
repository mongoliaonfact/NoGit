from pandas import read_csv, DataFrame, set_option
from re import findall, sub
import string
from collections import Counter

def in_the_bracket(x):
    '''
    returns string characters of those wrapped in the parentheses in a sentence.
    In most cases, that will be company ticker or symbol
    Other cases, not useful information which handfully removed
    '''
    urt = len(findall(r'\(.*?\)', x))
    if urt >= 2:
        if '(publ)' in x:
            return findall(r'\(.*?\)', x)[1]
        else:
            return findall(r'\(.*?\)', x)[0]
    else:
        return findall(r'\(.*?\)', x)

# optional for checking
def getall(x):
    return findall(r'\(.*?\)', x)

def remove_parenthesis(x):
    '''
    returns string without parentheses, optional
    '''
    return type(x)
    if isinstance(x, list) == True:
        return x[1:-1]
        #return sub(r'[()]', '', x[0])
    else:
        return type(x)
        return sub(r'[()]', '', x)
        
def remove_bracket(x):
    '''
    returns string without parentheses, optional
    '''
    if isinstance(x, str)== True:
        return 'yes' #sub(r'[[]]', '', x)
    else:
        return x#sub(r'[[]]', '', x)

def rm_bracket(x):
    return x[1:-1]


def main():
    
    df = read_csv('/Volumes/Metallica/company_links.csv.zip', compression='zip')
    '''
    #df.columns = ['names', 'url', 'ticker']
    #df = df.loc[1:, :]
    #df3 = df[:100]
    #df3['ticker2'] = df3.loc[:, 'names'].apply(lambda x: in_the_bracket(x))
    #df3['type'] = df3.loc[:, 'ticker2'].apply(lambda x: type(x))
    #df3['ticker3'] = df3.loc[:, 'ticker2'].apply(lambda x: remove_parenthesis(x))
    #df['ticker2'] = df.loc[:, 'names'].apply(lambda x: in_the_bracket(x))
    #df.to_csv('/Volumes/Metallica/company_links.csv.zip', index=False, compression='zip')
    '''
    df['ticker2'] = df.loc[:, 'names'].apply(lambda x: in_the_bracket(x))
    #df['type'] = df.loc[:, 'ticker2'].apply(lambda x: type(x))
    df['ticker3'] = df.loc[:, 'ticker2'].apply(lambda x: remove_parenthesis(x))
    print(df)
    #print(df.loc[:, 'ticker3'].apply(lambda x: remove_bracket(x)))
    #print(Counter(df['type'].to_list()))
    
if __name__ == '__main__': main()
