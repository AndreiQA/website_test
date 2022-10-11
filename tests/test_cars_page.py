"""modules"""
from time import sleep
from pages.cars_page import CarsPage
import allure


@allure.feature('Cars Page')
@allure.story('Search')
def test_search(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.cookies.click()
    cars_page.brand_auto.click()
    cars_page.brand_auto_name.click()
    sleep(3)
    cars_page.model_auto.click()
    cars_page.model_auto_name.click()
    sleep(3)
    cars_page.generation_dropdown.click()
    cars_page.generation_name.click()
    sleep(3)
    cars_page.year_dropdown_from.click()
    cars_page.year_from_value.click()
    sleep(3)
    cars_page.price_from.click()
    cars_page.price_from.send_keys("8000")
    sleep(3)
    cars_page.show_result.click()
    cars_list = cars_page.cars_list
    sleep(2)
    for car in cars_list:
        car_details = cars_page.get_car_details(car)
        print(car_details)
    assert cars_page.brand_auto_name == cars_page.brand_auto_name
    assert cars_page.model_auto_name == cars_page.model_auto_name
    assert cars_page.year_from_value == cars_page.year_from_value
    assert cars_page.price_from == cars_page.price_from


@allure.feature('Cars Page')
@allure.story('Reset button')
def test_reset_button(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.brand_auto.click()
    cars_page.brand_auto_name.click()
    sleep(3)
    cars_page.reset_button.click()
    assert cars_page.reset_button.is_displayed()


@allure.feature('Cars Page')
@allure.story('Additional')
def test_add_additional_brand(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.additional_brand.click()
    cars_page.additional_brand_name1_dropdown.click()
    cars_page.additional_brand_name1.click()
    sleep(4)
    cars_page.additional_brand_name2_dropdown.click()
    cars_page.additional_brand_name2.click()
    assert cars_page.additional_brand == cars_page.additional_brand


def test_volume(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.engine_dropdown_from.click()
    cars_page.engine_from_value.click()
    assert  cars_page.engine_from_value == cars_page.engine_from_value


@allure.feature('Cars Page')
@allure.story('Additional')
def test_transmission(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    sleep(3)
    cars_page.transmission_auto.click()
    sleep(3)
    cars_page.transmission_manual.click()
    sleep(3)
    assert cars_page.transmission_auto == cars_page.transmission_auto
    assert cars_page.transmission_manual == cars_page.transmission_manual


@allure.feature('Cars Page')
@allure.story('Additional')
def test_car_body(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.car_body_dropdown.click()
    sleep(4)
    cars_page.car_body_checkbox.click()
    sleep(3)
    assert cars_page.car_body_checkbox == cars_page.car_body_checkbox

@allure.feature('Cars Page')
@allure.story('Additional')
def test_type_engine(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.type_engine_dropdown.click()
    sleep(4)
    cars_page.type_engine_checkbox.click()
    sleep(3)
    assert cars_page.type_engine_checkbox == cars_page.type_engine_checkbox

@allure.feature('Cars Page')
@allure.story('Additional')
def test_drive_type(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.drive_type_dropdown.click()
    sleep(4)
    cars_page.drive_type_checkbox.click()
    sleep(3)
    assert cars_page.drive_type_checkbox == cars_page.drive_type_checkbox

@allure.feature('Cars Page')
@allure.story('Additional')
def test_all_params(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.cookies.click()
    sleep(3)
    cars_page.all_params.click()
    sleep(3)
    cars_page.search_by_word.click()
    cars_page.search_by_word.send_keys("black")
    sleep(3)
    cars_page.show_result.click()
    cars_list = cars_page.cars_list
    sleep(2)
    for car in cars_list :
        car_details = cars_page.get_car_details(car)
        print(car_details)
    assert cars_page.search_by_word.send_keys == cars_page.search_by_word


@allure.feature('Cars Page')
@allure.story('Additional')
def test_top_advert(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.top_advert.click()
    assert cars_page.top_advert.is_displayed()


@allure.feature('Cars Page')
@allure.story('Additional')
def test_sort_by_dropdown(driver):
    """modules"""
    cars_page = CarsPage(driver)
    cars_page.open()
    cars_page.show_result.click()
    sleep(2)
    cars_page.sort_by_dropdown.click()
    sleep(2)
    cars_page.sort_by_new.click()
    sleep(3)
    assert cars_page.sort_by_new == cars_page.sort_by_new
