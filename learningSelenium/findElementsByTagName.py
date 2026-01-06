from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class findByTagName():
    def findBytagName(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/login.php")

        #driver.find_element(By.TAG_NAME,'input').send_keys("Kaleeshadilum22@gmail.com")
        driver.find_element(By.CLASS_NAME,"inputtext").send_keys("kaleesha")
        time.sleep(400)


TagName = findByTagName()
TagName.findBytagName()