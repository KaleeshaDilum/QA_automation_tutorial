from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class handleIframes:
    def handleIframes(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://seleniumbase.io/w3schools/iframes")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        result=wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='seleniumbase.io/w3schools/iframes']")))
        result.click()
        time.sleep(5)
        print("Clicked")




handleIframes1 = handleIframes()
handleIframes1.handleIframes()
