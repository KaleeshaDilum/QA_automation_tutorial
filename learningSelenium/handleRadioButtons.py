from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class handleRadioButton():

    def handleRadioButton1(self):
        driver = webdriver.Chrome()
        driver.get("https://practice.expandtesting.com/radio-buttons")

        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"blue").click()
        check_result=driver.find_element(By.ID,"blue").is_selected()
        print(check_result)
        time.sleep(2)

result = handleRadioButton()
result.handleRadioButton1()

