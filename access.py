#!/usr/bin/env python3

'''
Author: PriyanshBordia
'''

# Credentials
rollNo = '[rollNo]'
pwd = '[password]'

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

PATH = "/Users/priyansh/Desktop/GitHub/netaccess/chromedriver"

service = Service(PATH)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get("https://172.22.2.6/connect/PortalMain")

try:
	username_box = driver.find_element(By.ID, 'LoginUserPassword_auth_username')
	username_box.send_keys(rollNo)
	pwd_box = driver.find_element(By.ID, 'LoginUserPassword_auth_password')
	pwd_box.send_keys(pwd)
	login_button = driver.find_element(By.ID, 'UserCheck_Login_Button')
	login_button.click()
	print("Successfully authenticated.!!")
except Exception as e:
	raise e
finally:
	sleep(20)
	driver.quit()