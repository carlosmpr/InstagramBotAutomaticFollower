import os
import time

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user = ""
username = ""
password = ""
url = "https://www.instagram.com/"
chrome_driver_path = "path to web driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)
enter_username = WebDriverWait(driver, 5).until(
    expected_conditions.presence_of_element_located((By.NAME, 'username')))

enter_username.send_keys(username)

enter_password = WebDriverWait(driver, 20).until(
    expected_conditions.presence_of_element_located((By.NAME, 'password')))

enter_password.send_keys(password)
enter_password.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element_by_xpath( '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)

ui.WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]').click()
time.sleep(3)
