import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class findElementByXpath:
    def locate_by_xpath_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.semrush.com/login/?src=header&redirect_to=%2Fwebsite%2Ftop%2Funited-states%2Ftravel-and-tourism%2F")

        driver.find_element(By.XPATH,"//input[@id='email']").send_keys("harshana@gmail.com")

        time.sleep(60)
        driver.quit()


xpathDemo = findElementByXpath()
xpathDemo.locate_by_xpath_demo()
