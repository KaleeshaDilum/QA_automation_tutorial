import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class handleCalander:
    def handlecalander(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.booking.com")
        driver.maximize_window()

        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-testid='searchbox-dates-container']")
        )).click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "(//button[@class='de576f5064 dc15842869 f1f96fdf10 d10abb4e59'])[1]")
        # )).click()
        #
        # driver.find_element(By.XPATH, "(//span[@aria-label='Sa 17 January 2026'])[1]").click()
        # time.sleep(4)

        dates = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//span[@data-date]")))

        for date in dates:
            print(date.text)
            if date.get_attribute("data-date") == "2026-01-17":
                date.click()
                print("Sucessfully clicked on date")
                time.sleep(6)
                break

handleCalander1= handleCalander()
handleCalander1.handlecalander()



