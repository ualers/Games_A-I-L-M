import pyautogui
import cv2
import numpy as np
import uuid
import time

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot = cv2.resize(screenshot, (1920, 1080))  
    random_filename = f'datasets/naruto_data_3/screenshot_{uuid.uuid4()}.png' 
    cv2.imwrite(random_filename, screenshot) 
    return screenshot

for i in range(250):
    time.sleep(10)
    capture_screen()