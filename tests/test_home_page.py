"""modules"""
from time import sleep
from selenium.webdriver import ActionChains
import conftest
from pages.home_page import HomePage
import allure
from conftest import telephone, password, email, telephone_wrong, password_wrong


@allure.feature('Home Page')
@allure.story('Logo')
def test_logo(driver):
    """modules"""
    with allure.step("Test"):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.logo.is_displayed()


@allure.feature('Home Page')
@allure.story('Tabs')
def test_transport(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.transport_tab.click()
    home_page.repair_pats_tab.click()
    home_page.wheels_tab.click()
    home_page.auto_journal_tab.click()
    home_page.knowledge_tab.click()
    home_page.finance_tab.click()
    assert home_page.transport_tab.is_displayed()
    assert home_page.repair_pats_tab.is_displayed()
    assert home_page.wheels_tab.is_displayed()
    assert home_page.auto_journal_tab.is_displayed()
    assert home_page.knowledge_tab.is_displayed()
    assert home_page.finance_tab.is_displayed()


# def test_footer_text(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.footer_text.click()
#     sleep(6)
#     assert home_page.footer_text.is_displayed()


@allure.feature('Home Page')
@allure.story('Sign in')
def test_sign_in_email(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.sign_in_email_tab.click()
    home_page.sign_in_email_field.click()
    home_page.sign_in_email_field.send_keys(email)
    sleep(2)
    home_page.password.click()
    sleep(2)
    home_page.password.send_keys(password)
    sleep(2)
    home_page.login_submit.click()
    sleep(2)
    ActionChains(driver).move_to_element(home_page.sign_out_dropdown).\
        click(home_page.sign_out_button).perform()
    sleep(3)


@allure.feature('Home Page')
@allure.story('Sign in')
def test_telephone_wrong(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.telephone.send_keys(telephone_wrong)
    sleep(2)
    home_page.password.click()
    sleep(2)
    home_page.password.send_keys(password)
    sleep(2)
    home_page.login_submit.click()
    sleep(2)
    assert home_page.telephone_wrong.is_displayed()
    sleep(2)


@allure.feature('Home Page')
@allure.story('Sign in')
def test_password_wrong(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.telephone.send_keys(telephone)
    sleep(2)
    home_page.password.click()
    sleep(2)
    home_page.password.send_keys(password_wrong)
    sleep(2)
    home_page.login_submit.click()
    sleep(2)
    assert home_page.telephone_wrong.is_displayed()
    sleep(2)


@allure.feature('Home Page')
@allure.story('Sign in')
def test_sign_in_email_wrong(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.sign_in_email_tab.click()
    home_page.sign_in_email_field.click()
    home_page.sign_in_email_field.send_keys(conftest.email_wrong)
    sleep(2)
    home_page.password.click()
    sleep(2)
    home_page.password.send_keys(password)
    sleep(2)
    home_page.login_submit.click()
    sleep(4)
    assert home_page.email_wrong.is_displayed()
    sleep(2)


@allure.feature('Home Page')
@allure.story('Sign in')
def test_login_so_long(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.sign_in_email_tab.click()
    home_page.sign_in_email_field.click()
    home_page.sign_in_email_field.send_keys(conftest.login_do_long)
    sleep(2)
    home_page.password.click()
    sleep(2)
    home_page.password.send_keys(password)
    sleep(2)
    home_page.login_submit.click()
    sleep(4)
    assert home_page.login_so_long.is_displayed()
    sleep(2)

@allure.feature('Home Page')
@allure.story('Sign in')
def test_sign_in(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.telephone.send_keys(telephone)
    sleep(2)
    home_page.password.click()
    sleep(2)
    home_page.password.send_keys(password)
    sleep(2)
    home_page.login_submit.click()
    sleep(2)
    ActionChains(driver).move_to_element(home_page.sign_out_dropdown).\
        click(home_page.my_warnings).perform()
    assert home_page.my_warnings_empty.is_displayed()
    sleep(2)
    home_page.transport_tab.click()



@allure.feature('Home Page')
@allure.story('Additional')
def test_bookmark_add_del(driver):
    """modules"""
    cars_page = HomePage(driver)
    cars_page.open()
    if cars_page.bookmark_add.click():
        sleep(2)
    else:
        cars_page.bookmark_del.click()
        sleep(2)


@allure.feature('Home Page')
@allure.story('Additional')
def test_advert_add(driver):
    """modules"""
    cars_page = HomePage(driver)
    cars_page.open()
    cars_page.advert_add.click()
    sleep(2)


@allure.feature('Home Page')
@allure.story('Additional')
def test_mobile_app(driver):
    """modules"""
    cars_page = HomePage(driver)
    cars_page.open()
    assert cars_page.mobile_app_android.is_displayed()
    assert cars_page.mobile_app_iphone.is_displayed()
    assert cars_page.mobile_app_huawei.is_displayed()


@allure.feature('Home Page')
@allure.story('Sign in')
def test_registration(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.cookies
    home_page.sign_in.click()
    sleep(1)
    home_page.registration.click()
    sleep(4)
    home_page.registration_form.click()
    assert home_page.registration_form.is_displayed()
    sleep(2)


@allure.feature('Home Page')
@allure.story('Sign in')
def test_remember_password(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.sign_in.click()
    sleep(1)
    home_page.remember_password.click()
    sleep(4)
    home_page.request_new_password.click()
    assert home_page.request_new_password.is_displayed()
    sleep(4)
