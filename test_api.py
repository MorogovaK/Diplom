import requests
import pytest
import allure
import unittest
from allure_commons.types import Severity
from allure_pytest.helper import allure_step

BASE_URL = "https://www.chitai-gorod.ru/api/v1/" 
BASE_URL_2 = "https://web-gate.chitai-gorod.ru/api/v2"
book_id = "plany-na-leto-3039541"

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjU1MjE4MDQsImlhdCI6MTcyMDYxMDA4NiwiZXhwIjoxNzIwNjEzNjg2LCJ0eXBlIjoyMH0.vDpqAAQxzUCvLXjEmrSZo6L3J8VvLvfzOK_g_Fb5g3U"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}" if API_TOKEN else None,
    "Content-Type": "application/json",
}

@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test

def test_get_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(f"{BASE_URL_2}/products", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.title("Тест получения списка книг по автору")
@allure.description("Проверка успешного получения списка книг по автору")
@allure.feature("API Читай-город")
@allure.severity(Severity.NORMAL)
@pytest.mark.api_test
def test_get_books_by_author():
    author_name = "Толстой"
    with allure.step(f"Отправка GET-запроса к /search?q={author_name}"):
        response = requests.get(f"{BASE_URL}/search?q={author_name}", headers=HEADERS)

    with allure.step("Проверка кода ответа"):
        assert response.status_code == 200


@allure.feature("API")
@allure.story("Получение информации о книге по ID")
@pytest.mark.api_test

def test_get_book_by_id():
    book_id = "plany-na-leto-3039541"    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL}/products/slug/{book_id}", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "Лавринович Ася" in response.text

@allure.feature("API")
@allure.story("Получение списка книг по категории")
@pytest.mark.api_test
def test_get_category_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?forceFilters[categories]=110282", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Добавление книги в корзину")
@pytest.mark.api_test
def test_add_book_to_cart():
    data = {
        "id": '3039541',
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.post(f"{BASE_URL}/cart/product", json=data, headers=headers)
    assert response.status_code == 400, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.title("Тест получения информации о книге по ID")
@allure.description("Проверка успешного получения информации о книге по ID")
@allure.feature("API Читай-город")
@allure.severity(Severity.NORMAL)
@pytest.mark.api_test
def test_get_book_by_id():
    book_id = 3039541  
    with allure.step(f"Отправка GET-запроса к /book/{book_id}"):
        response = requests.get(f"{BASE_URL}/book/{book_id}", headers=HEADERS)

    with allure.step("Проверка кода ответа"):
        assert response.status_code == 200

    with allure.step("Проверка наличия данных"):
        assert response.json().get("id") == book_id