import mysql.connector
import re
import requests
from bs4 import BeautifulSoup
conn=mysql.connector.connect(user='root',password='kistaiahgaripooja',host='localhost',database='stock')
mycursor=conn.cursor()
sql = "INSERT INTO profilestable(prof_ticker,name,Address,phonenum,website,sector,industry,full_time,bus_summ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
ind=0
list=['GOOG','CRON','STX','AAPL','ACB','GLUU']
list1=['Alphabet Inc','Cronos Group Inc','Seagate Technology plc','Apple Inc','Aurora Cannabis Inc','Glu Mobile Inc']
while ind<len(list1):
    f = open('C:/Users/pooja/PycharmProjects/PythonProject/'+ list1[ind] + '/Profile.html','r')
    soup = BeautifulSoup(f, 'html.parser')
    name = soup.find('h3', class_='Fz(m) Mb(10px)')
    print(name.get_text())
    t = soup.find(class_='D(ib) W(47.727%) Pend(40px)')
    t1 = t.findAll('a')
    for i in t1:
        if i.get('data-reactid') == '15':
            a= i.get_text()
            print(a)
        if i.get('data-reactid') == '17':
            webadd = i.get_text()
            print(webadd)
    add = soup.find('p', attrs={'data-reactid': '8'})
    print(add.text)
    si = soup.findAll('span', class_='Fw(600)')
    for row1 in si:
        if row1.get('data-reactid') == '21':
            sector = row1.get_text()
            print(sector)
        if row1.get('data-reactid') == '25':
            indu = row1.get_text()
            print(indu)
        if row1.get('data-reactid') == '29':
            fulltime = row1.get_text()
            print(fulltime)
    val = (list[ind], name.get_text(), add.text,a, webadd, sector, indu, fulltime,'summery')
    mycursor.execute(sql,val)
    conn.commit()
    ind+=1
    print(mycursor.rowcount,'record inserted')
