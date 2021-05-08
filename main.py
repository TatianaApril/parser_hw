#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pars_core.sch_parser import Parser

keywords = ("DATES", "COMPDAT", "COMPDATL")
path = r"C:\Users\asus\parser\files\test_schedule.inc"
out_path = r"C:\Users\asus\parser\files\fine_schedule.csv"

parser = Parser(path, keywords)
parser.transform_and_roll_out()
chedule_df = parser.result
chedule_df.to_csv(path_or_buf = out_path, header=True, sep=',', index=False, encoding='utf-8-sig')

