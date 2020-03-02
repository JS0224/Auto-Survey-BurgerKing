'''
    The full right of this code is on Jisoo Kim
    This project is to get special code after survey of burgerking
'''
#2020_02_07 //request test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from question_data import question_type

url = "http://kor.tellburgerking.com"
chrome_driver_path = "./chromedriver.exe"

#get chrome_browser object
chrome_browser = webdriver.Chrome(chrome_driver_path)
chrome_browser.get(url)

def clickNextButton():
    next_btn = chrome_browser.find_element_by_id("NextButton")
    next_btn.submit()

def clickOption():
    radio_input = chrome_browser.find_element_by_class_name("radioButtonHolder")
    radio_input.click()
    clickNextButton()

def clickQuality():
    radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
    for i,v in enumerate(radio_inputs):
        if i % 5 == 0:
            radio_inputs[i].click()
    clickNextButton()

def clickQualityCustomized(customize_class,customize_question_list):
    inputs = chrome_browser.find_elements_by_class_name(customize_class)
    for question in customize_question_list:
        inputs[question].click()
    clickNextButton()

for i,type in enumerate(question_type):
    if type == 0:
        clickNextButton()
    elif type == 1:
        clickOption()
    elif type == 2:
        clickQuality()
    elif type == 3:
        if i == 1:
            code = ["821","948","010","037","113","2"]
            for i,v in enumerate(code):
                name = "CN" + str(i+1)
                cn = chrome_browser.find_element_by_name(name).send_keys(v)
            clickNextButton()
        elif i == 9:
            clickQualityCustomized("radioSimpleInput",[0,-1])
        elif i == 10:
            clickQualityCustomized("radioSimpleInput",[-1])
        elif i == 13:
            clickQualityCustomized("checkboxSimpleInput",[0])
        elif i == 14:
            clickQualityCustomized("checkboxSimpleInput",[-1])
        elif i == 23:
            select = Select(chrome_browser.find_element_by_id('R069000'))
            select.select_by_index(3)
            select = Select(chrome_browser.find_element_by_id('R070000'))
            select.select_by_index(6)
            clickNextButton()
        elif i == 25:
            code = chrome_browser.find_element_by_class_name("ValCode")
            print(code.text)
