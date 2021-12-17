import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import * 
import pybithumb
import time 

tickers = ["BTC","ETH","BCH","ETC"]
#loadUiType()함수로 미리 생성한 파일을 로딩한다. 
form_class = uic.loadUiType("bull.ui")[0]

#다중 쓰레드를 사용하는 예제 
#아래와 같이 처리하면 UI는 그대로 반응하면서 별도 작업을 진행할 수 있다. 
class Worker(QThread):
    #새로운 시그널(이벤트)를 추가한다. 
    finished = pyqtSignal(dict)

    def run(self):
        while True:
            data = {} 

            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)
            print(data)
            #시그널(이벤트)객체를 생성한다. 
            self.finished.emit(data)
            time.sleep(2)

    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            #코드에 오류가 있어서 특정 컬럼명으로 받아오기(21/9/7)
            print(df[['open', 'close']])
            ma5 = df['close'].rolling(window=5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)

            state = None
            if price > last_ma5:
                state = "상승장"
            else:
                state = "하락장"

            return price, last_ma5, state
        except:
            return None, None, None 

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = Worker() 
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start() 

    @pyqtSlot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)

                self.tableWidget.setItem(index, 0, QTableWidgetItem(str(ticker)))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(str(infos[0])))
                self.tableWidget.setItem(index, 2, QTableWidgetItem(str(infos[1])))
                self.tableWidget.setItem(index, 3, QTableWidgetItem(str(infos[2])))
        except:
            pass 

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_() 
