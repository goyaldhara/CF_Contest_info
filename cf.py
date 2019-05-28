import requests
from bs4 import BeautifulSoup
def cf():
    url='https://codeforces.com/'
    resp=requests.get(url)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')
        l=soup.find("div",{"class":"roundbox sidebox"})
        for i in l.findAll("span"):
            x=i.text
            print(x)
            for j in l.findAll("a"):
                var2=j.text
                print(var2)
    else:
        print("Error,Internet connection is not available")

cf()
input("Press enter to exit ;)")
