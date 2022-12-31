#Code was done By Awmrit
import pyautogui as pt
import time

#asking users for message limit
limit =input("Please Enter Message limit: ")

#what message user wants to send
message=input("Pleaes Enter Message: ")
i =0
time.sleep(6)

# using while loop 
while i<int(limit):
          pt.typewrite(message)
          pt.press("enter")

          i+=1
