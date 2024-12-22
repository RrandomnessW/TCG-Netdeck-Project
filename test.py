from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

lService = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=lService)

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "input"))
)
print('hello\n')

input_element = driver.find_element(By.CLASS_NAME, 'input')
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

# art = driver.find_elements(By.XPATH, "//article[@class='index__contentBlock__7vKo-']")
# driver.get('https://www.kununu.com/de/volkswagen/kommentare/100')
# print([my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[starts-with(@class, 'index__ratingBlock')]//span[starts-with(@class, 'index__score__')]")))])
time.sleep(2)
driver.quit()