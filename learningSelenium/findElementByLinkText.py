from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class demobyLinkText:
    def demoByLinkText(self):
        driver = webdriver.Chrome()
        driver.get("https://www.booking.com/city/tw/huxi.en.html?aid=2276374&pagename=huxi&label=msn-ZDW6D9wJxGgeUmQhGSLNTg-80470715330324:tikwd-80470901935413:loc-36:neo:mte:lp147906:dec:qstravel&utm_campaign=Hotel%20-%20Taiwan&utm_medium=cpc&utm_source=bing&utm_term=ZDW6D9wJxGgeUmQhGSLNTg&msclkid=9f84d0810bcf194920f9b9c914126f46")

        driver.find_element(By.LINK_TEXT(),"Create your account").click()

        time.sleep(40)
        driver.quit()

demoLink = demobyLinkText()
demoLink.demoByLinkText()
