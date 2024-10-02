class ApproveKeyboardResolver:

    dict = {
        '0': False,
        '1': False,
        '2': False,
        '3': False,
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False
    }

    button = 'span.mat-button-wrapper'
    shift = 'keyboard_arrow_up'

    def __init__(self, driver):
        print('Resolver ready')
        self.driver = driver

    def resolve(self, symbol):
        print(f"resolve - {symbol}")

        symbol = str(symbol)
        cur = self.dict[symbol]

        if cur:
            self.driver.click(f"{self.button}:contains(\"{self.shift}\")")

        self.driver.sleep(0.5)
        self.driver.click(f"{self.button}:contains(\"{symbol}\")")

