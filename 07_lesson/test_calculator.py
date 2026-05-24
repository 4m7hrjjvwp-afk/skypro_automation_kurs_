from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import СalculatorPage


def test_calculator():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    calculator = СalculatorPage(driver)
    calculator.input_delay("45")
    calculator.click_button()
    result = calculator.get_result()
    assert result == "15"

    calculator.driver.quit()
