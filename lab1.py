from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


def lambda_test():
    driver = webdriver.Chrome()

    try:
        # 1. Перейти по ссылке
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # 2. Проверить, что присутствует текст “5 of 5 remaining”
        print("Checking '5 of 5 remaining' text")
        remaining_text_element = driver.find_element(By.XPATH, "//*[text()='5 of 5 remaining']")
        print("Success")

        # 3. Получить все незачеркнутые элементы списка
        print("Getting all 5 input boxes")
        input_boxes = driver.find_elements(By.XPATH, "//li/span[@class='done-false']/preceding::input")
        assert len(input_boxes) == 5, f"Expected 5 checkboxes, but got {len(input_boxes)}"
        print("Success")

        # 4. Поставить галочки у всех элементов и проверить зачеркнутость и изменение текста
        for i in range(len(input_boxes)):
            print(f"Clicking on checkbox number {i + 1}")
            input_boxes[i].click()
            time.sleep(1)  # Небольшая задержка для визуального эффекта
            print("Success")

            print("Checking if the clicked element is crossed")
            crossed_element = driver.find_element(By.XPATH, f"//li[{i + 1}]/span[@class='done-true']/preceding::input")
            print("Success")

            print("Checking if number of elements decreased")
            remaining_count = 5 - (i + 1)
            remaining_text_element = driver.find_element(By.XPATH, f"//*[text()='{remaining_count} of 5 remaining']")
            print("Success")

        # 5. Добавить новый элемент списка
        print("Typing new item in input field")
        new_item_input = driver.find_element(By.XPATH, "//input[@id='sampletodotext']")
        new_item_input.send_keys("MosPolytech")
        print("Success")

        print("Submitting new item")
        add_button = driver.find_element(By.XPATH, "//input[@id='addbutton']")
        add_button.click()
        print("Success")

        # 6. Проверить, что новый элемент добавлен и текст изменился на "1 of 6 remaining"
        print("Check if number of elements increased")
        new_remaining_text_element = driver.find_element(By.XPATH, "//*[text()='1 of 6 remaining']")
        print("Success")

        # 7. Нажать на новый элемент списка и проверить его зачеркнутость
        print("Clicking on new item checkbox")
        new_item_checkbox = driver.find_element(By.XPATH, "//li[6]/input")
        new_item_checkbox.click()
        time.sleep(1)
        print("Success")

        print("Checking if new item is crossed")
        new_item = driver.find_element(By.XPATH, "//li[6]/span[@class='done-true']/preceding::input")
        print("Success")

    except Exception as e:
        # Сделать скриншот в случае ошибки
        driver.save_screenshot('screenshot_error.png')
        print(f"Error: {e}")
    finally:
        # Закрываем браузер
        print("Closing browser gracefully")
        driver.quit()


if __name__ == "__main__":
    lambda_test()
