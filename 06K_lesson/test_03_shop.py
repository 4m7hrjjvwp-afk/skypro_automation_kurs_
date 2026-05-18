from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    fields = ['button[name="add-to-cart-sauce-labs-backpack"]',
              'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]',
              'button[name="add-to-cart-sauce-labs-onesie"]']
    for locator in fields:
        field = driver.find_element(By.CSS_SELECTOR, locator)
        field.click()

    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анна")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Граевская")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("603147")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]')

    total = driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
    WebDriverWait(driver, 15)
    assert total == "$58,29"

    print(total)

    driver.quit()
