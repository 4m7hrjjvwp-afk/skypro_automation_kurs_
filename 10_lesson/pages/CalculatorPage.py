from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """ Класс для взаимодействия со страницей онлайн-калькулятора.
    Использует паттерн проектирования Page Object.
    """
    def __init__(self, driver):
        """Инициализирует класс калькулятора.
        :param driver: экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def input_delay(self, value):
        """
        Вводит значение задержки выполнения операций в секундах.
        :param value: Время задержки.
        """
        #Поиск поля ввода по CSS-селектору #delay
        input_delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear() #очистка поля перед вводом
        input_delay.send_keys(value)# ввод значения

    def click_button(self):
        """
        Последовательно нажимает кнопки на калькуляторе для ввода выражения: '7 + 8 ='. 
        """
        #Поиск и клик по кнопкам с помощью ХРАТН по тексту на элементах
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self):
        """
        Ожидает появление результата вычисления на экране и возвращает его.
        Метод ждет до 55 секунд, пока в элементе экрана не появится текст '15'.
        :return: Текст с результатом вычисления (строка).
        """
        #Инициализация явного ожидания (WebDriverWait) до 55 секунд
        waiter = WebDriverWait(self.driver, 55)

        #Ожидание появления в элементе с классом .screen текста "15"
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        
        #Получение финального текста из элемента экрана
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result