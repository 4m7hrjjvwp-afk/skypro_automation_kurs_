from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.ResultPage import ResultPage


def test_shop():
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')
    login_page.login_button()
    main_page = MainPage(driver)
    main_page.add_product_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form()
    checkout_page.click_continue()
    result_page = ResultPage(driver)
    result_page.total_amount()
    result_page.click_finish()
    driver.quit()
