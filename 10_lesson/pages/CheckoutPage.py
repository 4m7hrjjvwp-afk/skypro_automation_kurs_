from selenium.webdriver.common.by import By


class CheckoutPage:
    """ Класс для взаимодействия со страницей оформления заказа.
     Реализует паттерн проектирования Page Object для ввода персональных данных
     и навигации на этапе оформления заказа."""
    def __init__(self, driver):
        """Инициализирует класс страницы оформления заказа.
        Ards:
        driver: экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def fill_form(self):
        """Заполняет форму персональных данных для оформления заказа.
        Args:
        first_name: имя покупателя
        last_name: фамилия покупателя
        postal_code: почтовый индекс
        """
        #Заполнение поля "Имя"
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(
            "Анна")
        #Заполнение поля "Фамилия"
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(
            "Граевская")
        #Заполнение поля "Почтовый индекс"
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(
            "603147")

    def click_continue(self):
        """Нажимает на кнопку 'Continue' для перехода к следующему шагу."""
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
