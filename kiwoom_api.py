import sys
from pykiwoom.kiwoom import *
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 39a675b826938a3968bf01f29ff94d12aaa22cd8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

# https://wikidocs.net/84079

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
<<<<<<< HEAD
=======
=======

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")
>>>>>>> e0ad4f6275af57bf10100ba15f93a73248e30aa1
>>>>>>> 39a675b826938a3968bf01f29ff94d12aaa22cd8
