# import time
# from Manipulations.Login.Login import Login
# from Settings.Options import *
# from Manipulations.Login.MailReader import MailReader
# from Manipulations.Login.ApprovalLogin import ApprovalLogin
from Manipulations.Logger.Logger import Logger
from Manipulations.KeyboardResolver.LoginKeyboardResolver import LoginKeyboardResolver
from Settings.settings import credentials


class InputLogin:

    def __init__(self, driver):
        self.logger = Logger()
        self.driver = driver

    def process(self):
        print('Input login Credentials')
        email = credentials['gmail']['email']
        password = credentials['gmail']['password']

        self.driver.connect()

        print('write email')
        self.driver.add_text('input#email', text=email)
        self.driver.sleep(1)
        self.driver.click('input#password')
        print('resolver')
        resolver = LoginKeyboardResolver(self.driver)
        self.driver.sleep(1)

        for c in password:
            resolver.resolve(c)

        self.driver.disconnect()