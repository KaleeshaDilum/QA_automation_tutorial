from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class demoEnable_Disable():
    def demoEnable(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")

        #driver.find_element(By.TAG_NAME,'input').send_keys("Kaleeshadilum22@gmail.com")
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("username")
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("password")
        time.sleep(3)
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        time.sleep(4)
        driver.find_element(By.XPATH,"//input[@id='login_button']").click()


        print(demo_state)
        time.sleep(70)


checkEnable = demoEnable_Disable()
checkEnable.demoEnable()