"""modules"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


logo = (By.CLASS_NAME, "header__logo")
sign_in = (By.CLASS_NAME, "nav__item--login")
sign_in_email_tab = (By.XPATH, '//button[text()="почте или логину" and @class="tab"]')
sign_in_email_field = (By.ID, 'authLogin')
sign_out_dropdown = (By.XPATH, '//li[@class="nav__item nav__item--user nav__item--dropdown"]')
sign_out_button = (By.CLASS_NAME, 'nav__dropdown-logout')
my_warnings = (By.XPATH, '//span[text()="Предупреждения" and @class="nav__dropdown-text"]')
my_warnings_empty = (By.CLASS_NAME, 'warning-list-empty')
telephone = (By.ID, 'authPhone')
password = (By.NAME, "password")
telephone_wrong = (By.XPATH, '//div[text()="Неверный телефон или пароль. '
                             'Если забыли пароль, восстановите его" and @class="error-message"]')
password_wrong = (By.XPATH, '//div[text()="Неверный телефон или пароль. '
                            'Если забыли пароль, восстановите его" and @class="error-message"]')
email_wrong = (By.XPATH, '//div[text()="Неверный телефон или пароль. '
                         'Если забыли пароль, восстановите его" and @class="error-message"]')
login_so_long = (By.XPATH, '//div[text()="Значение больше 100 знаков. '
                           'Возможно, это ошибка?" and @class="error-message"]')
registration = (By.XPATH, '//span[text()="Регистрация" and @class="drawer__slide-toggle"]')
registration_form = (By.XPATH, '//button[text()="Зарегистрироваться" and @class="button__text"]')
remember_password = (By.CLASS_NAME, "auth__forgot")
request_new_password = (By.XPATH, '//div[text()="Запрос на восстановление пароля" '
                                  'and @class="auth__title"]')
login_submit = (By.XPATH, '//span[text()="Войти" and @class="button__text"]')
transport_tab = (By.XPATH, '//span[@class="nav__link-text" and text()="Транспорт"]')
wheels_tab = (By.XPATH, '//span[@class="nav__link-text" and text()="Шины и диски"]')
repair_pats_tab = (By.XPATH, '//span[@class="nav__link-text" and text()="Запчасти"]')
auto_journal_tab = (By.XPATH, '//span[@class="nav__link-text" and text()="Автожурнал"]')
knowledge_tab = (By.XPATH, '//span[@class="nav__link-text" and text()="Знания"]')
finance_tab = (By.XPATH, '//span[@class="nav__link-text" and text()="Финансы"]')
footer_text = (By.XPATH, "//p[text()='© 2001, ООО «Автоклассифайд», УНП 192787977, "
                         "Минск, ул. Кутузова 15' and @class='footer__copy']")
bookmark_add = (By.CSS_SELECTOR, 'button[class="bookmark"]')
bookmark_del = (By.CSS_SELECTOR, 'button[title="Удалить из закладок"]')
advert_add = (By.XPATH, '//span[text()="Подать объявление" and @class="button__text"]')
advert_field = (By.CLASS_NAME, "heading-title")
mobile_app_android = (By.XPATH, '//span[text()="Android" and @class="app-badge__platform"]')
mobile_app_iphone = (By.XPATH, '//span[text()="iPhone" and @class="app-badge__platform"]')
mobile_app_huawei = (By.XPATH, '//span[text()="Huawei" and @class="app-badge__platform"]')
cookies = (By.XPATH, '//*[@id="__next"]/div[3]/div/div/button/span')


class HomePage(BasePage):
    """modules"""
    def __init__(self, driver):
        """modules"""
        super().__init__(driver)
        self.driver = driver

    def open(self):
        """modules"""
        self.driver.get("https://av.by/")

    @property
    def logo(self):
        """modules"""
        return self.find_element(logo)

    @property
    def sign_in(self):
        """modules"""
        return self.find_element(sign_in)

    @property
    def sign_in_email_tab(self):
        """modules"""
        return self.find_element(sign_in_email_tab)

    @property
    def sign_in_email_field(self):
        """modules"""
        return self.find_element(sign_in_email_field)

    @property
    def sign_out_dropdown(self):
        """modules"""
        return self.find_element(sign_out_dropdown)

    @property
    def sign_out_button(self):
        """modules"""
        return self.find_element(sign_out_button)

    @property
    def my_warnings(self):
        """modules"""
        return self.find_element(my_warnings)

    @property
    def my_warnings_empty(self):
        """modules"""
        return self.find_element(my_warnings_empty)

    @property
    def telephone(self):
        """modules"""
        return self.find_element(telephone)

    @property
    def password(self):
        """modules"""
        return self.find_element(password)

    @property
    def email_wrong(self):
        """modules"""
        return self.find_element(email_wrong)

    @property
    def login_so_long(self):
        """modules"""
        return self.find_element(login_so_long)

    @property
    def registration(self):
        """modules"""
        return self.find_element(registration)

    @property
    def registration_form(self):
        """modules"""
        return self.find_element(registration_form)

    @property
    def remember_password(self):
        """modules"""
        return self.find_element(remember_password)

    @property
    def request_new_password(self):
        """modules"""
        return self.find_element(request_new_password)

    @property
    def telephone_wrong(self):
        """modules"""
        return self.find_element(telephone_wrong)

    @property
    def password_wrong(self):
        """modules"""
        return self.find_element(password_wrong)

    @property
    def login_submit(self):
        """modules"""
        return self.find_element(login_submit)

    @property
    def transport_tab(self):
        """modules"""
        return self.find_element(transport_tab)

    @property
    def wheels_tab(self):
        """modules"""
        return self.find_element(wheels_tab)

    @property
    def repair_pats_tab(self):
        """modules"""
        return self.find_element(repair_pats_tab)

    @property
    def auto_journal_tab(self):
        """modules"""
        return self.find_element(auto_journal_tab)

    @property
    def knowledge_tab(self):
        """modules"""
        return self.find_element(knowledge_tab)

    @property
    def finance_tab(self):
        """modules"""
        return self.find_element(finance_tab)

    @property
    def footer_text(self):
        """modules"""
        return self.find_element(footer_text)

    @property
    def bookmark_add(self):
        """modules"""
        return self.find_element(bookmark_add)

    @property
    def bookmark_del(self):
        """modules"""
        return self.find_element(bookmark_del)

    @property
    def advert_add(self):
        """modules"""
        return self.find_element(advert_add)

    @property
    def advert_field(self):
        """modules"""
        return self.find_element(advert_field)


    @property
    def mobile_app_android(self):
        """modules"""
        return self.find_element(mobile_app_android)

    @property
    def mobile_app_iphone(self):
        """modules"""
        return self.find_element(mobile_app_iphone)

    @property
    def mobile_app_huawei(self):
        """modules"""
        return self.find_element(mobile_app_huawei)

    @property
    def cookies(self):
        """modules"""
        return self.find_element(cookies)
