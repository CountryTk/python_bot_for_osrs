import os
from pyautogui import *
from PIL import Image
from time import sleep
import random
import threading
import win32gui
import psutil
from pymsgbox import alert
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5 import QtTest


FAILSAFE = True
x = None #Setting the variable to None so that the globals in classes could change it

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Python bot'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 340
        self.threading = Thread() #yes
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
        self.choose_client()  # running the main func
    def choose_client(self):
        question = prompt("Which client are you currently using?", "Client", "Konduit or OSbuddy?")
        question_new = question.title()
        if question_new == "Konduit" or question_new == "Osbuddy":
            self.konduit()
        else:
            os._exit(1) #Closing the program if the question is none aka cancel is pressed
            #If the input is konduit, run the konduit function

    def konduit(self):
        name = password('Enter your Konduit username') #getting the username of the client so we could find the window
        if name is None:
            os._exit(1)
        while name is not None:
            global x #Creating a global variable to use it in the main function to get the location of the konduit client
            x = win32gui.FindWindow(None, "Konduit Oldschool - " + name) #FInding the window using the name
            if x != 0:
                self.main_fletching()
                print(x)
                break #If the name matches to the window name then run the main function
            alert("Window not found, please open your konduit client and enter the correct username")
            name = password('Enter your Konduit username')
            if name is None:
                os._exit(1)
    def osbuddy(self):
        print("fuck you osbuddy with you and your client names OMG")

    def main_fletching(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        windoiw = win32gui.GetWindowRect(x)
        print(windoiw)
        #creating willow button

        button = QPushButton('Willow longbows',self)
        button.move(0,310)
        button.clicked.connect(self.threading.willow)

        #creating maple button

        button_maple = QPushButton("Maple longbows", self)
        button_maple.clicked.connect(self.threading.maple)
        button_maple.move(100,310)

        #creating yew longbow button
        button_yew = QPushButton('Yew longbows', self)
        button_yew.clicked.connect(self.threading.yew)
        button_yew.move(190,0)

        #creating magic longbow button
        button_magic = QPushButton("Magic longbows", self)
        button_magic.clicked.connect(self.threading.magic)
        button_magic.move(290, 0)
        #Creating a new label for our image
        backpack_loadout_label = QLabel(self)
        backpack_image_label = QPixmap(self.backpack_image)
        backpack_loadout_label.setPixmap(backpack_image_label)
        backpack_loadout_label.resize(backpack_image_label.width(), backpack_image_label.height())
        
        
        #Creating the recommendation label and adding text to it

        rec_label= QLabel(self)
        rec_label.move(10, 260)
        rec_label.resize(185,10)
        rec_label.setText("Optimal backpack loadout ^")

        #Python power
        python_label = QLabel(self)
        python_label_pixmap = QPixmap(self.python_power)
        python_label.setPixmap(python_label_pixmap)
        python_label.resize(200,160)
        
        python_label.move(260, 180)
        
        self.show()
    def main_woodcutting(self):
        pass
#Creating a new class for threading
class Thread(QThread):
    def __init__(self):
        super().__init__()
        self.willow_log = r'images\willow_log.png'
        self.maple_log = r'images\maple_log.png'
        self.yew_log = None
        self.magic_log = None
        self.python_power = r'images\python_powered.png'
        self.knife_willows = r'images\knife_willow.png'
        self.willow_long_bow = r'images\long_bow.png'
        self.backpack_image = r'images\backpack_loadout.png'
        self.maple_knife = r'images\knife_maple.png'
        self.maple_long_bow = r'images\maple_longbow.png'
        self.wrench = r'images\wrench.png'
        self.screen = r'images\screen.png'
        self.backpack = r'images\backpack.png'

    def willow(self):
        duration_time = random.uniform(0.80, 1.35)
        #print(duration_time)
        #finding the log
        knives = os.listdir(r'knife_images')
        wrench = locateCenterOnScreen(self.wrench)
        logs = os.listdir(r'willow_images')
        def logfletch():
            for knifes in knives: #First we find the knife in the knives list
                knife = r'knife_images/' + knifes #Then we attach knife to the relative path
                detected_knife = locateCenterOnScreen(knife)
                #Now we're trying to locate the knife on the screen
                if detected_knife is not None: #If we found the knife then set running to true
                    running = True

                    while running: #While running is true print knife found and click on it then stop the while loop
                        print("Knife found!")
                        click(detected_knife, duration=duration_time)
                        running = False

                    for log in logs: #After the while loop is stopped, jump to this loop
                        log_new = r'willow_images/' + log
                        log_location = locateCenterOnScreen(log_new)
                        if log_location is not None:
                            running_log = True
                            while running_log: #When we found the log and running_log is true then click on the log, wait and click on the longbow image and then wait 50 seconds
                                print("Log found!")
                                click(log_location, duration=duration_time)
                                print("Waiting 2 seconds")
                                QtTest.QTest.qWait(2000)
                                print("Clicking on the longbow...")
                                long_bow_image = locateCenterOnScreen(self.willow_long_bow)
                                click(long_bow_image, duration=duration_time)
                                print("Waiting 50 seconds")
                                QtTest.QTest.qWait(49742)  # It takes approx 50 seconds to fletch the whole inventory
                                print("Inventory finished...")
                                break
                        else:
                            print("Finding the log...") #if we didnt find a log then print this until we find a log
                else:
                    print("Finding the knife...")

        if wrench is None: #If we don't find wrench on the screen aka the client is already in fixed mode then run the code below
            logfletch() #running the logfletch function that handles everything with willow longbow fletching

        else: #if the wrench isnt found on the screen then do this
            click(wrench, duration=.92)
            QtTest.QTest.qWait(1203)
            screen = locateCenterOnScreen(self.screen)
            click(screen, duration=.952)
            QtTest.QTest.qWait(901)
            backpack = locateCenterOnScreen(self.backpack)
            click(backpack, duration=.1023)
            QtTest.QTest.qWait(2031)
            logfletch() #After setting the screen to static size, run this function that handles the willow fletching

    def maple(self):
        duration_time = random.uniform(0.80, 1.35)
        wrench = locateCenterOnScreen(self.wrench)
        knives = os.listdir(r'knife_images')  # Listdir gets all the image names in the directory knife_images
        if wrench is None: #If the wrench is not found that means the client is already in fixed mode
            image = locateCenterOnScreen(self.maple_log)  # location image so the image would be found
            for knife in knives:
                if locateCenterOnScreen(knife) is None:
                    print('success')
            if image is None:
                alert('No logs found', 'Error')
            else:
                click(image, duration=duration_time)
                QtTest.QTest.qWait(1000)
                if knife is not None:
                    click(knife, duration=duration_time)
                    QtTest.QTest.qWait(2042)
                    maple_longbow = locateCenterOnScreen(self.maple_long_bow)
                    click(maple_longbow, duration=duration_time)
                else:
                    alert('No knife found', 'Error') #THen run this function that takes care of the botting part
        else: #if its not then we are going to put it on fixed mode
            click(wrench, duration=.92)
            QtTest.QTest.qWait(1203)
            screen = locateCenterOnScreen(self.screen)
            click(screen, duration=.952)
            QtTest.QTest.qWait(901)
            backpack = locateCenterOnScreen(self.backpack)
            click(backpack, duration=.1023)
            QtTest.QTest.qWait(2031)

        

    def yew(self):
        pass
    def magic(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    go = main()
    sys.exit(app.exec_())
