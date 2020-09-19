# Screenshot Tool
Running this script will take a screenshot of your desktop at a default rate of 30 seconds and repeat until the user exits the application. It's primarily designed for game journalists who cannot easily take a screenshot of a game at just the right moment in time.

![Screenshot](https://imgur.com/YIf2IeG.png)

## Requirements
Besides needing Python, obviously, Python dependencies are as follows:
* `pyautogui`
* `colorama`

Installing said dependencies, regardless of operating system, is as simple as:

`pip install pyautogui colorama`

As far as system dependencies are concerned, on Linux, `pyautogui` relies on `scrot`. On Debian/Ubuntu-based distros, this can be installed with:

`sudo apt install scrot`

As `pyautogui` uses the `screencapture` command on OS X, there's no additional system dependencies needed here. And Windows...well I don't know about that one.

## Usage
After cloning the repository (`git clone https://github.com/cow-killer/screenshot-tool.git`), simply navigate to the `screenshot-tool.py` file in the terminal and run:

`python screenshot-tool.py`

A few arguments can be passed to change the timer and the file format. The first argument is the number of seconds to wait before taking the next screenshot. The second defines the file format. So, for example, if you wanted a screenshot to be taken every 20 seconds and wanted them to be saved in `JPG` format, you would run:

`python screenshot-tool.py 20 JPG`

Press `CTRL+C` at any time to quit. Screenshots will be saved in the `screenshots/` folder.

## To-do
Not listed in any particular priority, and may or may not get worked on in the future:
* Add a simple GUI. However, as it's often faster and cleaner on system resources to use the program on the command line, I will probably keep it the way it is
* Add a few additional arguments to specify folder name, picture quality, screenshot dimensions, etc.
