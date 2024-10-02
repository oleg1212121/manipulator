from datetime import datetime
import os


class Logger:

    def __init__(self):
        self.path = os.path.dirname(__file__)
        pass

    def log(self, message):
        with open(f"{self.path}/log.txt", "a") as f:
            f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "----------\n")
            f.write(str(message) + "\n")

