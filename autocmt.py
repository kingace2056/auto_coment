import pyautogui
import time
import random
from pynput.mouse import Button,Controller 
mouse = Controller()

# in powershell below give following commands 
#       pip install pyautogui
#       pip install pynput 

#Uncomment the lines below to find out cursor position
# a=mouse.position
# print(a)

####dont forget to comment these lines while finding out 
###change values in range to specify number of comments to be done



for i in range(20):
# This is where you need to make changes in order to post required comment
#in the cmtList ; Put your required comment and let the program do remaining work 
    cmtList = ['Goli OP <3 <3 ','Goli Le hanxa hai aaba','Hello guys','Goli ko supporters le Goli OP lekham hai','Dont Spam Hai Guys','Revival Gaming OP','Revival OP','Dai audience alli kam vaye hai ', 'Goli OP <3 <3 ']
    mouse.position = (851, 256)
    #alter values in sleep for desired delay in comments . I prefer keeping all of them 2 to avoid getting banned .
    time.sleep(1)
    pyautogui.click()
    #insert your comments here 
    pyautogui.typewrite(random.choice(cmtList))
    # pyautogui.typewrite("Goli op <3 <3  ECN OP <3 <3 <3 ")
    time.sleep(1)
    mouse.position = (855, 309)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    



