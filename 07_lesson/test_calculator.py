from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage


def test_calculator():
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    calculator = CalculatorPage(driver)
    calculator.input_delay("45")
    calculator.click_button()
    result = calculator.get_result()
    assert result == "15"
    driver.quit()
