"""
Screenshot tool by Mark Dougherty (cow_killer)

Python dependencies:
-pyautogui for screenshots
-colorama for text colors

System dependencies:
-scrot
"""

import pyautogui
import datetime
import time
import sys
import os
from pathlib import Path
from colorama import init, Fore, Back, Style
init() # fire up colorama

version = "1.0"
screenshots_taken = 0 # keep track of the number of screengrabs we've taken
screenshot_folder = "screenshots"
screenshot_folder_path = Path(screenshot_folder)

def clear():
    if os.name == "nt": # Windows
        _ = os.system("cls")
    else: # Mac OS/Linux (posix)
        _ = os.system("clear")

clear() # clear the terminal, just for cleaner output
print(Style.BRIGHT + "Screenshot Tool")
print("Version " + str(version), Style.RESET_ALL + "\n")
print("Press " + Style.BRIGHT + 'CTRL+C' + Style.RESET_ALL + " at any time to quit\n")

try:
    sleep_timer = int(float(sys.argv[1])) # if the user passes a float, convert it to an integer
except IndexError: # set timer to 30 seconds if no argument is passed
    print("No timer passed, setting interval of " + Style.BRIGHT + "30 seconds" + Style.RESET_ALL)
    sleep_timer = 30
    pass
except ValueError: # Exit if user passes a string
    print("Cannot accept a string. Exiting...")
    sys.exit()
    
try:
    file_extension = "." + (sys.argv[2])
except IndexError:
    print("No file extension specified, setting it to " + Style.BRIGHT + "PNG\n" + Style.RESET_ALL)
    file_extension = ".png"
    pass
except ValueError: # having a bit of trouble trying to capture the error on this one, it still prints a ValueError from Image.py
    print("Cannot accept an integer. Exiting...")
    sys.exit()

# check if "screenshots" folder exists. If not, make one
if screenshot_folder_path.is_dir():
    pass
else:
    print("'" + screenshot_folder + "' folder does not exist, creating it now\n")
    os.mkdir(screenshot_folder)
while True: # enter a continuous loop until CTRL+C is pressed
    try:
        time_stamp = datetime.datetime.now() # get system time
        screenshot_name = time_stamp.strftime("%m-%d-%Y_%H:%M:%S" + file_extension) # format the filename as MM/DD/YYYY along with the time
        for remaining in range(sleep_timer, 0, -1): # block of code that refreshes the number of seconds displayed
            sys.stdout.write("\r")
            sys.stdout.write("Taking screenshot in {:2d} second(s)".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        screenshot = pyautogui.screenshot() # take the screenie!
        screenshot.save("screenshots/" + screenshot_name) # save the file in the "screenshots" folder
        screenshots_taken += 1

        print("\nImage saved as " + screenshot_name + "\n")
    except KeyboardInterrupt:
        if screenshots_taken == 0:
            print(Style.BRIGHT)
            print("\nNo screenshots have been saved.")
            break
        else:
            print(Style.BRIGHT)
            print("\nSaved " + str(screenshots_taken) + " screenshot(s) in '" + screenshot_folder + "/'")
            break
