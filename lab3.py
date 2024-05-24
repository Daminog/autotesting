import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64


class Market:
    def __init__(self, driver):
        self.driver = driver
        self.catalog_menu = (By.XPATH, "//button[.//span[text()='Каталог']]")
        self.category_menu = (By.XPATH, "//a/span[text()='Ноутбуки и компьютеры']")
        self.hdd_menu = (By.XPATH, "//a[text()='Внутренние жесткие диски']")
        self.sort_option = (By.XPATH, "//div[.//h2[text()='Сортировка']]//button[text()='подешевле']")
        self.product_card = (
        By.XPATH, "//div[@data-auto-themename='listDetailed' and .//button[@title='Добавить в избранное']]")
        self.product_title = (By.XPATH, ".//h3[@data-auto='snippet-title']")
        self.product_price = (By.XPATH, ".//span[@data-auto='snippet-price-current']//span[1]")

    def open(self):
        self.driver.get("https://market.yandex.ru")
        self.driver.add_cookie({'name': 'spravka', 'value': ''})
        self.driver.get("https://market.yandex.ru")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.catalog_menu))

    def navigate_to_hdd(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.catalog_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.category_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.hdd_menu)).click()

    def set_sort_by_price(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sort_option)).click()

    def get_first_n_products(self, n):
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.product_card))
        elements = []
        for product in products[:n]:
            product_name = product.find_element(*self.product_title).text
            product_price = product.find_element(*self.product_price).text.replace(' ', '')
            elements.append({'name': product_name, 'price': product_price})
        return elements

    def is_sorted(self, products):
        return all(float(products[i - 1]['price']) <= float(products[i]['price']) for i in range(1, len(products)))


class TestMarket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.market_page = Market(self.driver)
        self.market_page.open()

    def tearDown(self):
        # Check if the test failed
        if not self._outcome.success:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            test_case_name = self._testMethodName
            file_name = f"{test_case_name}_{timestamp}.png"
            screenshot = self.driver.get_screenshot_as_base64()
            with open(file_name, "wb") as f:
                f.write(base64.b64decode(screenshot))
            print(f"Test failed. Screenshot saved as {file_name}")
        self.driver.quit()

    def test_get_hdd_top_5_lowest_price(self):
        self.market_page.navigate_to_hdd()
        time.sleep(3)
        first_five_products = self.market_page.get_first_n_products(5)
        print("First five products:", first_five_products)

        self.market_page.set_sort_by_price()
        time.sleep(3)
        first_five_sorted_products = self.market_page.get_first_n_products(10)
        print("First five sorted products:", first_five_sorted_products)

        sorted_flag = self.market_page.is_sorted(first_five_sorted_products)
        print("Is sorted:", sorted_flag)
        self.assertTrue(sorted_flag)


if __name__ == "__main__":
    unittest.main()
