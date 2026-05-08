from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
driver.maximize_window()
waiter = WebDriverWait(driver, 10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(EC.presence_of_element_located((By.ID, "landscape")))

search_src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(search_src)

driver.quit()