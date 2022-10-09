"""modules"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


brand_auto = (By.XPATH, '//span[text()="Марка" and @class="dropdown-floatlabel__value"]')
brand_auto_name = (By.CSS_SELECTOR, 'button[data-item-label="Alfa Romeo"]')
model_auto = (By.NAME, 'p-6-0-3-model')
model_auto_name = (By.CSS_SELECTOR, 'button[data-item-label="Giulietta"]')
generation_dropdown = (By.XPATH, '//span[text()="Поколение" '
                                 'and @class="dropdown-floatlabel__value"]')
generation_name = (By.XPATH, '//button[text()="Все поколения" '
                             'and @class="dropdown__listboxbutton"]')
year_dropdown_from = (By.XPATH, '//span[text()="Год от" '
                                'and @class="dropdown-floatlabel__value"]')
year_from_value = (By.CSS_SELECTOR, 'button[data-item-label="2010"]')
#year_dropdown_to = (By.XPATH, '//span[text()="до" and @class="dropdown-floatlabel__value"]')
#year_to_value = (By.CSS_SELECTOR, 'button[data-item-label="2020"]')
price_from = (By.ID, 'p-9-price_usd')
show_result = (By.XPATH, '//div[@class="filter__show-result"]/a')
cars_list = (By.CSS_SELECTOR, 'div[class="listing-item"]')
reset_button = (By.XPATH, '//span[text()="Сбросить"]')
additional_brand = (By.CSS_SELECTOR, 'button[class="button button--link button--small"]')
additional_brand_name1_dropdown = (By.XPATH, '//span[text()="Марка" '
                                             'and @class="dropdown-floatlabel__value"]')
additional_brand_name1 = (By.CSS_SELECTOR, 'button[data-item-label="Audi"]')
additional_brand_name2_dropdown = (By.XPATH, '//span[text()="Марка" '
                                             'and @class="dropdown-floatlabel__value"]')
additional_brand_name2 = (By.CSS_SELECTOR, 'button[data-item-label="BMW"]')
dropdown_content = (By.CSS_SELECTOR, 'ul[class="dropdown-list dropdown-list--opened"]')
engine_dropdown_from = (By.NAME, 'p-12-engine_capacity')
engine_from_value = (By.CSS_SELECTOR, 'button[data-item-label="1,0 л."]')
transmission_auto = (By.XPATH, '//span[text()="автомат" and @class="button-group__text"]')
transmission_manual = (By.XPATH, '//span[text()="механика" and @class="button-group__text"]')
car_body_dropdown = (By.NAME, 'p-14-body_type')
car_body_checkbox = (By.XPATH, '//span[text()="лимузин" and @class="checkbox__description"]')
type_engine_dropdown = (By.NAME, 'p-15-engine_type')
type_engine_checkbox = (By.XPATH, '//span[text()="электро" and @class="checkbox__description"]')
drive_type_dropdown = (By.NAME, 'p-16-drive_type')
drive_type_checkbox = (By.XPATH, '//span[text()="постоянный полный привод" '
                                 'and @class="checkbox__description"]')
all_params = (By.XPATH, '//span[text()="Все параметры" and @class="button__text"]')
search_by_word = (By.ID, 'p-32-description')
sort_by_dropdown = (By.XPATH, '//span[text()="актуальные" '
                              'and @class="dropdown-link__value"]')
sort_by_new = (By.CSS_SELECTOR, 'button[data-item-label="новые объявления"]')
filter_show = (By.XPATH, '//div[@class="button button--secondary button--block"]')
top_advert = (By.XPATH, '//h2[text()="Топ-объявления" and @class="featured__title"]')
cookies = (By.XPATH, '//*[@id="__next"]/div[3]/div/div/button/span')


"""modules"""

#pylint: disable=R0904
class CarsPage(BasePage):
    """modules"""
    def __init__(self, driver):
        """modules"""
        super().__init__(driver)
        self.driver = driver

    def open(self):
        """modules"""
        self.driver.get("https://cars.av.by/")

    @property
    def auto_list(self, *args):
        """modules"""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    @property
    def brand_auto(self):
        """modules"""
        return self.find_element(brand_auto)

    @property
    def brand_auto_name(self):
        """modules"""
        return self.find_element(brand_auto_name)

    @property
    def model_auto(self):
        """modules"""
        return self.find_element(model_auto)

    @property
    def model_auto_name(self):
        """modules"""
        return self.find_element(model_auto_name)

    @property
    def generation_dropdown(self):
        """modules"""
        return self.find_element(generation_dropdown)

    @property
    def generation_name(self):
        """modules"""
        return self.find_element(generation_name)

    @property
    def year_dropdown_from(self):
        """modules"""
        return self.find_element(year_dropdown_from)

    @property
    def year_from_value(self):
        """modules"""
        return self.find_element(year_from_value)

    @property
    def show_result(self):
        """modules"""
        return self.find_element(show_result)

    @property
    def cars_list(self):
        """modules"""
        return self.find_elements(cars_list)

    @staticmethod
    def get_car_details(car):
        """modules"""
        details_text = car.find_element(By.CSS_SELECTOR, 'div[class="listing-item__params"]').text
        details_to_list = details_text.split('\n')
        characteristics_list = details_to_list[1].split(',')
        car_details = {
            'year': details_to_list[0].replace('г.', '').strip(),
            'gear': characteristics_list[0],
            'volume': characteristics_list[1].replace('л', '').strip(),
            'mileage': details_to_list[2].replace(' ', '').replace('км', '').replace('\u2008', '')
        }
        return car_details

    @property
    def additional_brand_name1_dropdown(self):
        """modules"""
        return self.find_element(additional_brand_name1_dropdown)

    @property
    def additional_brand_name1(self):
        """modules"""
        return self.find_element(additional_brand_name1)

    @property
    def additional_brand_name2_dropdown(self):
        """modules"""
        return self.find_element(additional_brand_name2_dropdown)

    @property
    def additional_brand_name2(self):
        """modules"""
        return self.find_element(dropdown_content).find_element(*additional_brand_name2)

    @property
    def price_from(self):
        """modules"""
        return self.find_element(price_from)

    @property
    def reset_button(self):
        """modules"""
        return self.find_element(reset_button)

    @property
    def additional_brand(self):
        """modules"""
        return self.find_element(additional_brand)

    @property
    def engine_dropdown_from(self):
        """modules"""
        return self.find_element(engine_dropdown_from)

    @property
    def engine_from_value(self):
        """modules"""
        return self.find_element(engine_from_value)

    @property
    def transmission_auto(self):
        """modules"""
        return self.find_element(transmission_auto)

    @property
    def transmission_manual(self):
        """modules"""
        return self.find_element(transmission_manual)

    @property
    def car_body_dropdown(self):
        """modules"""
        return self.find_element(car_body_dropdown)

    @property
    def car_body_checkbox(self):
        """modules"""
        return self.find_element(car_body_checkbox)

    @property
    def type_engine_dropdown(self):
        """modules"""
        return self.find_element(type_engine_dropdown)

    @property
    def type_engine_checkbox(self):
        """modules"""
        return self.find_element(type_engine_checkbox)

    @property
    def drive_type_dropdown(self):
        """modules"""
        return self.find_element(drive_type_dropdown)

    @property
    def drive_type_checkbox(self):
        """modules"""
        return self.find_element(drive_type_checkbox)

    @property
    def all_params(self):
        """modules"""
        return self.find_element(all_params)

    @property
    def search_by_word(self):
        """modules"""
        return self.find_element(search_by_word)

    @property
    def sort_by_dropdown(self):
        """modules"""
        return self.find_element(sort_by_dropdown)

    @property
    def sort_by_new(self):
        """modules"""
        return self.find_element(sort_by_new)


    @staticmethod
    def get_car_details_search_word(car):
        """modules"""
        details_text = car.find_element(By.CSS_SELECTOR, 'div[class="listing-item__params"]').text
        details_to_list = details_text.split('\n')
        characteristics_list = details_to_list[1].split(',')
        car_details = {
            'year': details_to_list[0].replace('г.', '').strip(),
            'gear': characteristics_list[0],
            'volume': characteristics_list[1].replace('л', '').strip(),
            'mileage': details_to_list[2].replace(' ', '').replace('км', '').replace('\u2008', '')
        }
        return car_details

    @property
    def filter_show(self):
        """modules"""
        return self.find_element(filter_show)

    @property
    def top_advert(self):
        """modules"""
        return self.find_element(top_advert)

    @property
    def cookies(self):
        """modules"""
        return self.find_element(cookies)
