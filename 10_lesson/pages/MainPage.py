from selenium.webdriver.common.by import By


class MainPage:
    """Класс для взаимодействия с главной страницей каталога интернет-магазина.
     Реализует паттерн проектирования Page Object для выбора товаров и добавления их в корзину.
    """
    def __init__(self, driver):
        """Инициализирует класс главной страницы каталога интернет-магазина.
        Args:
        driver: экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def add_product_to_cart(self):
        """Добавляет товары в корзину."""
        #Поиск и добавление в корзину рюкзака
        backpack = self.driver.find_element(By.CSS_SELECTOR,
                                            "#add-to-cart-sauce-labs-backpack")
        backpack.click()
        #Поиск и добавление в корзину футболки
        t_shirt = self.driver.find_element(By.CSS_SELECTOR,
                                           "#add-to-cart-sauce-labs-bolt-t"
                                           "-shirt")
        t_shirt.click()
        #Поиск и добавление в корзину комбинезона
        onesie = self.driver.find_element(By.CSS_SELECTOR,
                                          "#add-to-cart-sauce-labs-onesie")
        onesie.click()
