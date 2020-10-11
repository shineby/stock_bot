import sys
from pykiwoom.kiwoom import *

# https://wikidocs.net/84079
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")

