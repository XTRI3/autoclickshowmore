import pyautogui

while True:
    location = pyautogui.locateOnScreen('image.png', confidence=0.7, grayscale=True)
    if location == None:
        pass

    elif location != None:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
