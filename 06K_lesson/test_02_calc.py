from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    text_input.clear()
    text_input.send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    WebDriverWait(driver, 55).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
    WebDriverWait(driver, 55).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
    driver.quit()