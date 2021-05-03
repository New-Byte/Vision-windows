from abcd import *
import sys
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)


class Abcd(Ui_MainWindow):
        def __init__(self, window):
                self.setupUi(window)
                self.pushButton.clicked.connect(self.start)
                self.pushButton_2.clicked.connect(self.features)
                self.pushButton_3.clicked.connect(self.exit)

        
        
        def start(self):
                engine.say("Good morning Sir I am start function")
                engine.runAndWait()

        def features(self):
                engine.say("My features ae I can perform all system task, web browsing iand also data analysis and visualization and many more ")
                engine.runAndWait()
        def exit(self):
                engine.say("I am going sir bye")
                engine.runAndWait()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Abcd(MainWindow)

MainWindow.show()
app.exec_()



