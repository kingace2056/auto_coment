import pyautogui
import time
from pynput.mouse import Button,Controller 
mouse = Controller()

# in powershell below give following commands 
#       pip install pyautogui
#       pip install pynput 

#Uncomment the lines below to find out cursor position
# a=mouse.position
# print(a)

#dont forget to comment these lines while finding out 
# change values in range to specify number of comments to be done
for i in range(5):
    mouse.position = (847,303)
    #alter values in sleep for desired delay in comments . 
    time.sleep(1)
    pyautogui.click()
    #insert your comments here 
    pyautogui.typewrite('instagram.com/fiverrnp')
    time.sleep(1)
    mouse.position = (858, 351)
    time.sleep(3)
    pyautogui.click()
    time.sleep(1)
    



