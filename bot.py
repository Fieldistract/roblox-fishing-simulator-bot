# Import necessary libraries for automation, time management, and system interaction
from pydoc import cli  # Importing command-line interface utilities
from pyautogui import *  # Importing PyAutoGUI for automation of GUI interactions
import pyautogui  # Import PyAutoGUI for pixel color detection and mouse operations
import time  # Import time for adding delays
import keyboard  # Import keyboard for monitoring key presses
import random  # Import random for generating random values
import win32api, win32con  # Import win32api and win32con for low-level system control
import pydirectinput  # Import pydirectinput for safer and smoother input simulation
import math
import cv2

from utils.imitate import (
    reEquipRod,
    toggleInventory,
    leftClick,
    random_click,
    random_double_click,
    update_global_variables,
)
from utils.BubbleDetector import BubbleDetector
from utils.Presetter import Presetter

fishingGaugeColor = (255, 255, 255)  # WHITE
fishingMeterColor = (83, 250, 83)  # GREEN
bagFullTextColor = (253, 0, 97)  # RED
bubbleColor = (68, 252, 234)  # Define the RGB color code for air bubbles

monitorFishingPixel = 965, 785
throw_line_coords = (960, 390)  # Coords of where the player throws fishing line.
bagFullTextCords = (878, 697)

sellButtonCords = (1078, 323)
sellEverthingCords = (1210, 447)

sellGamepass = True  # CHANGE TO FALSE IF NO SELL GAMEPASS

        # After setting the values, you can directly use the global variables as updated.
def initFetchCords():
    bubble_detector = BubbleDetector()
    time_out_time = 15


    print("Recording initial coords. Please do not touch anything...")
    time.sleep(0.5)
    # Perform a double random throw to reset the fishing rod
    random_double_click(throw_line_coords)
    # toggleInventory()
    while(time_out_time != 0):
        if bubble_detector.check_air_bubbles_on_screen() == True:
            print("Detected Bubbles. Scanning screen for fishingbar.")
            random_click(throw_line_coords)
            # Find the UI element
            toggleInventory()
            button_location = pyautogui.locateOnScreen(
                "scan_assets/sell-button.png", confidence=0.8
            )
            if button_location:
                print(f"Button found at: {button_location}")
                # Move to the button and click it
            else:
                print("Button not found.")
        time_out_time-=1


# Function to retrieve a counter value for controlling loop iterations
def get_counter():
    counter = 21  # Set the counter to a predefined value
    return counter  # Return the counter value


def check_full_inv():
    if pyautogui.pixel(*bagFullTextCords) == bagFullTextColor:
        return True
    return False


def sell_inventory():
    toggleInventory()
    win32api.SetCursorPos(sellButtonCords)
    time.sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    leftClick()
    time.sleep(0.10)
    win32api.SetCursorPos(sellEverthingCords)
    time.sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    leftClick()
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -40, 0, 0, 0)  # FIX THIS
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    time.sleep(1)
    leftClick()
    time.sleep(1)
    toggleInventory()
    time.sleep(0.4)
    random_click(throw_line_coords)


def fishingBarCheck():
    # Number of pixels to check horizontally around monitorFishingPixel
    pixel_range = 3

    for offset in range(0, pixel_range + 1):  # Iterate from -5 to 5
        # Adjust x-coordinate of the pixel being checked
        x, y = monitorFishingPixel
        current_pixel = (x + offset, y)

        try:
            # Check if the pixel matches either color
            if (
                pyautogui.pixel(*current_pixel) == fishingMeterColor
                or pyautogui.pixel(*current_pixel) == fishingGaugeColor
            ):
                return True  # A match is found
        except Exception as e:
            print(f"Error checking pixel at {current_pixel}: {e}")

    return False  # No match found


def main():
    # Initialize counters and flags
    bubble_detector = BubbleDetector()
    manager = Presetter()
    preset_config = manager.checker_files()
    
    global monitorFishingPixel, throw_line_coords, bagFullTextCords
    global sellButtonCords, sellEverthingCords
    
    monitorFishingPixel = preset_config.get('monitorFishingPixel', monitorFishingPixel)
    throw_line_coords = preset_config.get('throw_line_coords', throw_line_coords)
    bagFullTextCords = preset_config.get('bagFullTextCords', bagFullTextCords)
    sellButtonCords = preset_config.get('sellButtonCords', sellButtonCords)
    sellEverthingCords = preset_config.get('sellEverthingCords', sellEverthingCords)
    counter = 0  # General counter for loop control
    fish_counter = 0  # Counter to track the number of fish caught
    fish_found = False  # Flag to indicate if a fish is currently detected
    userbubble = int(input("1. Normal Bubbles 2. Lava/red Bubbles 3. Void Bubbles"))

    # Main loop that continues until the 'q' key is pressed
    while keyboard.is_pressed("q") == False:
        # # Check if a fish is detected at specific screen coordinates
        # if pyautogui.pixel(847, 820)[0] == 255 or pyautogui.pixel(860, 800)[0] == 255:
        #     click_random_throw()  # Perform a random click to reel in the fish
        #     counter = get_counter()  # Reset the counter

        # Increment fish counter if a fish was detected
        # TODO: ADD COUNTER to keep track of time spent fishing. Otherwise you get stuck. INCASE SOMETHING WHITE (255,255,255) comes across screen.
        if fish_found == True:
            print("Fish hooked! Reeling...")
            # while pyautogui.pixel(*monitorFishingPixel) == fishingMeterColor or pyautogui.pixel(*monitorFishingPixel) == fishingGaugeColor:
            while fishingBarCheck() == True:

                if pyautogui.pixel(*monitorFishingPixel) == fishingGaugeColor:
                    print("Reeling Threshold hit! Pulling HARDER!!")
                    random_double_click(throw_line_coords)
                time.sleep(0.005)

            # Check if the pixel color at specific coordinates does not match the fishingbar colors
            if (
                pyautogui.pixel(*monitorFishingPixel) != fishingMeterColor
                or pyautogui.pixel(*monitorFishingPixel) != fishingGaugeColor
            ):
                fish_counter += 1  # Increment the fish counter
                print(
                    "Fish caught: " + str(fish_counter)
                )  # Log the number of fish caught
                fish_found = False  # Reset the fish detection flag
                print("RECASTING...")
                time.sleep(0.40)
                random_click(
                    throw_line_coords
                )  # Perform a double random throw to reset the fishing rod

        # If no fish is detected, check for air bubbles on the screen
        if fish_found == False:
            if bubble_detector.check_air_bubbles_on_screen() == True:
                print("Detected Bubbles. Attempting to reel.")
                random_click(
                    throw_line_coords
                )  # Perform a random click to reel in the fish
                random_click(
                    throw_line_coords
                )  # Perform a random click to reel in the fish
                counter = get_counter()  # Reset the counter
                fish_found = True  # Set the flag indicating a fish is found

        # If the counter reaches zero, perform a throw or reel-in action
        print("Waiting for Bubbles. Recasting in: ", counter)
        if counter == 0:
            reEquipRod()
            time.sleep(2)
            random_click(throw_line_coords)
            counter = get_counter()  # Reset the counter

        # If the inventory is full, sell fish
        if check_full_inv() == True:
            if sellGamepass:
                print("Inventory full, selling...")  # Log the inventory status
                sell_inventory()
            else:
                print("Inventory full. Sell Gamepass is set to False.")
                print("Quitting Program.")
                exit()

        counter -= 1  # Decrement the counter on each loop iteration
        time.sleep(0.025)  # Add a small delay to reduce CPU usage


if __name__ == "__main__":
    # initFetchCords()
    main()
