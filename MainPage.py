import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(15)
        

    with allure.step("Принятие файлов куки"):
        def set_cookie_policy(self): 
            cookie = {"name": "cookie_policy", "value": "1"}
            self._driver.add_cookie(cookie)

    with allure.step("Поиск книги на кириллице"):
        def search_book_rus_ui(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

        def search_book_eng_ui(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

        def search_invalid_ui(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            txt = self._driver.find_element(By.CLASS_NAME, "catalog-empty-result__description").text
            return txt

        def get_empty_cart(self):
            self._driver.find_element(By.CLASS_NAME, "header-cart__icon header-cart__icon--desktop").click()
            txt = self._driver.find_element(By. CLASS_NAME, "empty-title").text
            return txt