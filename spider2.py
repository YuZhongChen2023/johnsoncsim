import requests
from bs4 import BeautifulSoup

url = "https://www1.pu.edu.tw/~tcyang/course.html"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".team-box")

for x in result:
	print(x.find("h4").text)
	print(x.find("p").text)
	print(x.find("a").get("href"))
	print("https://www1.pu.edu.tw/~tcyang/" +x.find("img").get("src"))
	print()