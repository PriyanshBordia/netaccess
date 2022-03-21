#!/usr/bin/env python3

'''
Author: PriyanshBordia
'''

# Credentials
rollNo = '[rollNo]'
pwd = '[password]'

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from termcolor import cprint 

PATH = "/Users/priyansh/Desktop/GitHub/netaccess/chromedriver"

service = Service(PATH)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get("https://172.22.2.6/connect/PortalMain")

try:
	security_check = driver.find_element(By.ID, 'details-button')
	cprint(security_check.text, "red")
	security_check.click()
	security_check = driver.find_element(By.ID, 'proceed-link')
	cprint(security_check.text, "white")
	security_check.click()
	username_box = driver.find_element(By.ID, 'LoginUserPassword_auth_username')
	print(username_box.text)
	username_box.send_keys(rollNo)
	pwd_box = driver.find_element(By.ID, 'LoginUserPassword_auth_password')
	pwd_box.send_keys(pwd)
	login_button = driver.find_element(By.ID, 'UserCheck_Login_Button_span')
	login_button.click()
	print("Successfully authenticated.!!")
except Exception as e:
	raise e
finally:
	driver.quit()
