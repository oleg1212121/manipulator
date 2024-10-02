from seleniumbase import SB
from Manipulations.Manipulator import Manipulator


extension_dir = "Extensions/Proxy/"
proxy = ''

with SB(
        uc=True,
        log_cdp_events=True,
        uc_cdp_events=True,
        incognito=True
        # extension_dir=extension_dir,
        # Proxy=Proxy
) as driver:
    driver.maximize_window()
    driver.sleep(1)

    manipulator = Manipulator(driver)
    manipulator.run()

    driver.driver.connect()
    print("end")






