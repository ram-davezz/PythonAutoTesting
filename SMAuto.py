import pyautogui
from win32api import GetSystemMetrics
import os
print("SalesMate + Backup Menu Test")
print("Create a database directory called SMB")

path="D:/SMB"
if not os.path.exists(path):
    os.makedirs(path)

#width and height
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

#Launch Start Menu
print("Launch start menu")
pyautogui.FAILSAFE = False
pyautogui.click(0,height,1,2.0)

#To select SalesMate+ 
pyautogui.typewrite("SalesMate +",1.0)

#Launch SalesMate + and Delay 10Sec
pyautogui.press("enter",1,10)


#To cancel the setup wizard
pyautogui.typewrite("c",5)

#To close the tip of the day
pyautogui.press("enter",1,5)


#Select file folder using alt f
pyautogui.press(['alt','f'],1,2.0)

#invoke backup folder dialog
pyautogui.press("b",1,5)

#Go to D drive
pyautogui.press("N",1,2)

#To press right arrow
pyautogui.press("right",1,2)

#Go to SMB folder
pyautogui.typewrite("S",1)

#Press enter key to backup data
pyautogui.press("enter",1,3)

#Close the Successfully Dialog box
pyautogui.press("enter")

#Select view folder using alt v 
pyautogui.press(['alt','v'],1,2.0)

#Press F for fullscreen
pyautogui.press("f",1,2.0)

#Select view folder using alt v 
pyautogui.press(['alt','v'],1,2.0)

#Press F for exit fullscreen
pyautogui.press("f",1,2.0)


