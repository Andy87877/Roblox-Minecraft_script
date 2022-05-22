# https://www.roblox.com/games/9281034297/8-Goal-Kick-Simulator
import pyautogui
import pydirectinput
import time
import keyboard


Shoot_time = 0.4581
CD_time = 8
Repeat = 99999
Break_keyboard = "z"

def Shoot():
    pydirectinput.keyDown('q')
    print("Shoot!!!!")
    time.sleep(Shoot_time)
    pydirectinput.keyUp('q')

def Start():
    print("wait")
    time.sleep(3)

Start()
for i in range(Repeat):
    Shoot()
    print(i,end= " ")
    time.sleep(CD_time)

