from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

#driver.get("https://estivalet.github.io/robot-static-testing-site/")
# driver.get("https://estivalet.github.io/robot-static-testing-site/cadastro/index.html")
driver.get("https://estivalet.github.io/robot-static-testing-site/admin/index.html")

elements = driver.find_elements(By.XPATH, '//li[@class="nav-item"]')
for element in elements:
  print(element.text)
# time.sleep(3)
driver.close()