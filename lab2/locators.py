from selenium.webdriver.common.by import By

class Locators:
    OPEN_BTN_LIST = (By.CLASS_NAME, "hamburger")
    STUDENTS = (By.XPATH, "//a[@title='Обучающимся']")
    SCHEDULE = (By.XPATH, "//a[@title='Расписания']")
    SCHEDULE_URL = (By.XPATH, "//a[@href='https://rasp.dmami.ru/']")
    INPUT = (By.CLASS_NAME, "groups")
    GROUP = (By.ID, "221-323")
    PARENT = (By.CLASS_NAME, "schedule-day_today")
    DAY = (By.CLASS_NAME, "schedule-day__title")
