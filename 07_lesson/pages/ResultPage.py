from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def total_amount(self, driver):
        total_amount = self.driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
        print(total_amount)
        WebDriverWait(driver, 15)

    def click_finish(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="finish"]').click()
