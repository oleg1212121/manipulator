from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists
import time
class CheckIfLoginPageReady:

    def __init__(self):
        self.check = CheckIfImageExists()

    def process(self):
        v = None
        for i in range(0, 10):
            try:
                print(f"try - {i}")
                v = self.check.check("login_enter_title.PNG")
                if v:
                    print('FOUNDED')
                    break
            except:
                time.sleep(5)
                continue
        if not v:
            raise Exception("login page doesn't appear")