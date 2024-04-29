import pyautogui
import pyperclip
import time
import winsound
from Settings.Options import coordinates, animation, settings
from Logger import Logger

class MailReader:

    def __init__(self):
        self.logger = Logger()

    def process(self):

        self.logger.log('Mail reader started')
        # open browser
        pyautogui.click(coordinates["browser"])
        time.sleep(animation['slow_duration'])

        # resize browser
        pyautogui.hotkey('win', 'up')
        time.sleep(animation['slow_duration'])

        # open mailbox
        pyautogui.moveTo(*coordinates["mailbox"], animation["slow_duration"])
        pyautogui.click()
        time.sleep(animation['slow_duration'])
        # check if no robot icon there
        try:
            pyautogui.locateOnScreen(settings['email_not_robot'], 5, confidence=0.9, grayscale=True)
            winsound.Beep(200, 1000)
            time.sleep(0.2)
            winsound.Beep(200, 1000)
            time.sleep(0.2)
            winsound.Beep(200, 1000)
            pyautogui.alert(text='MAILBOX ASKS FOR NO ROBOT APPROVAL', title='YOU HAVE 30 SEC', button='OK')
            time.sleep(30)
        except:
            print('no robot check in email')


        # open recent email
        pyautogui.moveTo(*coordinates["email"], animation["slow_duration"])
        pyautogui.click()

        # move to start position for copying
        pyautogui.moveTo(*coordinates["start_copy"], animation["slow_duration"])
        pyautogui.mouseDown()

        # emphasize
        pyautogui.moveTo(*coordinates["end_copy"], animation["fast_duration"])
        pyautogui.mouseUp()

        # copy
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(animation['fast_duration'])

        # validate text
        code = pyperclip.paste()
        numbers = []
        for char in code:
            if char.isdigit():
                numbers.append(str(char))
        # code = str("".join(numbers))
        print(numbers)

        # close browser
        time.sleep(animation['fast_duration'])
        pyautogui.hotkey("alt", "f4")
        time.sleep(animation['fast_duration'])
        return numbers

