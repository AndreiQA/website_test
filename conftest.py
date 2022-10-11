import pytest
from selenium import webdriver

telephone = '293389920'
telephone_wrong = '293389922'
password = "Xbyfyf1212"
password_wrong = "Xbyfyf1222"
email = "andrei.ananich@gmail.com"
email_wrong = "andrei.ananich@gmail.by"
login_do_long = "login_so_long = (By.XPATH, //div[text()=Значение больше 100 знаков. Возможно, это ошибка? and @class=error-message)"

@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


