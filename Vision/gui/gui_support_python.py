from abcd import *
import sys
import speech_recognition as sr
import pyttsx3 as spk
import os

class Abcd(Ui_MainWindow):
        def __init__(self, window):
                self.setupUi(window)
                self.pushButton.clicked.connect(self.start)
                self.pushButton_2.clicked.connect(self.features)
                self.pushButton_3.clicked.connect(self.exit)

        
        
        def start(self):
                os.system("vision --cli")

        def features(self):
                spk.speak("I can perform various system task, I can launch any application, I am able to browse internet and explore wikipedia, I am able to talk with you and i can make you laugh, I can quote life and read the books, I can speak various languages, I am able to access your computer and i can control it to some extent, i can stream youtube videos and i can open any file or folder for you and much more")
                engine.runAndWait()
        def exit(self):
                spk.speak("sayonara...")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Abcd(MainWindow)

MainWindow.show()
app.exec_()



