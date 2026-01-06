from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class handleCheckBox:
    def handleCheckBox(self):
        driver = webdriver.Chrome()
        driver.get("https://practice.expandtesting.com/checkboxes")

        driver.maximize_window()
        driver.find_element(By.ID,"checkbox1").click()
        selectResult=driver.find_element(By.ID,"checkbox2").is_selected()
        print(selectResult)
        time.sleep(2)

result = handleCheckBox()
result.handleCheckBox()

