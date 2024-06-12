import pyautogui
import cv2
import numpy as np
import uuid
import time
import random
def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot = cv2.resize(screenshot, (640, 640))  
    random_1 = random.uniform(1, 29)
    random_filename = f'datasets/create/640/screenshot_{random_1}_{uuid.uuid4()}.png' 
    cv2.imwrite(random_filename, screenshot) 
    return screenshot

for i in range(900):
    time.sleep(3)
    capture_screen()
    print(i)