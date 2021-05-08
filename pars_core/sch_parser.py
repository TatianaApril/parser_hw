#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import pandas as pd

class Parser:
    def __init__(self, path, keywords, result = None):
        self.path = path
        self.keywords = keywords
        self.result = pd.DataFrame(columns=['Date', 'Decoder', 'Section number', 'Participants', 'Foreign participants',
                 'Min team number', 'Max team number', 'Registration', 'Exam', 'Leader', 'Lead assistent', 
                 'JR Lead assistent', 'Flag', 'Uniform', 'Shoes', 'Min exam result'])
        
    def data_reader(self):
        with open(self.path, "r", encoding="UTF-8") as data:
        #input_data = open(self.path)
        #data = list(input_data) 
            data = data.read()
        return data
    
    def data_cleaner(self, data):
        #delete comments and multienter
        data = re.sub(r'--.*',' ', data)
        data = re.sub(r'\n{1,}', '\n', data)
        data = re.sub(r'\t', ' ', data)
        return data
    
    def mystery_default_func(self, data):
        data = re.sub(r"1\*",'DEFAULT',data)
        data= re.sub(r"2\*",'DEFAULT DEFAULT',data)
        data = re.sub(r"3\*",'DEFAULT DEFAULT DEFAULT',data)
        return data
    
    def data_spliter(self, data):
        blocks = re.split(r'\n', data)  
        return blocks
    
    def parse_keyword_COMPDAT_line(self, data):
        #for i in range(len(data)):
            #data = re.sub(r'COMPDAT', '', data[i])
        data = re.sub('/', '', str(data))
        data = re.sub("'", '', str(data))
        data = re.split('\s+', data)
        return data
    
    def parse_keyword_COMPDATL_line(self, data):
        #for i in range(len(data)):
            #data = re.sub(r'COMPDATL', '', data[i])
        data = re.sub('/', '', str(data))
        data = re.sub("'", '', str(data))
        data = re.split('\s+', data)
        return data
    
    def parse_keyword_DATE_line(self, data):
        data = re.sub('/', '', str(data))
        data = re.sub("'", '', str(data))
        #data = re.split('\s+', data)
        return data
    
    
    def final_parsing(self, data):
        for i in range(len(data)):
            if re.search(r"COMPDAT\b", str(data[i - 1])):
                for k in range(i, len(data)):
                    data[k] = str(self.parse_keyword_COMPDAT_line(data[k]))
                    if re.search(r"W[0-9]|\d", str(data[k])):
                        a = re.findall(r'\w+', str(data[k]))
                        self.result = self.result.append({'Date': '',
                                        'Decoder': '',
                                        'Section number': a[0],
                                        'Participants': a[1],
                                        'Foreign participants': a[2],
                                        'Min team number': a[3],
                                        'Max team number': a[4],
                                        'Registration': a[5],
                                        'Exam': a[6],
                                        'Leader': a[7],
                                        'Lead assistent': a[8],
                                        'JR Lead assistent': a[9],
                                        'Flag': a[10],
                                        'Uniform': a[11],
                                        'Shoes': a[12],
                                        'Min exam result': a[13] + '.' + a[14]
                                        }, ignore_index=True)
                    if re.search(r"COMPDATL\b|DATES\b|WEFAC\b", str(data[k])): break
            
            elif re.search(r"COMPDATL\b", str(data[i - 1])):
                for k in range(i, len(data)):
                    data[k] = str(self.parse_keyword_COMPDATL_line(data[k]))
                    if re.search(r"W[0-9]|\d", data[k]):
                        a = re.findall(r'\w+', data[k])
                        self.result = self.result.append({'Date': '',
                                        'Decoder': a[1],
                                        'Section number': a[0],
                                        'Participants': a[2],
                                        'Foreign participants': a[3],
                                        'Min team number': a[4],
                                        'Max team number': a[5],
                                        'Registration': a[6],
                                        'Exam': a[7],
                                        'Leader': a[8],
                                        'Lead assistent': a[9],
                                        'JR Lead assistent': a[10],
                                        'Flag': a[11],
                                        'Uniform': a[12],
                                        'Shoes': a[13],
                                        'Min exam result': a[14] + '.' + a[14]
                                        }, ignore_index=True)
                    if re.search(r"COMPDAT\b|DATES\b|WEFAC\b", str(data[k])): break
                            
            elif re.search(r"DATES\b", str(data[i - 1])):
                for k in range(i, len(data)):
                    data[k] = str(self.parse_keyword_DATE_line(data[k]))
                    if re.search(r"W[0-9]|\d", data[k]):
                        a = re.findall(r'\w+.', data[k])
                        self.result = self.result.append({'Date': a[0] + " " + a[1] + " " + a[2],
                                        'Decoder': '',
                                        'Section number': '',
                                        'Participants': '',
                                        'Foreign participants': '',
                                        'Min team number': '',
                                        'Max team number': '',
                                        'Registration': '',
                                        'Exam': '',
                                        'Leader': '',
                                        'Lead assistent': '',
                                        'JR Lead assistent': '',
                                        'Flag': '',
                                        'Uniform': '',
                                        'Shoes': '',
                                        'Min exam result': ''
                                        }, ignore_index=True)
                    if re.search(r"COMPDAT\b|DATES\b|WEFAC\b", str(data[k])): break
                    

    
    def transform_and_roll_out(self):
        data = self.data_reader()
        clean_data = self.data_cleaner(data)
        clean_data_with_default = self.mystery_default_func(clean_data)
        Data = self.data_spliter(clean_data_with_default)
        self.final_parsing(Data)
        display(self.result)
                


# In[7]:





# In[ ]:




