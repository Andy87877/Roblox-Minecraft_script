import os
import pyautogui
import pydirectinput
import time
import keyboard


time.sleep(2)
flag = True

while True:
    if (keyboard.read_key() == "."):
        if (flag):
            pydirectinput.mouseDown()
            pydirectinput.mouseDown(button='right')
            print("On")
            # pyautogui.keyDown("w")
            time.sleep(0.1)
            flag = False
            time.sleep(0.1)
        else:
            pydirectinput.mouseUp()
            pydirectinput.mouseUp(button='right')
            print("Off")
            # pyautogui.keyUp("w")
            time.sleep(0.1)
            flag = True
            time.sleep(0.1)
    if (keyboard.read_key() == "]"):
        os._exit()