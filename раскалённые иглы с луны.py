import pyautogui
import time
pyautogui.doubleClick(30,450)
time.sleep(1.5)
pyautogui.click(1000,520)
pyautogui.write("gjujlf d fynfhrnblt")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(500,570)
time.sleep(2)
pyautogui.click(300,570)
z = float(input("темпервтура"))
time.sleep(1)
pyautogui.tripleClick(200,580)
pyautogui.hotkey("ctrl","c")
pyautogui.click(790,1100)
pyautogui.click(830,1000)
pyautogui.click(700,600)
sleep(0.4)
pyautogui.click(700,600)
pyautogui.hotkey("ctrl","v")
if z >= 0:
    print("ОСТОРОЖНО,ЛЕДНИКИ ТАЮТ")
if z >= -1:
    print("температура в норме")
