from bs4 import BeautifulSoup as bs
import requests,pandas
url='https://www.scrapethissite.com/pages/simple/'
res=requests.get(url)
soup =bs(res.content,'lxml')
country_info=soup.find_all('div',{'class':'country'})

countries=[]
for country in country_info:
    country_name=country.find('h3').text.strip()
    capital=country.find('span',{'class':'country-capital'}).text.strip()
    population=country.find('span',{'class':'country-population'}).text.strip()
    area=country.find('span',{'class':'country-area'}).text.strip()

    data={
    'country name':country_name,
    'capital city':capital,
    'population':population,
    'area':area
     }
    countries.append(data)
    
df=pandas.DataFrame(countries)
df.to_excel('country list.xlsx',index=False)
