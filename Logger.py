from datetime import datetime


class Logger:

    def __init__(self):
        pass

    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "----------\n")
            f.write(str(message) + "\n")

