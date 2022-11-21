from pathlib import Path
from os import getcwd, mkdir
from os.path import exists
from shutil import rmtree
#import nltk
# nltk.download()
from nltk.tokenize import sent_tokenize

# local module 
from transcript import get_transcript

TK_SILENCE_DEPRECATION=1

def substring_before_after(text, delim, get=True):
    if get == True:
        return text.partition(delim)[0]
    else:
        return text.partition(delim)[1]

def get_transcripts(ticker_lists=None, year_lists=None, quarter_lists=None): 
    print('Your request for transcript is being done soon. Thank you for waiting.')
    '''
    params:
    ticker_lists:
    year_lists:
    quarter_lists:
    
    '''
    dataset = 'dataset'
    
    try:
        mkdir(f'{dataset}')
    except:
        if exists(dataset):
            rmtree(dataset)
            mkdir(dataset)
            
    
    report = []
    
    for ticker in ticker_lists:
        try:
            #print('\n Creating a directory...')
            mkdir(f'dataset/{ticker}')
            #file = open(f'dataset/{ticker}/{ticker}.txt', 'w')
            #pass
        except FileExistsError:
            #rmdir(f'{ticker}')
            print(f'-- Folder {ticker} exists and we will use that folder.')
            pass
            
        #print('writing the text file ...')
        for year in year_lists:
            try:
                mkdir(f'dataset/{ticker}/{year}')
                
            except FileExistsError:
                #rmdir(f'{ticker}/{quarter}')
                print(f'-- {ticker}, year {year} also exists and will use that folder.')
                pass
            
            for quarter in quarter_lists:
                try:
                    mkdir(f'dataset/{ticker}/{year}/{quarter}')
                except FileExistsError:
                    #rmdir(f'{ticker}/{quarter}')
                    print(f'-- {ticker}, {year}, quarter {quarter} also exists and will use that folder.')
                    
                try:
                    date, transcript = get_transcript(ticker, year, quarter)
                    for i, a_paragraph in enumerate(transcript.split('\n')):
                        try:
                            sentence = sent_tokenize(a_paragraph)
                            person_name = substring_before_after(sentence[0], ':', get=True)
                            
                            filename = open(f'dataset/{ticker}/{year}/{quarter}/{person_name}_{i}.txt', 'w+')
                            filename.write(a_paragraph)
                            filename.close()
                        
                            '''
                            try:
                            pass
                            #first_twenty_char = a_paragraph[0:20]
                            #person_name = substring_before_after(first_twenty_char, ':', get=True)
                            #rest = substring_before_after()
                            
                            if ':' in first_twenty_char:
                                person_name, rest = first_twenty_char.split(':')
                                
                                #a_paragraph = a_paragraph.replace(person_name, '')
                                filename = open(f'dataset/{ticker}/{year}/{quarter}/{person_name}_{i}.txt', 'w+')
                                filename.write(a_paragraph)
                                filename.close()'''
                                
                        except ValueError:
                            print(f'{ticker}, {year}, {quarter}, {i}')
                            print('-------------------------')
                            
                except ValueError as e:
                    #raise
                    pass
    print(f'Your request is now Done and can be found in the following folder. Thank you \n {getcwd()}')


#def main():
    
    #test_firms = ['AAPL', 'AMZN'] #, 'AMZN']
    #test_years = [f for f in range(2008, 2022, 1)]
    #test_quarters = [1, 2, 3, 4] 
    #df = get_transcripts(ticker_lists=test_firms, year_lists=test_years, quarter_lists=test_quarters)
    #print('hello')
    
    
    
#if __name__ == '__main__':  main()