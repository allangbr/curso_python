from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://estivalet.github.io/robot-static-testing-site/cadastro/index.html")

select_element = driver.find_element(By.ID, "estado-civil")
select_object = Select(select_element)
# all_available_options = select_object.options

# for option in all_available_options:
#   print(option.text)
select_object.select_by_value("Casado(a)")
time.sleep(3)

driver.close()