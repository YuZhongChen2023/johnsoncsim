import requests
from bs4 import BeautifulSoup

url = "https://www1.pu.edu.tw/~tcyang/course.html"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select("a")

for x in result:
	print(x.text)
	print(x.get("href"))
	print()

print("h3的標題為:")
result=sp.select("h3")
for x in result:
	print(x.text)	