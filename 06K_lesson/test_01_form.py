from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_fill_form():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    wait = WebDriverWait(driver, 5)

    zip_code_field = driver.find_element(By.NAME, "zip-code")
    wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    assert "alert-danger" in zip_code_field.get_attribute("class")
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]

    for field_name in fields:
        field = driver.find_element(By.NAME, field_name)
        assert "alert-success" in field.get_attribute("class")

    driver.quit()
