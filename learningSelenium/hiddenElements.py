from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class demoEnable_Disable():
    def demoEnable(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        demo_state=driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("kaleeshadilum")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("sample")
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state1)

        time.sleep(3)



demoEnable_Disable = demoEnable_Disable()
demoEnable_Disable.demoEnable()