from selenium import webdriver
import time

class BrowserCommands:

    def browser_command_line(self):
        driver = webdriver.Chrome()
        driver.get("https://facebook.com")
        print(driver.title)
        driver.maximize_window()
        time.sleep(5)
        driver.minimize_window()
        time.sleep(10)


test1 = BrowserCommands()
test1.browser_command_line()