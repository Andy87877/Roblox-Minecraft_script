# https://www.roblox.com/games/9281034297/8-Goal-Kick-Simulator
import pyautogui
import pydirectinput
import time
import keyboard


time.sleep(2)
flag = True

while True:
    if (keyboard.read_key() == "`"):
        if (flag):
            pydirectinput.mouseDown()
            time.sleep(0.1)
            flag = False
            time.sleep(0.1)
        else:
            pydirectinput.mouseUp()
            time.sleep(0.1)
            flag = True
            time.sleep(0.1)
