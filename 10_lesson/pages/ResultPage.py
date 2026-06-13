from selenium.webdriver.common.by import By


class ResultPage:
    """Класс для взаимодействия с финальной страницей заказа.
    Реализует паттерн проектирования Page Object для проверки итоговой суммы покупки 
    и завершения поцесса оформления заказа.
    """
    def __init__(self, driver):
        """Инициализирует класс финальной страницы заказа.
        Args:
        driver: экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def get_total(self):
        """Получает текстовое значение итоговой стоимости заказа.
        return: 
        str: строка с текстом итоговой суммы.
        """
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         'div[data-test="total-label"]').text
        return total

    def click_finish(self):
        """Находит и нажимает кнопку 'Finish' для окончательного подтверждения заказа."""
        self.driver.find_element(By.CSS_SELECTOR,
                                 'a[data-test="finish"]').click()
