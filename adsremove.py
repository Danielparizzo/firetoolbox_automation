import pyautogui

lockscreen = None
while lockscreen is None:
      lockscreen = pyautogui.locateOnScreen('lockscreen.png', grayscale = True)
pyautogui.click('lockscreen.png')

removeads = None
while removeads is None:
      removeads = pyautogui.locateOnScreen('removeadshover.png', grayscale = True)
pyautogui.moveTo(removeads), pyautogui.moveRel(270, 0), pyautogui.click()

executetool = None
while executetool is None:
      executetool = pyautogui.locateOnScreen('executetool.png', grayscale = True)
pyautogui.click('executetool.png')