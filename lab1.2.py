import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64

class TodoPage:
    HEADER = (By.XPATH, '//h2')
    TODO_REMAINING_TEXT = (By.XPATH, '//span[contains(text(), "remaining")]')
    TODO_INPUT = (By.ID, 'sampletodotext')
    ADD_BUTTON = (By.ID, 'addbutton')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')

    def get_header(self):
        return self.driver.find_element(*self.HEADER).text

    def get_todo_remaining_text(self):
        return self.driver.find_element(*self.TODO_REMAINING_TEXT).text

    def click_todo_by_index(self, index):
        todo = (By.NAME, f'li{index}')
        self.driver.find_element(*todo).click()

    def add_todo_item(self, text):
        self.driver.find_element(*self.TODO_INPUT).send_keys(text)
        self.driver.find_element(*self.ADD_BUTTON).click()

class TestTodoApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.page = TodoPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        if any(error for method, error in self._outcome.result.errors):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            test_case_name = self._testMethodName
            file_name = f"{test_case_name}-{timestamp}.png"
            screenshot = self.driver.get_screenshot_as_base64()
            with open(file_name, "wb") as f:
                f.write(base64.b64decode(screenshot))

    def test_display_correct_header(self):
        self.page.open()
        header = self.page.get_header()
        self.assertEqual(header, 'LambdaTest Sample App')

    def test_update_remaining_todos(self):
        self.page.open()
        remaining_text = self.page.get_todo_remaining_text()
        self.assertEqual(remaining_text, '5 of 5 remaining')
        for i in range(1, 6):
            self.page.click_todo_by_index(i)
            remaining_text = self.page.get_todo_remaining_text()
            self.assertEqual(remaining_text, f'{5 - i} of 5 remaining')
        self.page.add_todo_item('TestTestTestTest')
        remaining_text = self.page.get_todo_remaining_text()
        self.assertEqual(remaining_text, '1 of 6 remaining')
        self.page.click_todo_by_index(6)
        remaining_text = self.page.get_todo_remaining_text()
        self.assertEqual(remaining_text, '0 of 6 remaining')

if __name__ == '__main__':
    unittest.main()
