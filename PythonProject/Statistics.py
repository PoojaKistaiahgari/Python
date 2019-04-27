import mysql.connector
import re
from bs4 import BeautifulSoup
conn= mysql.connector.connect(user='root',password='kistaiahgaripooja',host='localhost',database='Stock')
cursor=conn.cursor()
insert="INSERT INTO statisticstable(sno,stat_ticker,marketcap,enterprise_value,return_on_assets,total_cash,operating_cash_flow,levered_free_cash_flow,total_debt,current_ratio,gross_profit,proffit_margin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
i=0
list_ticker=['GOOG','CRON','STX','AAPL','ACB','GLUU']
list_name=['Alphabet Inc','Cronos Group Inc','Seagate Technology plc','Apple Inc','Aurora Cannabis Inc','Glu Mobile Inc']
while i<len(list_name):
    path = "C:/Users/pooja/PycharmProjects/PythonProject/" + list_name[i] + "/Statistics.html"
    file1 = open(path, "r")
    soup = BeautifulSoup(file1, 'html.parser')
    data1 = soup.findAll('td', class_='Fz(s) Fw(500) Ta(end)')
    for row in data1:
        if row.get('data-reactid') == '19':
            marketcap = row.get_text()
            print(marketcap)
        if row.get('data-reactid') == '26':
            evalue = row.get_text()
            print(evalue)
        if row.get('data-reactid') == '131':
            roassets = row.get_text()
            print(roassets)
        if row.get('data-reactid') == '211':
            totalcash = row.get_text()
            print(totalcash)
        if row.get('data-reactid') == '258':
            opcashflow = row.get_text()
            print(opcashflow)
        if row.get('data-reactid') == '265':
            levelcashflow = row.get_text()
            print(levelcashflow)
        if row.get('data-reactid') == '225':
            totaldebt = row.get_text()
            print(totaldebt)
        if row.get('data-reactid') == '239':
            currentratio = row.get_text()
            print(currentratio)
        if row.get('data-reactid') == '171':
            grossprofit = row.get_text()
            print(grossprofit)
        if row.get('data-reactid') == '112':
            profitmargin = row.get_text()
            print(profitmargin)

    val=(i,list_name[i],marketcap,evalue,roassets,totalcash,opcashflow,levelcashflow,totaldebt,currentratio,grossprofit,profitmargin)
    cursor.execute(insert, val)
    conn.commit()
    i += 1
    print(cursor.rowcount, 'record inserted')



