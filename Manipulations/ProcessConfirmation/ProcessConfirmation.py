from Settings.Elements.settings import *
from Manipulations.Logger.Logger import Logger


class ProcessConfirmation:

    actions = {
        'open_browser': {
            "name": "OPEN_BROWSER",
            "description": "Open browser",
            "show": False,
        },
        'open_login_page': {
            "name": "OPEN_LOGIN",
            "description": "Open login page",
            "show": False,
        },
        'login': {
            "name": "LOGIN",
            "description": "Input login Credentials process",
            "show": True,
        },
        'confirm_login_credentials': {
            "name": "CONFIRM_LOGIN",
            "description": "Confirm login process",
            "show": True,
        },
        'input_approval_code': {
            "name": "INPUT_APPROVAL_CODE",
            "description": "Input approval code from email",
            "show": True,
        },
        'confirm_approval_form': {
            "name": "CONFIRM_APPROVAL_FORM",
            "description": "Confirm approval form",
            "show": True,
        },
        'check_slots': {
            "name": "CHECK_SLOTS",
            "description": "Check slots",
            "show": True,
        },
        "pause": {
            "name": "PAUSE",
            "description": "30 sec pause",
            "show": True,
        },
        "close": {
            "name": "CLOSE",
            "description": "Close application",
            "show": True,
        }
    }

    def __init__(self):
        self.logger = Logger()
        self.title = 'WHAT NEXT?'
        self.text = "\n".join([f"{v['name']} - {v['description']}" for _, v in self.actions.items() if v["show"]])

    def process(self, title=None, text=None):
        code = pyautogui.confirm(
            text=text or self.text,
            title=title or self.title,
            buttons=[_ for _, v in self.actions.items() if v["show"]]
        )
        return code





