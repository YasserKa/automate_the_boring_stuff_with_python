# nudge the mouse every 10 seconds
import pyautogui
import time

while True:
    pyautogui.moveRel(1, 0)
    time.sleep(10)
