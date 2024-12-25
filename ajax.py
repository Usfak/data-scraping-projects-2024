from bs4 import BeautifulSoup as bs
import requests, pandas
datas=[]
url='https://www.scrapethissite.com/pages/ajax-javascript/'
res=requests.get(url)
soup=bs(res.content,'lxml')
years=[a.text for a in soup.find_all('a',{'class':'year-link'})]

for year in years: 
    url=f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={year}'
    res=requests.get(url) 
    datas.extend(res.json())
    
df=pandas.DataFrame(datas)
df.to_excel('ajex.xlsx',index=False)