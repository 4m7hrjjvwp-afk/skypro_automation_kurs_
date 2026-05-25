from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def input_delay(self, value):
        input_delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear()
        input_delay.send_keys(value)

    def click_button(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self):
        waiter = WebDriverWait(self.driver, 55)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
