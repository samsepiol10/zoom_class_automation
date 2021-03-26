'''programmed by suryadev singh'''
import time
from datetime import datetime
import pyautogui
import webbrowser
schedule=[
    #enter your zoom class link and starttime and endtime(sepereted by ":")  in list
    ["https://zoom.us/j/9972367366","14:42","14:43"],
    ["https://zoom.us/j/9972367366","14:44","16:00"]]
k=1
classStarted = False
print()
print("your python bot will attend your class , dont worry !!")
print("you just chill and focus on your sleep") 
print()
print("               ___")
print("              |. .|","I AM NOT NOT ROBOT")
for i in schedule:
    print()
    print()
    print(f"---------------------class-{k}--------------------")
    while True:
        if classStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                print(f"[+] class {k} started and running....")
                classStarted = True
                time.sleep(25)
                pyautogui.keyDown("alt")
                pyautogui.keyDown("tab")
                pyautogui.keyUp("alt")
                pyautogui.keyUp("tab")
                time.sleep(3)
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("w")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("w")
                k+=1
        elif classStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                pyautogui.keyDown("x")
                print("your class is attend sucessfully by your bot !!")
                #for linux uncomment the following block:
                #---------------------
                #pyautogui.keyDown("alt")
                #pyautogui.press("q")
                #pyautogui.keyUp("alt")
                # time.sleep(1)
                # pyautogui.keyDown("enter")
                # pyautogui.keyUp("enter")
                #----------------------
                classStarted = False
                break
