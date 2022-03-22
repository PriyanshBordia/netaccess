#!/usr/bin/env python3

'''
Author: PriyanshBordia
'''

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from termcolor import cprint 


# Credentials
rollNo = os.getenv('NETACCESS_USERNAME')
pwd = os.getenv('NETACCESS_PASSWORD')

PATH = "/Users/priyansh/Desktop/GitHub/netaccess/chromedriver"

service = Service(PATH)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get("https://172.22.2.6/connect/PortalMain")

try:
	security_check = driver.find_element(By.ID, 'details-button')
	security_check.click()
	security_check = driver.find_element(By.ID, 'proceed-link')
	security_check.click()
	sleep(.1)
	username_box = driver.find_element(By.ID, 'LoginUserPassword_auth_username')
	username_box.send_keys(rollNo)
	pwd_box = driver.find_element(By.ID, 'LoginUserPassword_auth_password')
	pwd_box.send_keys(pwd)
	login_button = driver.find_element(By.ID, 'UserCheck_Login_Button_span')
	login_button.click()
	cprint("Successfully authenticated.!!", "white")
except Exception as e:
	raise e
finally:
	driver.quit()
