
# @author: bbaasan
# date: 9/5/2022
# bbaasan@gmu.edu

import requests
import warnings

warnings.filterwarnings('ignore')


def get_transcript(ticker, year, quarter):
        key = '22579006dc377a880ec7abbba96fbdd2'
        transcript = requests.get(f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{ticker}?quarter={quarter}&year={year}&apikey={key}').json()
        if len(transcript) > 0:
            
            trans = transcript[0]['content']
            date = transcript[0]['date']
            date_ = str(date).split(' ')[0]
            return date_, trans
        else:
            return 'transcript is empty.'
'''
def main():
    
    ticker = 'AAPL'
    year = 2020
    quarter = 2
    key = '22579006dc377a880ec7abbba96fbdd2'
    print(get_transcript(ticker=ticker, year=year, quarter=quarter))
    #print(requests.get(f'https://financialmodelingprep.com/api/v3/earning_call_transcript/{ticker}?quarter={quarter}&year={year}&apikey={key}').json())
    
if __name__ == '__main__':
    main()
    '''