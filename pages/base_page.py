"""modules"""


class BasePage:
    """modules"""
    def __init__(self, driver):
        """modules"""
        self.driver = driver

    def find_element(self, *args):
        """modules"""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        """modules"""
        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)
