import win32api, win32con
import time, keyboard, random


def reEquipRod():
    time.sleep(0.1)
    keyboard.press("1")
    keyboard.release("1")
    time.sleep(0.1)
    keyboard.press("1")
    keyboard.release("1")


def toggleInventory():
    time.sleep(0.20)
    keyboard.press("f")
    keyboard.release("f")
    time.sleep(0.20)


def leftClick():
    time.sleep(random.uniform(0.001, 0.005))  # Pause for a short, randomized duration
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # Simulate mouse press
    time.sleep(random.uniform(0.001, 0.005))  # Pause for a short, randomized duration
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # Simulate mouse release


# Function to simulate a mouse click at random coordinates within a defined range
def random_click(clickCoords, offset=10):
    # Generate random coordinates near target
    x = random.randint(clickCoords[0], clickCoords[0] + offset)
    y = random.randint(clickCoords[1], clickCoords[1] + offset)
    win32api.SetCursorPos((x, y))  # Move the cursor to the random coordinates
    leftClick()  # <--- pyautogui has an existing leftClick() function. Maybe use that instead of create our own?


# Function to simulate a double mouse click at random coordinates within a defined range
def random_double_click(clickCoords):
    random_click(clickCoords)  # Perform the first random click
    time.sleep(random.uniform(0.02, 0.025))  # Add a short delay
    random_click(clickCoords)  # Perform the second random click

def update_global_variables(preset):
        global monitorFishingPixel, throw_line_coords, bagFullTextCords
        global sellButtonCords, sellEverthingCords

        # Assuming 'preset' is a dictionary with keys like 'monitorFishingPixel', 'throw_line_coords', etc.
        monitorFishingPixel = preset.get('monitorFishingPixel', monitorFishingPixel)
        throw_line_coords = preset.get('throw_line_coords', throw_line_coords)
        bagFullTextCords = preset.get('bagFullTextCords', bagFullTextCords)
        sellButtonCords = preset.get('sellButtonCords', sellButtonCords)
        sellEverthingCords = preset.get('sellEverthingCords', sellEverthingCords)

        # After setting the values, you can directly use the global variables as updated.

