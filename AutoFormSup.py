import pyautogui
from pyautogui import *

while True:
    x, y = pyautogui.position()
    print('X: {} Y: {}'.format(x, y))
    sleep(1)