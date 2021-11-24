import pandas as pd
import os

dir = os.path.dirname(os.path.realpath('__file__'))
print(dir)
file_path = dir + '\\part2\\read_csv_sample.csv'

df1=pd.read_csv(file_path)
print(df1)
df2=pd.read_csv(file_path, header=None)
print(df2)

df3= pd.read_csv(file_path, index_col='c0')
print(df3)

url=dir+'\\part2\\sample.html'
tables=pd.read_html(url)

import lxml

from bs4 import BeautifulSoup
import requests
import re

url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp=requests.get(url)
soup=BeautifulSoup(resp.text, 'lxml')
rows=soup.select('div>ul>li')

etfs={}

for row in rows:
    try:
        etf_name=re.findall('^(.*) \(NYSE',row.text)
        etf_market= re.findall('\((.*)\|', row.text)
        etf_ticker= re.findall('NYSE Arca\|(.*)\)', row.text)

        if (len(etf_ticker)>0) & (len(etf_market)>0) & (len(etf_name)>0):
            etfs[etf_ticker[0]]= [etf_market[0], etf_name[0]]

    except AttributeError as err:
        pass


print(etfs)

import googlemaps

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df=pd.DataFrame(data)
print(df)

df.set_index('name',inplace=True)
print(df)
df.to_csv(file_path)

data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
         'algol' : [ "A", "A+", "B"],
         'basic' : [ "C", "B", "B+"],
          'c++' : [ "B+", "C", "C+"]}

data2 = {'c0':[1,2,3], 
         'c1':[4,5,6], 
         'c2':[7,8,9], 
         'c3':[10,11,12], 
         'c4':[13,14,15]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

writer=pd.ExcelWriter(dir+'\\part2\\df_excelwriter123.xlsx')
df1.to_excel(writer, sheet_name='sheet1')
df2.to_excel(writer, sheet_name='sheet2')
writer.save()

df= pd.read_csv(dir+'\\part3\\auto-mpg.csv', header=None)
df.head()

df.columns= ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

print(df.shape)

print(df.info())
print(df.dtypes)

print(df.mpg.dtypes)

print(df.describe())
print(df.describe(include='all'))

print(df.count())

unique_value= df['origin'].value_counts(dropna=True)
print(unique_value)

print(type(unique_value))