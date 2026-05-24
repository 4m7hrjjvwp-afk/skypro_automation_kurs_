from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анна")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Граевская")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("603147")

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
