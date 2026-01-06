from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class demoHiddenElement:
    def demoHiddenElement(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        result1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(result1)
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)
        result=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(result)

        time.sleep(5)

Check1=demoHiddenElement()
Check1.demoHiddenElement()
