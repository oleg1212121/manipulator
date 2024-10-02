import time
from Manipulations.Logger.Logger import Logger
from Manipulations.MailboxReader.GmailReader import GmailReader


class MailReader:

    def __init__(self):
        self.logger = Logger()

    def process(self):

        self.logger.log('Mail Reader started')
        reader = GmailReader()
        time.sleep(5)
        codes = []
        for _ in range(0, 10):
            print(f"try - {_}")
            codes = reader.process()

            if len(codes) == 1:
                break
            else:
                time.sleep(5)

        return codes

