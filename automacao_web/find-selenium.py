from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

#driver.get("https://estivalet.github.io/robot-static-testing-site/")
# driver.get("https://estivalet.github.io/robot-static-testing-site/cadastro/index.html")
driver.get("https://estivalet.github.io/robot-static-testing-site/admin/index.html")

# username = driver.find_element(By.ID, "username")
# username.send_keys("allan")
# driver.implicitly_wait(0.5)
# password = driver.find_element(By.ID, "password")
# username.send_keys("senha")
# driver.implicitly_wait(0.5)

# login_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[3]/div/a")
# login_button.click()

# element = driver.find_element(By.LINK_TEXT, "Desenvolvido para o curso de automação com Robot Framework")
element = driver.find_element(By.CSS_SELECTOR, "div.card-body > p")
driver.implicitly_wait(0.5)
print(element.text)
# time.sleep(3)
driver.close()