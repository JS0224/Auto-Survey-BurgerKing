'''
    The full right of this code is on Jisoo Kim
    This project is to get special code after survey of burgerking
'''
#2020_02_07 //request test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://kor.tellburgerking.com"
chrome_driver_path = "./chromedriver.exe"

#get chrome_browser object
chrome_browser = webdriver.Chrome(chrome_driver_path)
chrome_browser.get(url)

def clickNextButton():
    next_btn = chrome_browser.find_element_by_id("NextButton")
    next_btn.submit()


#####PAGE1 - Start!
#get button by name
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

#####PAGE7
radio_input = chrome_browser.find_element_by_class_name("radioSimpleInput")
radio_input.click()
clickNextButton()

def clickSeveralInPage():
    radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
    for i,v in enumerate(radio_inputs):
        if i % 5 == 0:
            radio_inputs[i].click()
    clickNextButton()

####PAGE8,9,10
clickSeveralInPage()
clickSeveralInPage()
clickSeveralInPage()

####PAGE11
radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
radio_inputs[0].click()
radio_inputs[11].click()
clickNextButton()

####PAGE12
radio_inputs = chrome_browser.find_elements_by_class_name("radioSimpleInput")
radio_inputs[1].click()
clickNextButton()

####PAGE13,14
clickSeveralInPage()
clickNextButton()
