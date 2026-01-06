from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class demoElmentByIDandName:
    def locate_by_id_demo(self):
        # Method 2: Selenium 4 auto-manages ChromeDriver
        driver = webdriver.Chrome()
        driver.get(
            "https://www.semrush.com/login/?src=header&redirect_to=%2Fwebsite%2Ftop%2Funited-states%2Ftravel-and-tourism%2F"
        )
        driver.find_element(By.NAME, "email").send_keys("kaleeshadilum22@gmail.com")


        time.sleep(60)
        driver.quit()


findbyID = demoElmentByIDandName()
findbyID.locate_by_id_demo()
