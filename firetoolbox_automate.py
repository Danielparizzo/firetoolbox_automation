import pyautogui
import time

pyautogui.press('win')
pyautogui.write('Fire')
pyautogui.press('enter')

########## ADB Shell - Set sleep time to 10 min ##########
adbshell = None
while adbshell is None:
      adbshell = pyautogui.locateOnScreen('1adbshell.png', grayscale = True)    

time.sleep(1)
pyautogui.click(adbshell), pyautogui.write('settings put system screen_off_timeout 600000'), pyautogui.press('enter')

adbshellexit = None
while adbshellexit is None:
      adbshellexit = pyautogui.locateOnScreen('1adbshellexitx.png', grayscale = True)  
pyautogui.click(adbshellexit)

########## Install Nova Launcher ##########
launcher = None
while launcher is None:
      launcher = pyautogui.locateOnScreen('buttonlauncher.png', grayscale = True)    
pyautogui.click(launcher)

dropdown = None
while dropdown is None:
      dropdown = pyautogui.locateOnScreen('buttondropdown.png', grayscale = True)    
pyautogui.click(dropdown)

time.sleep(1)

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

########## Remove lockscreen amazon ads ##########
lockscreen = None
while lockscreen is None:
      lockscreen = pyautogui.locateOnScreen('lockscreen.png', grayscale= True)
pyautogui.click(lockscreen)

removeads = None
while removeads is None:
      removeads = pyautogui.locateOnScreen('removeadshover.png', grayscale= True)
pyautogui.moveTo(removeads), pyautogui.moveRel(270, 0), pyautogui.click()

executetool = None
while executetool is None:
      executetool = pyautogui.locateOnScreen('executetool.png', grayscale= True)
pyautogui.click(executetool)

removeadesyes = None
while removeadesyes is None:
      removeadesyes = pyautogui.locateOnScreen('removeadesyes.png', grayscale= True)
pyautogui.click(removeadesyes)
pyautogui.press('enter')

time.sleep(10), pyautogui.moveRel(0, 90), pyautogui.click(), pyautogui.press('enter')

removeadsback = None
while removeadsback is None:
      removeadsback = pyautogui.locateOnScreen('removeadsback.png', grayscale= True)
pyautogui.click(removeadsback)

########## debloat unnecessary app ##########
debloat = None
while debloat is None:
      debloat = pyautogui.locateOnScreen('debloat.png', grayscale= True)
pyautogui.click(debloat)

debloatdropdown = None
while debloatdropdown is None:
      debloatdropdown = pyautogui.locateOnScreen('debloatdropdown.png', grayscale= True)
pyautogui.click(debloatdropdown)

time.sleep(1)

standarddebloat = None
while standarddebloat is None:
      standarddebloat = pyautogui.locateOnScreen('standarddebloat.png', grayscale= True)
pyautogui.click(standarddebloat)

executedebloat = None
while executedebloat is None:
      executedebloat = pyautogui.locateOnScreen('executedebloat.png', grayscale= True)
pyautogui.click(executedebloat)

debloatok = None
while debloatok is None:
      debloatok = pyautogui.locateOnScreen('debloatok.png', grayscale= True)
pyautogui.click(debloatok)
pyautogui.press('enter')

########## move to page 2 ##########
nextpage = None
while nextpage is None:
      nextpage = pyautogui.locateOnScreen('nextpage.png', grayscale= True)
pyautogui.click(nextpage)

########## remove searchbar on lockscreen ##########
settings = None
while settings is None:
      settings = pyautogui.locateOnScreen('settings.png', grayscale= True)
pyautogui.click(settings)

disablesearchbard = None
while disablesearchbard is None:
      disablesearchbard = pyautogui.locateOnScreen('disablesearchbard.png', grayscale= True)
pyautogui.click(disablesearchbard), pyautogui.moveRel(280, 0), pyautogui.click()

settingsback = None
while settingsback is None:
      settingsback = pyautogui.locateOnScreen('settingsback.png', grayscale= True)
pyautogui.click(settingsback)
