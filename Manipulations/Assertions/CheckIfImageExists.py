import pyautogui


class CheckIfImageExists:

    def __init__(self):
        pass

    def check(self, image, min_search_time= 5, grayscale=True, confidence=0.9):
        print(f"Looking for: {image} ...")
        try:
            coordinates = pyautogui.locateOnScreen(f"Images\\{image}", minSearchTime=min_search_time, grayscale=grayscale, confidence=confidence)
            return coordinates
        except:
            print(f"Image {image} was not found")
            return None
