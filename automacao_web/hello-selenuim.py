from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
assert "Google" in driver.title
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
driver.implicitly_wait(0.5)

button_search = driver.find_element(By.NAME, "btnK")
button_search.click()

time.sleep(5)
driver.quit()
