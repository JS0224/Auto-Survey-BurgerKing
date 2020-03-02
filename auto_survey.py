'''
    The full right of this code is on Jisoo Kim
    This project is to get special code after survey of burgerking
'''
#import library and variable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from question_data import question_type

#set url, path
url = "http://kor.tellburgerking.com"
chrome_driver_path = "./chromedriver.exe"

#get chrome_browser object
chrome_browser = webdriver.Chrome(chrome_driver_path)
chrome_browser.get(url)

#user code
__code = "8219480100371132"

#split serial number into Code
def splitNumInCode(serial_num):
    #serial_num is string type
    code = []
    num =""
    for i,v in enumerate(serial_num):
        num = num + v
        if((i+1) % 3 is 0):
            code.append(num)
            num = ""
    code.append(num)
    return code

#click next button
def clickNextButton():
    next_btn = chrome_browser.find_element_by_id("NextButton")
    next_btn.submit()

#click option in irrelevant options
def clickOption():
    radio_input = chrome_browser.find_element_by_class_name("radioButtonHolder")
    radio_input.click()
    clickNextButton()

#click qulity in options(best option only)
def clickQuality():
    radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
    for i,v in enumerate(radio_inputs):
        if i % 5 == 0:
            radio_inputs[i].click()
    clickNextButton()

#customized answer for qulity question
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
        if i == 1: #Input Code
            code = splitNumInCode(__code)
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
        elif i == 23: #Dropbox
            select = Select(chrome_browser.find_element_by_id('R069000'))
            select.select_by_index(3)
            select = Select(chrome_browser.find_element_by_id('R070000'))
            select.select_by_index(6)
            clickNextButton()
        elif i == 25: #Get final code
            code = chrome_browser.find_element_by_class_name("ValCode")
            print(code.text)
