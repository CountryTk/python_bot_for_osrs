
from pyautogui import *
from PIL import Image
from time import sleep

FAILSAFE = True

def main():
    log = locateCenterOnScreen(r'images\willow_log.png')
    knife = locateCenterOnScreen(r'images\knife2.png')
     #gets the pic on screeen
    #x1 , y1 = longbowlocation
    print("Position of the knife {}".format(knife))
    print("Position of your log {}".format(log))
    
    while True:
        click(log, duration=1)
        sleep(1)#Wont detect the image with less time
        longbowlocation = locateCenterOnScreen(r'images\long_bow.png')
        print(longbowlocation)
        if longbowlocation != None:
            click(longbowlocation, duration=0.92)
        break
       
    


main()