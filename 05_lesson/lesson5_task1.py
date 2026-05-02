from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

sleep(5)
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()
driver.switch_to.alert.accept()
sleep(5)
driver.quit()
