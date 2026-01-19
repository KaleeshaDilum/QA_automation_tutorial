from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class handleMultipleWindows:
    def handleMultipleWindows(self):
        driver =webdriver.Chrome()
        wait = WebDriverWait(driver, 15)
        driver.get("https://sg.yahoo.com/?p=us")
        parent_handle = driver.current_window_handle
        print("Parent handle:",parent_handle)
        driver.maximize_window()
        time.sleep(5)

        findElement1= wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Check your mail']")))
        if findElement1:
            findElement1.click()
            print("Clicked")

        all_handles=driver.window_handles
        print("All handles:", all_handles)

        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)

        findElement2= wait.until(EC.presence_of_element_located((By.ID, "login-signin")))
        if findElement2:
            findElement2.click()
            print("Clicked")
            time.sleep(5)

test1 = handleMultipleWindows()
test1.handleMultipleWindows()



