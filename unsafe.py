from pyautogui import *; import pyautogui; import time; from os import walk; from playsound import playsound; pyautogui.FAILSAFE = False
while 1:
    for f in next(walk("lineups"), (None, None, []))[2]:
        if pyautogui.locateOnScreen(f'lineups/{f}', grayscale=True, confidence=0.8) != None:
            for i in range(int(f.strip(".jpg").split("_")[2])): playsound("sfx/1.wav");
            for i in range(int(f.strip(".jpg").split("_")[3])): playsound("sfx/3.wav")
            print("Located"); time.sleep(2)
        # pyautogui.mouseDown(button="left")
        # time.sleep(0.667)
        # pyautogui.mouseUp(button="left")