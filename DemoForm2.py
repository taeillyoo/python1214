# DemoForm2.py
# DemoForm2.py (로직을 구현) + DemoForm2.py (화면 디자인)

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

import urllib.request
from bs4 import BeautifulSoup


# 화면을 로딩
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]


# 윈도우 클래스 정의 (부모 클래스: QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯 메서드 추가
    def firstClick(self):
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
        self.label.setText("웹툰가져오기 종료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")


# 진입점을 체크해서 설정
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()

