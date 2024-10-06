import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
# TODO: make exams actually load
browser.get('https://intern.gymkirchenfeld.ch/myregister/')
# TODO: replace dirty way of pausing with webdriverwait
time.sleep(5)

user_field = browser.find_element(By.ID, 'i0116')
# TODO: make variables for username and password
user_field.send_keys('nikolaj.veljkovic@mygymer.ch')
user_field.send_keys(Keys.RETURN)

time.sleep(3)
pwd_field = browser.find_element(By.ID, 'i0118')
pwd_field.send_keys('W1rs1ndd0ch4lle')
pwd_field.send_keys(Keys.RETURN)