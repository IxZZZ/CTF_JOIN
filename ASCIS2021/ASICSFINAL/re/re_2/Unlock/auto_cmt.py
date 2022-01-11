import pyautogui
import time

# comments = ["Hi", "Just commenting for fun", "Checking my python comment bot", "Just for fun",
#             "I am just checking my python skill", "python is awesome", "I am a messy programmer"]
comments = open('text.txt','r').read().split(' ')
print(len(comments))
time.sleep(1)

for i in range(500):
    pyautogui.typewrite(comments[i])
    pyautogui.typewrite("\n")
    time.sleep(0.5)
