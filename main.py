from pyautogui import *; import pyautogui; import time; from os import walk; from playsound import playsound; pyautogui.FAILSAFE = False
lineups = next(walk("lineups"), (None, None, []))[2]
while 1:
    for f in lineups:
        if pyautogui.locateOnScreen(f'lineups/{f}', grayscale=True, confidence=0.8) != None:
            data = f.strip(".jpg").split("_")
            for i in range(int(data[2])): playsound("sfx/1.wav")
            for i in range(int(data[3])): playsound("sfx/3.wav")
            print("Located"); time.sleep(2)