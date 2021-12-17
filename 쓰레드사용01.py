import sys 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 

class Worker(QThread):
    def run(self):
        while True:
            print("hello~~")
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start() 

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_() 

        