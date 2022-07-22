from urllib import response
from bs4 import BeautifulSoup
import requests

url = "https://www.nate.com/"
response = requests.get(url)
source = response.text


#print(source)
#rso > div:nth-child(2) > div > div:nth-child(2) > div
#li > a > span.txt_rank

soup = BeautifulSoup(source,'html.parser')

#result = soup.select("#olLiveIssueKeyword > li:nth-child(2) > a > span.txt_rank")
result = soup.select("#olLiveIssueKeyword > li > a > span.txt_rank")
print(result)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(result[0].text)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for top in result:
    print(top.text)