
from Settings.settings import *
from Manipulations.ProcessConfirmation.ProcessConfirmation import ProcessConfirmation
from Manipulations.Simulations.ShakeAndClick import ShakeAndClick
from Manipulations.Assertions.CheckIfLoginPageReady import CheckIfLoginPageReady
from Manipulations.Assertions.CheckIfCookiesButtonReady import CheckIfCookiesButtonReady
from Manipulations.Assertions.CheckIfCloudflareReady import CheckIfCloudflareReady
from Manipulations.Actions.OpenLoginPage.OpenLoginPage import OpenLoginPage
from Manipulations.Actions.OpenBrowser.ClickCookiesButton import ClickCookiesButton
from Manipulations.Actions.ConfirmLoginCredentials.ClickSubmitButton import ClickSubmitButton
from Manipulations.Actions.InputApprovalCode.InputApprovalCode import InputApprovalCode
from Manipulations.Actions.ConfirmApprovalForm.ConfirmApprovalForm import ConfirmApprovalForm
from Manipulations.Actions.ConfirmApprovalForm.ClickApprovalSubmit import ClickApprovalSubmit
from Manipulations.Actions.Login.LoginProcess import LoginProcess
from Manipulations.Actions.Login.InputLogin import InputLogin

from Manipulations.Simulations.TimeFiller import TimeFiller

from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists


class Manipulator:

    def __init__(self, driver):
        self.driver = driver
        self.confirmation = ProcessConfirmation()
        self.code = "open_browser"
        self.shake = ShakeAndClick()
        self.openLoginPage = OpenLoginPage()
        self.checkIfLoginPageReady = CheckIfLoginPageReady()
        self.checkIfCookiesButtonReady = CheckIfCookiesButtonReady()
        self.clickCookiesButton = ClickCookiesButton()
        self.checkIfCloudflareReady = CheckIfCloudflareReady()
        self.clickSubmitButton = ClickSubmitButton()
        self.approval = InputApprovalCode()
        self.confirmApprovalForm = ConfirmApprovalForm()
        self.clickApprovalSubmit = ClickApprovalSubmit()

        self.loginProcess = LoginProcess()
        # self.login = InputLogin(driver)

        # self.filler = TimeFiller()

        self.tokens = set()
        self.checkIfExists = CheckIfImageExists()

    def run(self):
        # self.code = self.confirmation.process()
        while True:
            if self.code in ['open_browser']:
                try:
                    # Open vfs pre-login page
                    self.driver.driver.uc_open_with_disconnect(paths['vfs_url'])

                    # shake and click
                    self.shake.process(3)

                    # Assert cookies button
                    self.checkIfCookiesButtonReady.process()

                    # Click cookies button
                    self.clickCookiesButton.process()

                    # Wait
                    self.driver.driver.sleep(1)

                    # Next step
                    self.code = "open_login_page"

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['open_login_page']:
                try:
                    # Open login page
                    self.openLoginPage.process()
                    self.driver.driver.sleep(1)

                    # shake and click
                    self.shake.process()

                    # Checking for page rendering
                    self.checkIfLoginPageReady.process()

                    # Next step
                    self.code = "login"

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['login']:
                try:
                    # shake and click
                    self.shake.process(2)

                    # Start login process
                    self.loginProcess.process()

                    # Next step
                    self.code = 'confirm_login_credentials'

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['confirm_login_credentials']:
                try:
                    # Checking for cloudflare passed OK
                    self.checkIfCloudflareReady.process()

                    # Click submit and check if passed
                    if self.clickSubmitButton.process():
                        self.code = 'input_approval_code'
                    else:
                        # self.code = 'input_approval_code'
                        raise Exception('Approval page has not been loaded')

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['input_approval_code']:
                try:
                    print('INPUT APPROVAL CODE')
                    # shake and click
                    self.shake.process(5)

                    # Input approval code
                    self.approval.process()

                    self.code = 'confirm_approval_form'

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['confirm_approval_form']:
                try:
                    print('CONFIRM_APPROVAL')
                    # Checking for cloudflare passed OK
                    self.confirmApprovalForm.process()

                    # Add listener to requests
                    def cdp_response_print(request):
                        if 'params' in request:
                            if ('headers' in request['params']) and ('authorize' in request['params']['headers']):
                                self.tokens.add(request['params']['headers']['authorize'])

                            elif ('request' in request['params']) and ('headers' in request['params']['request']) and (
                                    'authorize' in request['params']['request']['headers']):
                                self.tokens.add(request['params']['request']['headers']['authorize'])

                    self.driver.driver.add_cdp_listener(
                        "*", cdp_response_print
                    )

                    # Checking for cloudflare passed OK (again)
                    self.confirmApprovalForm.process()

                    # Connect driver for reading requests
                    self.driver.driver.connect()

                    # Click submit
                    self.clickApprovalSubmit.process()

                    # Next step
                    self.code = 'check_slots'

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['check_slots']:
                try:
                    # self.filler.shake(animation['short_sleep'])
                    # print('CHECK SLOTS')
                    #
                    # # Disconnect driver
                    # self.driver.driver.disconnect()
                    #
                    # # Check Authorize tokens
                    if len(self.tokens) == 1:
                        token = self.tokens.pop()

                        print(f"Slots check request")
                        print(token)
                        # c = CheckSlots()
                        # c.process(token, Credentials['email'])

                    else:
                        self.code = self.confirmation.process(title=f"Wrong authorize token!!")
                    self.code = 'pause'

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ['pause']:
                try:
                    self.driver.sleep(30)
                    self.code = self.confirmation.process()

                except Exception as e:
                    self.code = self.confirmation.process(title=f"{e} ({self.code})")

            if self.code in ["close"]:
                break
