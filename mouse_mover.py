"""
Handles the automation via mouse seeding option.
"""
from time import sleep
import pyautogui
from const import GPX, GPY

def get_screen_measurements() -> list:
    """
    Gets screen measurement dimensions.
    """
    size =  pyautogui.size()
    centre = [int(i/2) for i in size]
    centre_x = centre[0]
    centre_y = centre[1]
    return [centre_x, centre_y]


# Relative movements

def make_movements(server_name: str) -> None:
    """
    Makes movements on seed game UI.
    """
    centres = get_screen_measurements()
    centre_x = centres[0]
    centre_y = centres[1]
    # Actual pixel size
    steps = [
        ("move",-0.1*GPX, -0.9*GPY),
        ("click",1),
        ("move",-0.1*GPX, -0.75*GPY),
        ("click",1),
        ("write", server_name),
        ("move", -0.1*GPX, -0.60*GPY),
        ("enter"),
        ("click",2)
        ]
    pyautogui.moveTo(centre_x, centre_y)
    for step in steps:
        if  "click" in step:
            if 2 in step:
                pyautogui.doubleClick()
            elif 1 in step:
                pyautogui.leftClick()
        elif "write" in step:
            pyautogui.typewrite(step[1])
        elif "move" in step:
            pyautogui.moveTo(centre_x+step[1],centre_y+step[2])
        elif "enter" in step:
            pyautogui.keyDown("Enter")
            sleep(5)
        sleep(1)
        