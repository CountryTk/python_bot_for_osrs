
from pyautogui import *
from PIL import Image
from time import sleep
import random
import threading
from pymsgbox import alert
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5 import QtTest


FAILSAFE = True

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Python bot'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 340
        self.threading = Thread()
        self.threading.start()
        #self.setWindowIcon(QIcon()
        self.willow_log = r'images\willow.png'
        #self.maple_log = r'images\maple_log.png'
        #self.yew_log = None
        #self.magic_log = None

        #self.knife_willows = r'images\knife_willow.png'
        #self.willow_long_bow = r'images\long_bow.png'
        self.backpack_image = r'images\backpack_loadout.png'
        self.python_power = r'images\python_powered.png'
        self.main()  # running the main func

    
    def main(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        
        #creating willow button

        button = QPushButton('Willow longbows',self)
        button.move(0,310)
        button.clicked.connect(self.threading.willow)

        #creating maple button

        self.button_maple = QPushButton("Maple longbows", self)
        self.button_maple.clicked.connect(self.threading.maple)
        self.button_maple.move(100,310)

        #creating yew longbow button
        self.button_yew = QPushButton('Yew longbows', self)
        self.button_yew.clicked.connect(self.threading.yew)
        self.button_yew.move(190,0)

        #creating magic longbow button
        self.button_magic = QPushButton("Magic longbows", self)
        self.button_magic.clicked.connect(self.threading.magic)
        self.button_magic.move(290, 0)
        #Creating a new label for our image
        self.backpack_loadout_label = QLabel(self)
        self.backpack_image_label = QPixmap(self.backpack_image)
        self.backpack_loadout_label.setPixmap(self.backpack_image_label)
        self.backpack_loadout_label.resize(self.backpack_image_label.width(), self.backpack_image_label.height())
        
        
        #Creating the reccommendation label and adding text to it

        self.rec_label = QLabel(self)
        self.rec_label.move(10, 260)
        self.rec_label.resize(185,10)
        self.rec_label.setText("You must use this backpack loadout ^")
        
        #Python power
        self.python_label = QLabel(self)
        self.python_label_pixmap = QPixmap(self.python_power)
        self.python_label.setPixmap(self.python_label_pixmap)
        self.python_label.resize(200,160)
        
        self.python_label.move(260, 180)
        
        self.show()
        
#Creating a new class for threading
class Thread(QThread):
    def __init__(self):
        super().__init__()
        self.willow_log = r'images\willow.png'
        self.maple_log = r'images\maple_log.png'
        self.yew_log = None
        self.magic_log = None
        self.python_power = r'images\python_powered.png'
        self.knife_willows = r'images\knife_willow.png'
        self.willow_long_bow = r'images\long_bow.png'
        self.backpack_image = r'images\backpack_loadout.png'
    
    def willow(self):
        duration_time = random.uniform(0.80, 1.35)
        #print(duration_time)
        #finding the log
        knife = locateCenterOnScreen(self.knife_willows) 
        log_image = locateCenterOnScreen(self.willow_log)
        if log_image == None or self.knife_willows == None:
            print("u fucked up, try again")
        else:
            click(log_image, duration=duration_time)
            QtTest.QTest.qWait(1000)
            if knife == None:
                print('shit')
            click(knife, duration=0.92)
            QtTest.QTest.qWait(1000)
            long_bow_image = locateCenterOnScreen(self.willow_long_bow)
            click(long_bow_image, duration=duration_time)
            QtTest.QTest.qWait(50000)
            alert(text='Please bank your longbows and take a fresh inventory of willow logs', title='Alert!', button='OK') #It takes approx 50 seconds to fletch the whole inv

    def maple(self):
        image = locateCenterOnScreen(self.maple_log)
        if image == None:
            alert('Error, maple logs not FUCKING FOUND', 'shit', 'OK')
        else: 
            click(image, duration=0.92)
    def yew(self):
        pass
    def magic(self):
        pass




if __name__ == '__main__':

    app = QApplication(sys.argv)
    go = main()
    sys.exit(app.exec_())
    
    

