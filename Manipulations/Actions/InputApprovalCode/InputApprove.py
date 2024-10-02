
from Manipulations.Logger.Logger import Logger
from Manipulations.KeyboardResolver.ApproveKeyboardResolver import ApproveKeyboardResolver

from Manipulations.Actions.InputApprovalCode.MailReader import MailReader


class InputApprove:

    def __init__(self, driver):
        self.logger = Logger()
        self.driver = driver
        self.reader = MailReader()

    def process(self):

        print('reading email ........')
        codes = self.reader.process()

        if len(codes) == 1 and len(codes[0]) == 6:
            number = codes[0]

            print('click approve input')
            self.driver.connect()
            self.driver.sleep(1)
            self.driver.click('input#mat-input-5')

            print('resolver')
            resolver = ApproveKeyboardResolver(self.driver)
            self.driver.sleep(1)
            print(self.driver.driver.get_page_source())
            print('==================================================')
            for c in number:
                resolver.resolve(c)

            self.driver.disconnect()

        else:
            self.driver.disconnect()
            raise Exception('Email Reader gets unanticipated result')