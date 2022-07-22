from bs4 import BeautifulSoup
from numpy import source
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=068270&page=1"
response = requests.get(url,headers={'User-agent':'Mozilla/5.0'})
source = response.text

soup = BeautifulSoup(source,'lxml')
span_today = soup.find('span',class_="tah p11")


#(1) 마지막 페이지 찾아내기

td_pgRR = soup.find("td",class_="pgRR")

#print("td_pgRR :\n",td_pgRR)
#print("td_pgRR.text : \n",td_pgRR.text)
a_href= td_pgRR.a['href'] # /item/sise_day.nhn?code=068270&page=421
print(a_href)

a_href_split_list = a_href.split("=")
last_page = a_href_split_list[-1]
print("last_page :",last_page)


#전체페이지 읽어오기
'''base_url = "https://finance.naver.com/item/sise_day.nhn?code=068270"

for page in range(1,int(last_page)+1):
url = "{}&page={}".format(base_url,page)
response = requests.get(url,headers={'User-agent':'Mozilla/5.0'})
source = response.text'''

# 데이터 정제하기
import pandas as pd

df = pd.DataFrame()

base_url = "https://finance.naver.com/item/sise_day.nhn?code=068270"

'''for page in range(1,int(last_page)+1):
    url = "{}&page={}".format(base_url,page)
    response = requests.get(url,headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html_in_pd = pd.read_html(source, header=0)[0]
    #print(html)
    df = pd.concat([df, html_in_pd])'''

#테스트용 페이지수 줄임
for page in range(1,int(last_page)-450):
    url = "{}&page={}".format(base_url,page)
    response = requests.get(url,headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html_in_pd = pd.read_html(source, header=0)[0]
    #print(html)
    df = pd.concat([df, html_in_pd])
#print(df.to_string())

#(3) DataFrame 가공
df = df.dropna()
#df = df.iloc[]
print(df.to_string())
print("---------------------------------------------------------------------------------------------")
print(df)

#df = df.sort_values(by='날짜')
#print(df.to_string())
dics = []
for i in range(1,20):
    
    dic = {"날짜":"df[\"날짜\"][\i]",
           "종가":"df[\"종가\"][\i]",
           "전일비":"df[\"전일비\"][\i]",
           "시가":"df[\"시가\"][\i]",
           "고가":"df[\"고가\"][\i]",
           "저가":"df[\"저가\"][\i]",
           "거래량":"df[\"거래량\"][\i]"
    }
    dics.append(dic)

#print(dics)


#(4) 차트 그리기
import matplotlib.pyplot as plt
plt.title("TTTTTILTE")
plt.xticks(rotation=45)
plt.plot(df['시가'],df['종가'],'bx-')
plt.grid(color='gray', linestyle="--")
plt.show()