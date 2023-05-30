from pandas import DataFrame
from requests import get
from bs4 import BeautifulSoup
from os import listdir, path
from PyPDF2 import PdfReader


class SCHOOL:

    def __init__(self) -> None:
        self.school = 'Schar'
        self.year_list = list()
        self.program_name_list = list()
        self.syllabus_list = list()
        self.semester_list = list()

    def to_add_info(self, year, program, syllabus, 
                    semester):
        self.year_list.append(year)
        self.program_name_list.append(program)
        self.syllabus_list.append(syllabus)
        self.semester_list.append(semester)
    
    def print_info(self):
        return DataFrame({
            'school': self.school,
            'year': self.year_list,
            'program': self.program_name_list,
            'syllabus': self.syllabus_list,
            'semester': self.semester_list  
        })
    
    def get_texts_from_pdf(self, pdf_file):
        
        extracted_texts = list()
        reader = PdfReader(pdf_file)
        
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text = page.extract_text()
            extracted_texts.append(text+' ')
        return(extracted_texts)
    
    def get_texts(self, file):
        extracted_texts = list()
        with open(file, 'r', encoding='utf-8') as text_file:
            reader = text_file.readlines()
            
            for line in reader:
                extracted_texts.append(str(line.replace('\u200b', '').replace('\n', '')))
        
        return(','.join(extracted_texts))
    
    def get_files(self, dirname):
        extracted_files = []
        for file in listdir(dirname):
            extracted_files.append(path.abspath(''.join((dirname,'/', file))))
        return extracted_files
    
    