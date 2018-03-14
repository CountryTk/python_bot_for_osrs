
from pyautogui import *
from PIL import Image
from time import sleep
import random
from pymsgbox import alert
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


FAILSAFE = True

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Python bot'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        #self.setWindowIcon(QIcon()
        self.willow_log = r'images\willow.png'
        self.maple_log = r'images\maple_log.png'
        self.yew_log = None
        self.magic_log = None
        self.knife_willows = r'images\knife_willow.png'
        self.willow_long_bow = r'images\long_bow.png'
        self.main() #running the main func

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
            sleep(1)
            if knife == None:
                print('shit')
            click(knife, duration=0.92)
            sleep(1)
            long_bow_image = locateCenterOnScreen(self.willow_long_bow)
            click(long_bow_image, duration=duration_time)
            sleep(50)
            alert(text='Please bank your longbows and take a fresh inventory of willow logs', title='Alert!', button='OK') #It takes approx 50 seconds to fletch the whole inv

    def maple(self):
        image = locateCenterOnScreen(self.maple_log)
        if image == None:
            print("fuck i messed up")
        else: 
            click(image, duration=0.92)
    def main(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.button = QPushButton('Willows',self)
        self.button.clicked.connect(self.willow)
        self.show()
        #if choice == "willow":
            #self.willow()
       # elif choice == "maple":
            #self.maple()
        







if __name__ == '__main__':

    app = QApplication(sys.argv)
    go = main()
    sys.exit(app.exec_())
    
    
