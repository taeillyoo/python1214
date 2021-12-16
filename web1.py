# web1.py
from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# <p> 전부 검색
# print(soup.find_all("p"))
# print(soup.find("p"))
print(soup.find_all("p", class_="outer-text"))


