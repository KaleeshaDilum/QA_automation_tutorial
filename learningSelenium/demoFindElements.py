from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class findByTagName():
    def findBytagName(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/login.php")
        lista=(driver.find_elements(By.TAG_NAME,"a"))
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(4)


TagName = findByTagName()
TagName.findBytagName()