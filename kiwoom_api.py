import sys
import backtrader as bt
from datetime import datetime
from pykiwoom.kiwoom import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

# https://wikidocs.net/84079
# finance reader https://financedata.github.io/posts/finance-data-reader-users-guide.html


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,150)
        self.update_statusbar("disconnected")

        btn_login = QPushButton("Login", self)
        btn_login.move(20, 20)
        btn_login.clicked.connect(self.onclicked_btn_login)

    def update_statusbar(self, msg):
        self.statusBar().showMessage(msg)

    def onclicked_btn_login(self):
        kiwoom = Kiwoom()
        kiwoom.CommConnect(block=True)
        state = kiwoom.GetConnectState()
        if state == 1:
            self.update_statusbar("connected")        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")
