a = 100
import pyautogui
import keyboard
key = 'a'
ke = "s"
while True:
    if keyboard.is_pressed(key):
        a = 0
while True:
    if keyboard.is_pressed(ke):
        a = 100
        pyautogui.moveTo(1200,600)
        while a != 100:
            pyautogui.click()
