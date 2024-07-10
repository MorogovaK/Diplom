import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Проверка загрузки главной страницы")
@allure.feature("READ")
@allure.severity("blocker")
def test_chitai_gorod(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()

@allure.title("Поиск книги на кириллице")
@allure.description("Проверка получения книг на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_search_book_rus_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на кириллице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_book_rus_ui('планы на лето')
        assert text [0:53] == "Показываем результаты по запросу «планы на лето», 2 р"

@allure.title("Поиск книги на латинице")
@allure.description("Проверка получения книг на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_search_book_eng_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на латинице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_book_eng_ui('Master i Margarita')
        assert text [0:53] == "Показываем результаты по запросу «master i margarita»"

@allure.title("Поиск по автору")
@allure.description("Проверка поиска по автору")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_search_invalid_ui():
    with allure.step("Открытие веб-страницы в Chrome, ввод автора"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_invalid_ui('Анна Джейн')
        assert text == "Показываем результаты по запросу «анна джейн», 129 результатов"

@allure.title("Переход на вкладку 'Распродажа'")
@allure.description("Проверка перехода на вкладку 'Распродажа' на сайте Читай-город")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_open_sales_tab():
    with allure.step("Переход на вкладку 'Распродажа' "):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = browser.find_element(By.CSS_SELECTOR, ".header-bottom__link").text
        assert text == "Акции"