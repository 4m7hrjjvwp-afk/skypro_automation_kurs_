from selenium.webdriver.common.by import By


class CartPage:
    """ Класс для взаимодействия со страницей корзины интернет-магазина.
     Реализует паттерн проектирования Page Object. 
    """
    def __init__(self, driver):
        """Инициализирует класс корзины.
        Args:
        driver: экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def go_to_cart(self):
        """Переходит на страницу корзины, кликая по иконке корзины.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    def proceed_to_checkout(self):
        """Нажимает кнопку перехода к оформлению заказа."""
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
