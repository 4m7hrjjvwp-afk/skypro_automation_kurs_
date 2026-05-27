from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        backpack = self.driver.find_element(By.CSS_SELECTOR,
                                            "#add-to-cart-sauce-labs-backpack")
        backpack.click()
        t_shirt = self.driver.find_element(By.CSS_SELECTOR,
                                           "#add-to-cart-sauce-labs-bolt-t"
                                           "-shirt")
        t_shirt.click()
        onesie = self.driver.find_element(By.CSS_SELECTOR,
                                          "#add-to-cart-sauce-labs-onesie")
        onesie.click()
