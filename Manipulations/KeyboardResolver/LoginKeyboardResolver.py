class LoginKeyboardResolver:

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
        '9': False,
        'a': False,
        'b': False,
        'c': False,
        'd': False,
        'e': False,
        'f': False,
        'g': False,
        'h': False,
        'i': False,
        'j': False,
        'k': False,
        'l': False,
        'm': False,
        'n': False,
        'o': False,
        'p': False,
        'q': False,
        'r': False,
        's': False,
        't': False,
        'u': False,
        'v': False,
        'w': False,
        'x': False,
        'y': False,
        'z': False,
        'A': True,
        'B': True,
        'C': True,
        'D': True,
        'E': True,
        'F': True,
        'G': True,
        'H': True,
        'I': True,
        'J': True,
        'K': True,
        'L': True,
        'M': True,
        'N': True,
        'O': True,
        'P': True,
        'Q': True,
        'R': True,
        'S': True,
        'T': True,
        'U': True,
        'V': True,
        'W': True,
        'X': True,
        'Y': True,
        'Z': True,
        '!': True,
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
        # self.driver.connect()
        if cur:
            self.driver.click(f"{self.button}:contains(\"{self.shift}\")")

        self.driver.sleep(0.5)
        self.driver.click(f"{self.button}:contains(\"{symbol}\")")

        # self.driver.disconnect()
