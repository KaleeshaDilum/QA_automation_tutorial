import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class demoByCSSselector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.semrush.com/login/?src=header&redirect_to=%2Fwebsite%2Ftop%2Funited-states%2Ftravel-and-tourism%2F")

        driver.find_element(By.CSS_SELECTOR,"#email").send_keys("TharindiDananjana@gmail.com")

        time.sleep(40)
        driver.quit()

demoBycss = demoByCSSselector()
demoBycss.locate_by_id_demo()