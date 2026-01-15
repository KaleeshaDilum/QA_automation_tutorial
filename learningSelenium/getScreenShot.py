from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class getScreenShot:
    def getScreenShot(self):
        driver = webdriver.Chrome()
        wait =WebDriverWait(driver, 15)
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(5)

        username=wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@id='email']")
        ))
        username.send_keys("testemail@gmail.com")
        username.screenshot("test_screenshot.png")
        time.sleep(5)
        password = wait.until(EC.presence_of_element_located(
            (By.ID, "pass")
        ))

        password.send_keys("testPassword")
        time.sleep(5)
        button = driver.find_element(By.XPATH,"(//button[normalize-space()='Log in'])[1]")
        button.click()
        driver.save_screenshot("test_screenshot_full_page.png")


testRun1 = getScreenShot()
testRun1.getScreenShot()



