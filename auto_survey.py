'''
    The full right of this code is on Jisoo Kim
    This project is to get special code after survey of burgerking
'''
#2020_02_07 //request test

import urllib.request as req

url = "http://www.postech.ac.kr"
def request(url):
    response = req.urlopen(url) #object
    byte_data = response.read() #binary
    text_data = byte_data.decode('utf-8') #text
    return text_data

#=========== print contents of url =============
#print(request(url))
