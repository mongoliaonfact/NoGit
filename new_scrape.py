from bs4 import BeautifulSoup
import requests
from pandas import DataFrame


url = 'https://seekingalpha.com/article/4560263-golub-capital-bdc-gbdc-q4-2022-earnings-call-transcript'
#url = 'https://seekingalpha.com/article/4560276-aft-pharmaceuticals-limited-aftpf-q2-2023-earnings-call-transcript'
#url = 'https://seekingalpha.com/article/4560281-naspers-ltd-and-prosus-nv-prosy-q2-2022-earnings-call-transcript' 
def single_transcript(url, filename):
    text_content = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    with open(f'{filename}.txt', 'wt', encoding='utf-8') as newfile:
        for line in text:
            newfile.write(line)
    return text_content

a_script = single_transcript(url, '2')
#print(a_script)

def get_transcript_info(a_script):
    '''
    returns:
    --------
    company info:   info on what when the company transcript took place
    from_company:   participants from the company leadership
    others:         journalists, or participants or stakeholders of the company
    transcript:     discussion transcript that was conducted during the conference
    
    example: 
    -------
    script_info = get_transcript_info(a_script)
    company info = script_info[0]['company_info]
    '''
    info = []
    company_index = a_script.index('Company Participants')
    participants_index = a_script.index('Conference Call Participants')
    operator_index = a_script.index('Operator')
    script_info = a_script[:company_index]
    cparticipant = a_script[company_index+1 : participants_index]
    others = a_script[participants_index+1: operator_index]
    info.append({
        'company_info': script_info,
        'from_company': cparticipant,
        'others': others,
        'transcript': a_script[operator_index: ]
    })
    
    return info

script_info = get_transcript_info(a_script)
print(script_info)
#print(script_info[0]['company_info'])