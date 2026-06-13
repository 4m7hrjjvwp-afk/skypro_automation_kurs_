import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage

@allure.title("Тестирование калькулятора")
@allure.description("Проверка работы калькулятора с задержкой")
@allure.feature("Вычисление с задрежкой")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    """Тест проверяет корректность арифметического расчета на калькуляторе с задержкой"""

    with allure.step("Инициализация и запуск браузера Chrome"):
        chrome_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
    with allure.step("Открытие страницы калькулятора"):    
        driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Увеличение окна до полного размера экрана"):    
        driver.maximize_window()
    
        calculator = CalculatorPage(driver)

        with allure.step("Установка задержки вычислений на 45 секунд"):
            calculator.input_delay("45")
        with allure.step("Нажатие на кнопку выполнения операции"):
            calculator.click_button()
        with allure.step("Ожидание и получение итогового результата"):
            result = calculator.get_result()
     
        with allure.step("Проверка: ожидаемый результат равен '15'"):
            assert result == "15"
    
        with allure.step("Закрытие браузера и очистка сессии"):
            driver.quit()
