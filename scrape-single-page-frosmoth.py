# Code to check only 1 page on 401 games for card products only

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def get_shadow_root(element):
    return driver.execute_script('return arguments[0].shadowRoot', element)

def shdw_rt_click_btn(element):
    driver.execute_script('arguments[0].click();',element)

website = 'https://store.401games.ca/pages/search-results?q=frosmoth'

# headless-mode
options = Options()
options.add_argument("-headless")
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()

driver.get(website) 

# wait until website has finished loading
WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

# Find the shadow host and shadow root.
shadow_host = driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
shadow_root = get_shadow_root(shadow_host)

# From shadowroot, find the sort min to max button and click it.
sort_product_btn = shadow_root.find_element(By.CSS_SELECTOR, value='span[data-value="price_min_to_max"]')
shdw_rt_click_btn(sort_product_btn)
# wait until the html page is fully loaded
WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

# print('done waiting')

# refresh your information because your elements become stale after the website has changed
shadow_host = driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
shadow_root = get_shadow_root(shadow_host)

product_list = shadow_root.find_elements(By.CSS_SELECTOR, value='div[class*="product-card-items-wrapper"]')

thing = 'Frosmoth'
card_title = []
card_price = []
card_set = []
card_link = []

# store name, price, set, and link of a single card to different lists
for product in product_list:
    card_title.append(product.find_element(By.CSS_SELECTOR, value='span[aria-label*='+thing+']').text)
    card_price.append(product.find_element(By.CSS_SELECTOR, value='div[aria-label*="regular price:"]').text)
    card_set.append(product.find_element(By.CSS_SELECTOR, value='div[class*="vendor"]').text)
    card_link.append(product.find_element(By.CSS_SELECTOR, value='a[href]').get_attribute('href'))

# store cards on page into a csv file

my_dict = {'Title':card_title, 'Set':card_set, 'Price':card_price, 'Link':card_link} 
df_headlines = pd.DataFrame(my_dict)

# os.getcwd() returns path that script is running from.
df_headlines.to_csv(os.getcwd()+r'/card-list-test.csv') # 'r' before a string tells interpreter to treat backslashes as literal character

time.sleep(3)

driver.close()
driver.quit()

# coding to 

# name
# price
# set name