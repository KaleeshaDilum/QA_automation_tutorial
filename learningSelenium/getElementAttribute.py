from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class getAttribute:
    def getAttribute1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.figma.com/login")

        wait = WebDriverWait(driver, 15)

        # Locate button by visible text instead of type='submit'
        button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Log in') or contains(.,'Sign in')]"))
        )

        # Most buttons don’t have "value" attribute
        attr_value = button.get_attribute("value")
        print("value attribute:", attr_value)

        # Better: print the button text
        print("button text:", button.text)

        time.sleep(5)
        driver.quit()

demo = getAttribute()
demo.getAttribute1()
