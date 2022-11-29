# @author: bbaasan
# date: 11/22/2022
# bbaasan@gmu.edu


from bs4 import BeautifulSoup
import requests
from pandas import DataFrame, read_csv
from collections import Counter
from danielkennet import tech2
from datetime import datetime 


def single_transcript(url):
    text_content = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    for line in text:
        text_content.append(line)

def single_transcript_v2(url):
    
    breaks = ['Question-and-Answer', 'Questions-and-Answers', 'Question-and-Answer Session', 'Question-and-Answer Session ',
              'And with that, we would like to open up the call for Q&A. Operator?', 'Question-And-Answer Session ',
              'Question-And-Answer Session', 'Questions-and-Answers Session', 'Questions-and-Answer Session']
    text_content = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    company_script = []
    for i, line in enumerate(text):
        company_script.append(line)
        if line in breaks:
            ind = i
        #print(f'index: {i}, {[line]}')
    #print(f'break: {ind}')
    #print('-------------------------------------')  
    #print(company_script) 
    #print('=====================================')
    #print(company_script[: ind])
    
    text_content.append({
        'presentation': company_script[: ind],
        'q_and_a': company_script[ind +1: ] 
    })
    return text_content

def write_transcript(url, filename):    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    with open(f'{filename}.txt', 'wt', encoding='utf-8') as newfile:
        for line in text:
            newfile.writelines(line)
            #newfile.write('\n')


    
def get_transcript_info(a_script):
    '''
    returns:
    --------
    company info:       info on what when the company transcript took place
    from_company:       participants from the company leadership
    others:             journalists, or participants or stakeholders of the company
    transcript:         discussion transcript that was conducted during the conference
    ceo_presentation:   presentation that company managers presented
    q_and_a:            questions and answers exchanged between managers and others
    
    example: 
    -------
    script_info = get_transcript_info(a_script)
    company info = script_info[0]['company_info]
    '''
    #a_script = a_script[0]
    info = []
    company_index = a_script.index('Company Participants')
    participants_index = a_script.index('Conference Call Participants')
    operator_index = a_script.index('Operator')
    script_info = a_script[:company_index]
    cparticipant = a_script[company_index + 1 : participants_index]
    others = a_script[participants_index + 1: operator_index]
    ceo_index = a_script.index('Question-and-Answer Session')
    ceo_present = a_script[operator_index + 1: ceo_index]
    q_and_a = a_script[ceo_index + 1: ]
    info.append({
        'company_info': script_info,
        'from_company': cparticipant,
        'others': others,
        'transcript': a_script[operator_index: ],
        'ceo_presentation': ceo_present,
        'q_and_a': q_and_a
    })
    
    return info

def either(x):
    y = ''
    if x in tech2: y = 'yes'
    else: y = 'no'
    return y

def main():
    start = datetime.now()
    #url = 'https://seekingalpha.com/article/4560263-golub-capital-bdc-gbdc-q4-2022-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4560276-aft-pharmaceuticals-limited-aftpf-q2-2023-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4560281-naspers-ltd-and-prosus-nv-prosy-q2-2022-earnings-call-transcript' 
    #url = 'https://seekingalpha.com/article/4380147-duck-creek-technologies-inc-dct-ceo-mike-jackowski-on-q4-2020-results-earnings-call'
    #url = 'https://seekingalpha.com/article/4546251-duck-creek-technologies-inc-dct-q4-2022-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4367179-ceva-inc-ceva-ceo-gideon-wertheizer-on-q2-2020-results-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4362686-2u-inc-twou-ceo-chip-paucek-on-q2-2020-results-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4298925-sps-commerce-inc-spsc-ceo-archie-black-on-q3-2019-results-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4481454-commvault-systems-inc-cvlt-ceo-sanjay-mirchandani-on-q3-2022-results-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4261266-cornerstone-ondemand-inc-csod-ceo-adam-miller-on-q1-2019-results-earnings-call-transcript'
    '''
    breaks = ['Question-and-Answer', 'Questions-and-Answers', 'Question-and-Answer Session', 'Question-and-Answer Session ', 
              'And with that, we would like to open up the call for Q&A. Operator?', 'Question-And-Answer Session ', 
              'Question-And-Answer Session', 'Questions-and-Answers Session', 'Questions-and-Answer Session']
    text_content = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    company_script = []
    for i, line in enumerate(text):
        company_script.append(line)
        if line in breaks:
            ind = i
        print(f'index: {i}, {[line]}')
    print(f'break: {ind}')
    #print('-------------------------------------')  
    #print(company_script) 
    #print('=====================================')
    #print(company_script[: ind])
    
    #a_script = single_transcript_v2(url)
    #print(DataFrame(a_script))
    
    #print(tech2)
    '''
    df = read_csv('main_tbl.csv')
    print(df)
    df['prep'] = df['tick'].apply(lambda x: either(x))
    daniel = df[df['prep'] == 'yes'].loc[:, ['names', 'url', 'tick']]
    for ind, row in daniel.iterrows():
        name = row['names']
        tick = row['tick']
        url = row['url']
        #script = single_transcript_v2(url)
        try:
            script = single_transcript_v2(url)
            print(name, tick, script)
        except UnboundLocalError:
            print('--------------------------')
            print(f'this is error message {url}')
            return #'''
    end = datetime.now()
    
    print(f'Total time is: {end - start}')

    
if __name__ == '__main__':
    main()