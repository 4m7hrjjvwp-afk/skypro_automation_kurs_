from selenium.webdriver.common.by import By


class LoginPage:
    """Класс для взаимодействия со страницей авторизации.
     Реализует паттерн проектирования Page Object для ввода учетных данных пользователя 
     и выполнения входа в систему.
    """
    def __init__(self, driver):
        """Инициализирует класс страницы авторизации.
        Args:
        driver: экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def login(self, username, password):
        """Вводит имя пользователя и пароль.
        Args:
        username:  имя пользователя (логин) для авторизации
        password: пароль для авторизации.
        """
        #Поиск и заполнение поля "Имя пользователя"
        username_field = self.driver.find_element(By.CSS_SELECTOR,
                                                  '#user-name')
        username_field.send_keys(username)

        #Поиск и заполнение поля "Пароль"
        password_field = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password_field.send_keys(password)

    def login_button(self):
        """Находит и нажимает кнопку 'Login' для отправки формы авторизации."""
        login_button = self.driver.find_element(By.CSS_SELECTOR,
                                                '#login-button')
        login_button.click()
