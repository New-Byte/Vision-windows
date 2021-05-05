from abcd import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.uic import loadUiType
import sys
import pyttsx3 as spk
import os
import threading

class Abcd(Ui_MainWindow):
        def __init__(self, window):
                self.setupUi(window)
                self.pushButton.clicked.connect(self.start)
                self.pushButton_2.clicked.connect(self.features)
                self.pushButton_3.clicked.connect(self.exit)

        def initiate(self):
                os.system("vision --cli")
        
        def start(self):
                x = threading.Thread(target=self.initiate, args=())
                x.start()
                t_ime = QTime.currentTime()
                time = t_ime.toString()
                d_ate = QDate.currentDate()
                date = d_ate.toString()
                label_time = "Time :" + time +" \n "+ "Date :" + date
                self.real_date_time.setText(label_time)

                self.label = QtGui.QMovie("C:\\Vision\\Vision-windows\\Vision\\gui\\listen.gif")
                self.Gif_1.setMovie(self.label)
                self.label.start()

        def features(self):
                spk.speak("My name is Vision, I can perform various system task, I can launch any application, I am able to browse internet and explore wikipedia, I am able to talk with you and i can make you laugh, I can quote life and read the books, I can speak various languages, I am able to access your computer and i can control it to some extent, i can stream youtube videos and i can open any file or folder for you and much more")
        def exit(self):
                spk.speak("Sayonara...")
                spk.speak("Terminating...")
                os.system("taskkill /F /IM python.exe /T")
                os.system("taskkill /F /IM cmd.exe")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Abcd(MainWindow)

MainWindow.show()
app.exec_()



