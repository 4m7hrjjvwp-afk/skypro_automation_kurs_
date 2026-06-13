import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.ResultPage import ResultPage

@allure.title("Тестирование интернет-магазин Swag Labs")
@allure.description("Проверка процесса оформления заказа в интернет-магазине")
@allure.feature("")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop():
    """Тест проверяет полный цикл покупки от авторизации до проверки итоговой суммы заказа.
    """
    with allure.step("Инициализация и запуск браузера Firefox"):
        service = Service()
        driver = webdriver.Firefox(service=service)

        with allure.step("Открытие страницы интрент-магазина"):
            driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        with allure.step("Авторизация пользователя в системе"):
            login_page.login('standard_user', 'secret_sauce')
            login_page.login_button()

        main_page = MainPage(driver)
        with allure.step("Добавление выбранных товаров в корзину"):
            main_page.add_product_to_cart()

        cart_page = CartPage(driver)
        with allure.step("Переход в корзину и инициация оформления"):
            cart_page.go_to_cart()
            cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(driver)
        with allure.step("Заполнение формы"):
            checkout_page.fill_form()
            checkout_page.click_continue()

        result_page = ResultPage(driver)
        with allure.step("Проверка итоговой суммы заказа"):
            total = result_page.get_total()
            assert total == "$58.29"

        with allure.step("Нажатие кнопки завершения заказа"):
            result_page.click_finish()

        with allure.step("Закрытие браузера и очистка сессии"):    
            driver.quit()
