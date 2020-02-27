'''
    The full right of this code is on Jisoo Kim
    This project is to get special code after survey of burgerking
'''
#2020_02_07 //request test
from selenium import webdriver

url = "http://kor.tellburgerking.com"
chrome_driver_path = "./chromedriver.exe"

#get chrome_browser object
chrome_browser = webdriver.Chrome(chrome_driver_path)
chrome_browser.get(url)

#get button by name
next_btn = chrome_browser.find_element_by_name("NextButton")
next_btn.submit()
