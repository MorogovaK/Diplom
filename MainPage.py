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
        self._driver.implicitly_wait(10)
        

    with allure.step("Принятие файлов куки"):
        def set_cookie_policy(self): 
            cookie = {"name": "cookie_policy", "value": "1"}
            self._driver.add_cookie(cookie)

    with allure.step("Поиск книги на кириллице"):
        def search_book_rus_ui(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            wait = WebDriverWait(self._driver, 20)
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

    with allure.step("Открытие веб-страницы в Chrome, поиск книги на латинице"):    
        def search_book_eng_ui(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            wait = WebDriverWait(self._driver, 20)
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

    with allure.step("Открытие веб-страницы в Chrome, ввод автора"):    
        def search_invalid_ui(self, author):
            self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(author)
            self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
            wait = WebDriverWait(self._driver, 20)
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

    with allure.step("Переход на вкладку 'Распродажа' "):   
        def open_sales_tab(self):
            sales_tab = self._driver.find_element(By.XPATH, "//a[@href='/sale']")
            sales_tab.click()
            wait = WebDriverWait(self._driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-bottom__link")))