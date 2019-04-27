import csv
import requests
from bs4 import BeautifulSoup
url='https://finance.yahoo.com/trending-tickers'
respone=requests.get(url)
f=csv.writer(open("input.txt","w"))
data=respone.content
soup=BeautifulSoup(data,'html.parser')
table1=soup.findAll('td',class_='data-col0 Ta(start) Pstart(6px) Pend(15px)')
table2=soup.findAll('td',class_='data-col1 Ta(start) Pstart(10px) Miw(180px)')
for l,l1 in zip(table1,table2):
    #print(l.text,l1.text)
    f.writerow([l.text,l1.text])

