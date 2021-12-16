# web2.py

import urllib.request
from bs4 import BeautifulSoup

#동적으로 페이지 번호 생성
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

for i in range(1, 6):
    urlStr = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri" + "&page=" + str(i)
    print(urlStr)
    data = urllib.request.urlopen(urlStr)
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        link = item.find("a")["href"]
        print(title)
        # print(link)
        f.write(title + "\n")

f.close()