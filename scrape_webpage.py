# @author: bbaasan
# date: 11/22/2022
# bbaasan@gmu.edu


from bs4 import BeautifulSoup
import requests
from pandas import DataFrame, read_csv

def single_transcript(url):
    text_content = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    for line in text:
        text_content.append(line)
    #with open(f'{filename}.txt', 'wt', encoding='utf-8') as newfile:
        #newfile.write(text[0])
    #    for line in text[0]:
    #        newfile.write(line+" \n")
            #newfile.write('\n')
    return text_content
    
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

def main():
    
    url = 'https://seekingalpha.com/article/4560263-golub-capital-bdc-gbdc-q4-2022-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4560276-aft-pharmaceuticals-limited-aftpf-q2-2023-earnings-call-transcript'
    #url = 'https://seekingalpha.com/article/4560281-naspers-ltd-and-prosus-nv-prosy-q2-2022-earnings-call-transcript' 
    
    #a_script = single_transcript(url)
    #company = get_transcript_info(a_script)
    #print(company[0]['company_info'][0])
    #print(company[0]['from_company'])
    #print(company[0]['others'])
    #print(company[0]['q_and_a'])
    
    
    #filename = open('first.txt', 'w', encoding='utf-8')
    #filename.write(company)
    #filename.close()
    #df = DataFrame(company)
    #df.to_csv('company.csv', index=False)
    
    print(read_csv('company.csv'))
    
if __name__ == '__main__':
    main()