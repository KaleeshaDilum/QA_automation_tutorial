from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium .webdriver.support.select import Select

class dropDownSingleSelct():

    def dropDownSingleSelct(self):
        driver = webdriver.Chrome()
        driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
        driver.maximize_window()

        dropdown=driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
        dropdownSelect = Select(dropdown)
        dropdownSelect.select_by_index(1)
        selected = dropdownSelect.first_selected_option
        print("Selected Text",selected.text)
        print("Value",selected.get_attribute("value"))

        time.sleep(5)
        dropdownSelect.select_by_value("ASM")
        selected1 = dropdownSelect.first_selected_option
        print("Selected Text",selected1.text)
        time.sleep(5)



result = dropDownSingleSelct()
result.dropDownSingleSelct()

