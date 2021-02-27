import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import getopt
import requests
import base64
import json
import re
#import qdarkstyle
from QCandyUi import CandyWindow
import fofa_gui_ui_2


def search():
    email = ui.lineEdit.text()
    key = ui.lineEdit_2.text()
    rule = ui.lineEdit_3.text()
    numbers = ui.lineEdit_4.text()
    ui.textBrowser.setText("")#每次开始之前先将
    en_rule = (base64.b64encode(rule.encode())).decode("utf-8")
    
    query_url = "https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+en_rule+"&size="+numbers+"&fields=host"
    resp = requests.get(query_url).json()

    list1 = []

    for results in resp["results"]: #根据返回的json数据获取results
        
        #print(results)
        try:
            if "https" not in results:
                resp1 = requests.get("http://" + results, timeout=3, verify=False) #先判读https目标存活情况
                if resp1.status_code == 200:
                    target_url = "http://" + results
                    list1.append(target_url)       #存入列表
            else:
                list1.append(results)

        except Exception as e:
            print(e)

    list1 = list(set(list1))   #去重

    for lis in list1:
        ui.textBrowser.append(lis)
        ui.textBrowser.lineWrapMode()#设置自动换行
        try:
            with open ("fofa_api_2021.txt", "a") as f:
                f.write(lis+"\n")
        except Exception as e:
            print(e)
    
    f.close()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())#黑色主题美化
    ui = fofa_gui_ui_2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow = CandyWindow.createWindow(MainWindow, 'blue')
    MainWindow.show()
    ui.pushButton.clicked.connect(search)
    sys.exit(app.exec_())

