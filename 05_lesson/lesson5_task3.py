from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("12345")

sleep(5)

input_field.clear()

input_field.send_keys("54321")

sleep(5)

driver.quit()