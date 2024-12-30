from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import pandas as pd
import time

website = 'https://bulbapedia.bulbagarden.net/wiki/Main_Page'

# headless-mode
options = Options()
options.add_argument("-headless")
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox() # to launch without headless

driver.get(website)

search_bar = driver.find_element(By.XPATH, value='//input[@id="searchInput"]')
search_bar.clear()
search_bar.send_keys("Frosmoth (TCG)")
search_bar.send_keys(Keys.RETURN)

time.sleep(2)


search_bar = driver.find_element(By.XPATH, value='//input[@id="searchInput"]')
search_bar.clear()
search_bar.send_keys("Pikachu (TCG)")
search_bar.send_keys(Keys.RETURN)

time.sleep(2)

# you can change websites on the spot here.
website = 'https://pkmncards.com/sets/'
driver.get(website)

time.sleep(2)

driver.close()
driver.quit()

# read the card abbrievation