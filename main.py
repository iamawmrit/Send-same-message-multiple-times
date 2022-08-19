#Code was done By Awmrit
import pyautogui as pt
import time

#ask for message limit
limit =input("Message limit: ")

#what message wants to send
message=input("Enter Message: ")
i =0
time.sleep(5)

# using while loop 
while i<int(limit):
          pt.typewrite(message)
          pt.press("enter")

          i+=1