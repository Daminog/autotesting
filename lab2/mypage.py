from base_page import BasePage
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time

class MyPage(BasePage):
    def get_screenshot(self):
        self.driver.save_screenshot("screenshot.png")

    def open_list(self):
        self.find_element(Locators.OPEN_BTN_LIST).click()
        time.sleep(1)
        return len(self.find_elements(Locators.STUDENTS))

    def go_to_table(self):
        element = self.find_elements(Locators.STUDENTS)[1]
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()
        time.sleep(1)
        self.find_elements(Locators.SCHEDULE)[0].click()
        time.sleep(1)
        self.find_elements(Locators.SCHEDULE_URL)[0].click()
        time.sleep(1)
        return self.driver.title

    def checking_schedule(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_element(Locators.INPUT).send_keys("221-323")
        self.find_element(Locators.GROUP).click()
        time.sleep(1)

    def check_color(self):
        parent = self.find_element(Locators.PARENT)
        data = parent.find_element(*Locators.DAY).text
        time.sleep(1)
        return data
