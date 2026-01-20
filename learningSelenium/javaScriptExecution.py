from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class demosJS:
    def demo_javaScript(self):
        driver = webdriver.Chrome()
        wait =WebDriverWait(driver, 15)
       # driver.get("https://www.facebook.com/")
        driver.execute_script("window.open('https://www.facebook.com/'),'_self'")
        driver.maximize_window()
        time.sleep(5)


js= demosJS()
js.demo_javaScript()