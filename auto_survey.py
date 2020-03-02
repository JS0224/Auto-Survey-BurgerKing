'''
    The full right of this code is on Jisoo Kim
    This project is to get special code after survey of burgerking
'''
#2020_02_07 //request test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = "http://kor.tellburgerking.com"
chrome_driver_path = "./chromedriver.exe"

#get chrome_browser object
chrome_browser = webdriver.Chrome(chrome_driver_path)
chrome_browser.get(url)

def clickNextButton():
    next_btn = chrome_browser.find_element_by_id("NextButton")
    next_btn.submit()

#####PAGE1 - Start!
clickNextButton()

#####PAGE2 - Code typing
code = ["821","948","010","037","113","2"]
for i,v in enumerate(code):
    name = "CN" + str(i+1)
    cn = chrome_browser.find_element_by_name(name).send_keys(v)
clickNextButton()

def clickOneInPage():
    radio_input = chrome_browser.find_element_by_class_name("radioButtonHolder")
    radio_input.click()
    clickNextButton()

#####PAGE3,4,5
clickOneInPage()
clickOneInPage()
clickOneInPage()

#####PAGE6
radio_input = chrome_browser.find_element_by_class_name("radioSimpleInput")
radio_input.click()
clickNextButton()

def clickSeveralInPage():
    radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
    for i,v in enumerate(radio_inputs):
        if i % 5 == 0:
            radio_inputs[i].click()
    clickNextButton()

####PAGE 7,8,9
clickSeveralInPage()
clickSeveralInPage()
clickSeveralInPage()

####PAGE10
radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
radio_inputs[0].click()
radio_inputs[11].click()
clickNextButton()

####PAGE11
radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
radio_inputs[1].click()
clickNextButton()

####PAGE12,13
clickSeveralInPage()
clickNextButton()

####PAGE14
check_inputs = chrome_browser.find_elements_by_class_name("checkboxSimpleInput")
check_inputs[0].click()
clickNextButton()

####PAGE15
check_inputs = chrome_browser.find_elements_by_class_name("checkboxSimpleInput")
check_inputs[-1].click()
clickNextButton()

####PAGE 16,17,18,19,20
clickSeveralInPage()
clickSeveralInPage()
clickSeveralInPage()
clickSeveralInPage()
clickSeveralInPage()

####PAGE21,22,23
clickOneInPage()
clickOneInPage()
clickOneInPage()

####PAGE24,25
select = Select(chrome_browser.find_element_by_id('R069000'))
select.select_by_index(3)
select = Select(chrome_browser.find_element_by_id('R070000'))
select.select_by_index(6)
clickNextButton()
clickNextButton()

####Final page
code = chrome_browser.find_elements_by_class_name("ValCode")
print(code.text)
