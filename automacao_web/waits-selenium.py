from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
# driver.get("https://estivalet.github.io/robot-static-testing-site/cadastro/index.html")

# select_element = driver.find_element(By.ID, 'cep').send_keys('93330-000')
# search_button = driver.find_element(By.XPATH, '//button[.="Pesquisar"]').click()
# # driver.implicitly_wait(2)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.text_to_be_present_in_element_attribute((By.ID, 'rua'), 'value', 'Rua São Leopoldo'))
# street = street_element = driver.find_element(By.ID, 'rua').get_attribute('value')
# print(street)

# driver.get("https://estivalet.github.io/static-testing-sites/simple/dynload.html")
# select_element = driver.find_element(By.XPATH, '//button[.="Start 1"]').click()
# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
# print("execução continuada")

# driver.get("https://estivalet.github.io/static-testing-sites/simple/dynload.html")
# select_element = driver.find_element(By.XPATH, '//button[.="Start 2"]').click()
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, '//p[.="Hello Dynamic Element Created!"]')))
# print("execução continuada")

driver.get("https://estivalet.github.io/static-testing-sites/simple/dynload.html")
select_element = driver.find_element(By.XPATH, '//button[.="Enable"]').click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//form[@id="input-example"]/input')))
print("execução continuada")

driver.close()