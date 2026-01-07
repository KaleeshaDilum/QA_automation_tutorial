from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium .webdriver.support.select import Select

class dropDownExam:
    def exam(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.mobiscroll.com/select/multiple-select")
        time.sleep(6)
        driver.maximize_window()

        saveDropDown=driver.find_element(By.ID,"my-input")
        clickDropDown=Select(saveDropDown)
        clickDropDown.select_by_index(1)
        clickDropDown.select_by_index(2)
        time.sleep(2)
        selected = clickDropDown.first_selected_option
        print("name:", selected.text)
        print("Value:",selected.get_attribute("value"))

obj1 = dropDownExam()
obj1.exam()

#code is not working