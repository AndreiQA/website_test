"""modules"""
import requests
import allure

@allure.feature('API test')
@allure.story('Status code')
def test_available_access():
    """modules"""
    response = requests.get("http://av.by", timeout=10)
    assert response.status_code == 200


@allure.feature('API test')
@allure.story('Status code')
def test_not_available_access():
    """modules"""
    response = requests.get("https://cars.av.by/alfa-romeo/giulietta/100889306", timeout=10)
    assert response.status_code != 200


@allure.feature('API test')
@allure.story('Status code')
def test_not_authorize_access():
    """modules"""
    response = requests.get("http://av.by/api", timeout=10)
    text = response.json
    print(text)
    assert response.status_code == 401


@allure.feature('API test')
@allure.story('Headers')
def test_check_headers():
    """modules"""
    response = requests.get("http://av.by/api", timeout=10)
    data = response.request.headers
    print(data)
    assert response.headers["Connection"] == "keep-alive"
