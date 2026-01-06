from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.yahoo.com")
driver.maximize_window()
print(driver.title)
#driver.close()

time.sleep(10)