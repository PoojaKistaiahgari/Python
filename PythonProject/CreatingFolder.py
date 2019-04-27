import os

import urllib.request

f=open("input.txt","r")
for line in f:
    str=line.split(',')
    st=str[1].rstrip()
    path = "C:/Users/pooja/PycharmProjects/PythonProject/%s" % st
    os.mkdir(path)
    app=str[0]
    print(app)
    url=("https://finance.yahoo.com/quote/{}/profile?p={}".format(app,app))
    url1=("https://finance.yahoo.com/quote/{}/key-statistics?p={}".format(app,app))
    url2=("https://finance.yahoo.com/quote/{}/financials?p={}".format(app, app))
    url3=("https://finance.yahoo.com/quote/{}/summary?p={}".format(app, app))

    page=urllib.request.Request(url)
    #path="C:/Users/pooja/PycharmProjects/PythonProject/%s" %st
    fpath=os.path.join(path, "Profile.html")
    fpath1=os.path.join(path,"Statistics.html")
    fpath2=os.path.join(path, "Finance.html")
    fpath3=os.path.join(path, "Summary.html")

    urllib.request.urlretrieve(url,fpath)
    urllib.request.urlretrieve(url1,fpath1)
    urllib.request.urlretrieve(url2,fpath2)
    urllib.request.urlretrieve(url3,fpath3)


f.close()