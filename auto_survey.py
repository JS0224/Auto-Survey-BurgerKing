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

#####PAGE1 - Start!
#get button by name
next_btn = chrome_browser.find_element_by_name("NextButton")
next_btn.submit()

#####PAGE2 - Code typing
code = ["821","948","010","037","113","2"]
for i,v in enumerate(code):
    name = "CN" + str(i+1)
    cn = chrome_browser.find_element_by_name(name).send_keys(v)
