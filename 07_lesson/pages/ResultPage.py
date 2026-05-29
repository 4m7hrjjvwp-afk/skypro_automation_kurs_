from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total(self):
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         'div[data-test="total-label"]').text
        return total

    def click_finish(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'a[data-test="finish"]').click()
