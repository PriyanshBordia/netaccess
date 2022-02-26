#!/usr/bin/env python3

'''
Author: jeeva2812, 
'''

#Change this
rollNo = '[username]'
pwd = '[password]'

import selenium
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--headless") #Remove this to see the process
driver = selenium.webdriver.Chrome(options=chrome_options)

driver.get('http://172.2.2.6/connect')

rollNo_box = driver.find_element(By.ID, 'username')
rollNo_box.send_keys(rollNo)

pwd_box = driver.find_element(By.ID, 'password')
pwd_box.send_keys(pwd)

login_button = driver.find_element(By.ID, 'submit')
login_button.click()

driver.get('http://172.2.2.6/connect')

oneDay = driver.find_element(By.ID, 'radios-1')
oneDay.click()

approve_button = driver.find_element(By.ID, 'approveBtn')
approve_button.click()

#print("Successfully authenticated")
