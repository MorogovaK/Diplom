import requests
import allure
import pytest
import unittest

BASE_URL = "https://web-gate.chitai-gorod.ru/api/v1"
BASE_URL_2 = "https://web-gate.chitai-gorod.ru/api/v2"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjU1MjE4MDQsImlhdCI6MTcyMDYzMjA2NywiZXhwIjoxNzIwNjM1NjY3LCJ0eXBlIjoyMH0.6QO2mrF7SA71IwdfGg6ZWWkaNiRcGDTMGVFq_NnS2mw"

@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test
def test_get_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }
    response = requests.get(f"{BASE_URL_2}/products", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Поиск книг на латинице")
@pytest.mark.api_test
def test_search_books_eng():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=phyton", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Пробел")
@pytest.mark.api_test
def test_search_space():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=   ", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"


@allure.feature("API")
@allure.story("Получение списка книг по категории")
@pytest.mark.api_test
def test_get_category_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?forceFilters[categories]=110282", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка книг по фильтрам")
@pytest.mark.api_test
def test_get_filtres_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?filters[onlyNew]=1", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"      


@allure.feature("API")
@allure.story("Получение списка книг по автору")
@pytest.mark.api_test
def test_get_books_by_author():      
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products/facet?filters[authors]=593251", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}" 