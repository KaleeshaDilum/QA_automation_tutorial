from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class getTextElement():
    def getTextElement1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.figma.com/login")

        #driver.find_element(By.TAG_NAME,'input').send_keys("Kaleeshadilum22@gmail.com")
        element = driver.find_element(By.XPATH, "//h1[normalize-space()='Sign in to Figma']")
        print(element.text)
        time.sleep(20)


TagName = getTextElement()
TagName.getTextElement1()