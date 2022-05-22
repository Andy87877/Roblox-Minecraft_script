# https://www.roblox.com/games/9281034297/8-Goal-Kick-Simulator
import pyautogui
import pydirectinput
import time

Shoot_time = 0.4581
CD_time = 8
Repeat_time = 5

def shoot():
    pydirectinput.keyDown('q')
    time.sleep(Shoot_time)
    pydirectinput.keyUp('q')

def start():
    print("wait")
    time.sleep(3)
    print("shoot")

start()

for i in range(Repeat_time):
    print(i+1)
    shoot()
    time.sleep(CD_time)

