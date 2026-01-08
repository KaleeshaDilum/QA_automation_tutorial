import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class handleAutoSugesstions:
    def handleAutoSugesstions(self):
        driver = webdriver.Chrome()
        driver.get("https://www.booking.com/")
        driver.maximize_window()
        time.sleep(5)

        # search=driver.find_element(By.ID, ":rh:")
        # search.click()
        # time.sleep(2)
        # search.send_keys("Kalutara")
        # search.send_keys(Keys.ENTER)
        # time.sleep(2)

        search = driver.find_element(By.NAME, "ss")
        search.click()
        search.clear()
        search.send_keys("Kalutara")
        time.sleep(5)

        wait = WebDriverWait(driver, 15)

        suggestions = wait.until(
            EC.presence_of_all_elements_located((By.XPATH,"//li[@role='option']"))
        )

        print("Suggestions:")
        for s in suggestions:
            print(s.text)
        print("------------------------------------------------------------------------------")
        clickHotel = wait.until(
            EC.element_to_be_clickable((By.XPATH,"//li[@role='option' and contains(.,'Turyaa Kalutara')]")),

        )
        print("Success")
        clickHotel.click()

        time.sleep(5)


test1 = handleAutoSugesstions()
test1.handleAutoSugesstions()
