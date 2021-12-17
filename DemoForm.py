# DemoForm.py
# DemoForm.py (로직을 구현) + DemoForm.py (화면 디자인)

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

# 화면을 로딩
form_class = uic.loadUiType("c:\\work\\DemoForm.ui")[0]


# 윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt화면")


# 진입점을 체크해서 설정
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()

