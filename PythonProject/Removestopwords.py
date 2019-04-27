import re
ticker=[]
tickerName=[]
file=open('input.txt','r')
for x in file:
    n=x.split(',')
    ticker.append(n[0].rstrip())
    tickerName.append(n[1].rstrip())
#print(ticker)
#print(tickerName)

#Entering a question and removing stopwords
f=open('stopwords.txt','r')
list=[]
for k in f:
    k=k.replace('"','')
    list.append(k.strip())
q=input("enter the question")
arr=[]
q1=q.split(" ")
for i in q1:
    if i not in list:
        arr.append(i)
print(arr)
list1= []
Dict = { 'statistics' : {'sno' : 'None','stat_ticker': 'what','marketcap' : 'what,how much','enterprise_value' : 'what,how much','return_on_assets' : 'how much,what','total_cash' :'what','operating_cash' : 'what','levered_free_cash_flow' : 'what','total_debt ': 'what','current_ratio' : 'what,how much','gross_profit' : 'what,how much','profit_margin' : 'what,how much'},
         'profiles' : {'prof_ticker' : 'what','name' : 'what','address' :'where,what','Phone_Number' : 'what','website' :'what','sector' : 'what, which','Industry' : 'what,which','full_time' : 'how many,what','bus_summ' : 'what'},
         'finances' : { 'Fin_ticker'  : 'what','Total_Revenue': 'how much,what','Cost_of_Revenue': 'how much,what','Income_Before_Tax' : 'how much,what','Net_Income' : 'what'}
          }
for word in arr:
    for type in Dict:
        #print(type)
        for type1 in Dict[type]:
            if word in Dict[type][type1]:
                #print(type+"--->"+type1)
                s=type+str("==>")+type1
                list1.append(s)
#print(list1)
for word in list[1:]:
    for line in list1:
        split_data=line.split("==>")
        if word in split_data[1]:
            print(word)
