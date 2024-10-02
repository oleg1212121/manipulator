import pyautogui
import time
from Settings.settings import elements
from Manipulations.Logger.Logger import Logger
from Manipulations.Actions.InputApprovalCode.MailReader import MailReader


class InputApprovalCode:

    def __init__(self):
        self.allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.logger = Logger()

    def process(self):
        self.logger.log('Approval login started')
        # number = pyautogui.prompt(text='Code', title='Type the code!')

        # Approval input click
        pyautogui.moveTo(*elements['coordinates']['approval_input'], elements['animation']['middle_duration'], elements['animation']['animation'])
        pyautogui.click()
        time.sleep(elements['animation']['middle_duration'])

        print('reading email ........')
        reader = MailReader()
        codes = reader.process()
        if len(codes) == 1:
            number = codes[0]
            if len(number) == 6:
                for symbol in number:
                    if symbol not in self.allowed:
                        raise Exception('WRONG CODE')
                    pyautogui.moveTo(*elements['approval_keyboard'][symbol], elements['animation']['pre_middle_duration'])
                    pyautogui.click()
            else:
                raise Exception('WRONG CODE')

            # # checkbox click
            # time.sleep(animation['middle_duration'])
            # pyautogui.moveTo(*Elements['approval_checkbox'], animation['middle_duration'], animation['animation'])
            # pyautogui.click()

            # time.sleep(animation['middle_duration'])
            # # input password during login
            # pyautogui.moveTo(*Elements['approval_submit'], animation['middle_duration'], animation['animation'])
            # pyautogui.click()
            # print('approval done')

        else:
            raise Exception('Email Reader gets unanticipated result')
