import os
import pyautogui
import pydirectinput
import time
import keyboard


time.sleep(2)
print("Dig Off")
print("Jump Off")
DIG = False
JUMP = False


while True:
    if (keyboard.read_key() == "."):
        if (DIG):
            pydirectinput.mouseDown()
            pydirectinput.mouseDown(button='right')
            print("Dig On")
            # pyautogui.keyDown("w")
            time.sleep(0.1)
            DIG = False
            time.sleep(0.1)
        else:
            pydirectinput.mouseUp()
            pydirectinput.mouseUp(button='right')
            print("Dig Off")
            # pyautogui.keyUp("w")
            time.sleep(0.1)
            DIG = True
            time.sleep(0.1)
    
    if (keyboard.read_key() == ","):
        if (JUMP):
            pyautogui.keyDown("space")
            print("Jump On")
            time.sleep(0.1)
            JUMP = False
            time.sleep(0.1)
        else:
            pyautogui.keyUp("space")
            print("Jump Off")
            time.sleep(0.1)
            JUMP = True
            time.sleep(0.1)
    if (keyboard.read_key() == "]"):
        os._exit()