from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        password_field = self.driver.find_element(By.CSS_SELECTOR, '#password')

        username_field.send_keys(username)
        password_field.send_keys(password)

    def login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, '#login-button')
        login_button.click()
