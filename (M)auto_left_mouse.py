import pyautogui
import pydirectinput
import time
import keyboard


time.sleep(2)
flag = True

while True:
    if (keyboard.read_key() == "`"):
        if (flag):
            #pydirectinput.mouseDown()
            pyautogui.keyDown("space")
            time.sleep(0.1)
            flag = False
            time.sleep(0.1)
        else:
            #pydirectinput.mouseUp()
            pyautogui.keyUp("space")
            time.sleep(0.1)
            flag = True
            time.sleep(0.1)
