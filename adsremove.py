import pyautogui
import time

########## sideload FideliZi!, Ajuda FideliZi! and File manager ##########
sideload = None
while sideload is None:
      sideload = pyautogui.locateOnScreen('sideload.png', grayscale= True)
pyautogui.click(sideload)


