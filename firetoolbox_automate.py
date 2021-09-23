import pyautogui
import time

### ADB Shell
adbshell = None
while adbshell is None:
      adbshell = pyautogui.locateOnScreen('1adbshell.png', grayscale = True)    

time.sleep(1)
pyautogui.click(adbshell), pyautogui.write('settings put system screen_off_timeout 600000'), pyautogui.press('enter')

adbshellexit = None
while adbshellexit is None:
      adbshellexit = pyautogui.locateOnScreen('1adbshellexitx.png', grayscale = True)  
pyautogui.click(adbshellexit)

### Install Nova Launcher
launcher = None
while launcher is None:
      launcher = pyautogui.locateOnScreen('buttonlauncher.png', grayscale = True)    
pyautogui.click(launcher)

dropdown = None
while dropdown is None:
      dropdown = pyautogui.locateOnScreen('buttondropdown.png', grayscale = True)    
pyautogui.click(dropdown)

nova = None
while nova is None:
      nova = pyautogui.locateOnScreen('buttonnova.png', grayscale = True)    
pyautogui.click(nova)

widgets = None
while widgets is None:
      widgets = pyautogui.locateOnScreen('widgets.png', grayscale = True)    
pyautogui.click(widgets)

launcherinstall = None
while launcherinstall is None:
      launcherinstall = pyautogui.locateOnScreen('launcherinstall.png', grayscale = True)    
pyautogui.click(launcherinstall)

buttonoklauncher = None
while buttonoklauncher is None:
      buttonoklauncher = pyautogui.locateOnScreen('buttonoklauncher.png', grayscale = True)
pyautogui.click(buttonoklauncher), pyautogui.press('enter')
