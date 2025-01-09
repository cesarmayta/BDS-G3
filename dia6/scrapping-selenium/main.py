from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.sunat.gob.pe/")
    time.sleep(2)
    
    sell_rate = driver.find_element(By.ID,"sell-rate").text
    print(f'Tipo de cambio venta: {sell_rate}')
finally:
    driver.quit()