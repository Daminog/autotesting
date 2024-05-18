from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class BasePage:

    def __init__(self):
        self.URL = "https://mospolytech.ru/"
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(options=options)

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def start_session(self):
        return self.driver.get(self.URL)

    def stop_session(self):
        return self.driver.close()
