import mysql.connector
import requests
import re
from bs4 import BeautifulSoup
conn = mysql.connector.connect(user='root',password='kistaiahgaripooja',host='localhost',database='Stock')
cursor=conn.cursor()
sql = "INSERT INTO financestable(Fin_ticker,TotalRevenue,costofRevenue,IncomeBeforeTax,NetIncome) VALUES (%s,%s,%s,%s,%s)"
i=0
list_ticker=['GOOG','CRON','STX','AAPL','ACB','GLUU']
list_name=['Alphabet Inc','Cronos Group Inc','Seagate Technology plc','Apple Inc','Aurora Cannabis Inc','Glu Mobile Inc']
while i<len(list_name):
    path = "C:/Users/pooja/PycharmProjects/PythonProject/" + list_name[i] + "/Finance.html"
    file1 = open(path, "r")
    soup = BeautifulSoup(file1, 'html.parser')
    row = soup.findAll('td', class_='Fz(s) Ta(end) Pstart(10px)')
    for t in row:
        if t.get('data-reactid') == '42':
            tot= t.get_text()
            print(tot)
        if t.get('data-reactid') == '53':
            costrevenue = t.get_text()
            print(costrevenue)
        if t.get('data-reactid') == '172':
            income = t.get_text()
            print(income)
    t1 = soup.findAll('td', class_='Fw(600) Ta(end) Py(8px) Pt(36px)')
    for k in t1:
        if k.get('data-reactid') == '247':
            net = k.get_text()
            print(net)

    val = (list_name[i],tot,costrevenue,income,net)
    cursor.execute(sql, val)
    conn.commit()
    i += 1
    print(cursor.rowcount, 'record inserted')
