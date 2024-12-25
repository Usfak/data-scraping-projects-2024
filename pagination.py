from bs4 import BeautifulSoup as bs
import requests,pandas
page_num , datas = 1 , []
while True:
     url=f'https://www.scrapethissite.com/pages/forms/?page_num={page_num}&per_page=100'
     responce=requests.get(url)
     soup=bs(responce.content,'lxml')
     team=soup.find_all('tr',{'class':'team'})
     if team:
         for tr in team:
             data={td.get('class')[0] : td.text.strip() for td in tr.find_all('td')} 
             datas.append(data)
         page_num += 1  
     else:
        break
df=pandas.DataFrame(datas)
df.to_excel('pagelist.xlsx',index=False)

