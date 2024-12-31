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

# wait until the element it finds is stale before refreshing the shadow_root
# driver: webdriver
# shadow_root: 
# val: string to find using CSS_SELECTOR
def wait_staleness_of(driver, shadow_root, val):
    WebDriverWait(driver, 5).until(
        EC.staleness_of(shadow_root.find_element(By.CSS_SELECTOR, value=val))
    )

# scrape this website too for Pokemon singles selection : https://store.401games.ca/pages/search-results?q=irida
# website = 'https://store.401games.ca/pages/search-results?q=frosmoth'
website = 'https://store.401games.ca/pages/search-results?q=irida'
filter_401 = r'&sort=price_min_to_max' #&filters=Category,Pokemon+Singles'
# add this at the end of the website search results page for 401games: &sort=price_min_to_max&filters=Category,Pokemon+Singles

# headless-mode
options = Options()
options.add_argument("-headless")
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()

driver.get(website + filter_401)
# driver.get(website)
# driver.implicitly_wait(10) # sets implicit wait time when searching for elements to 10 s

# wait until website has finished loading
WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

# Find the shadow host and shadow root.
shadow_host = driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
shadow_root = get_shadow_root(shadow_host)

# From shadowroot, find the sort min to max button and click it.
# sort_product_btn = shadow_root.find_element(By.CSS_SELECTOR, value='span[data-value="price_min_to_max"]')
# shdw_rt_click_btn(sort_product_btn)
# # wait until the html page is fully loaded
# WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
# # refresh your information because your elements become stale after the website has changed
# shadow_host = driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
# shadow_root = get_shadow_root(shadow_host)

category_list = shadow_root.find_elements(By.CSS_SELECTOR, value='div[class*="checkbox"]')
found = False

# see if the Pokemon Singles filter is visible
for category in category_list:
    if category.get_attribute('aria-label') == 'Pokemon Singles':
        found = True
        break
# if filter not visible, click on show more and get the 
if found == False:
    show_more_btn = shadow_root.find_element(By.CSS_SELECTOR, value='span[class*="show-more-button-text"]')
    shdw_rt_click_btn(show_more_btn)
    shadow_host = driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
    shadow_root = get_shadow_root(shadow_host)

pkmn_singles_btn = shadow_root.find_element(By.CSS_SELECTOR, value='span[aria-label*="Pokemon Singles"]') # click on span, not div
shdw_rt_click_btn(pkmn_singles_btn)

# wait until the element it finds is stale before refreshing the shadow_root
WebDriverWait(driver, 5).until(
    EC.staleness_of(shadow_root.find_element(By.CSS_SELECTOR, value='div[class*="product-card-items-wrapper"]'))
)

shadow_host = driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
shadow_root = get_shadow_root(shadow_host)


# find elements for div class*=checkbox
# look through and check if the attribute Pokemon Singles exists
# if not, click on show more
# check again
# done so cause if there is no show more and the attribute is visible right away, trying to find the show more could crash the program.

# thing = 'Frosmoth'
thing = 'Irida'
card_title = []
card_price = []
card_set = []
card_link = []

# make sure things have loaded before taking the html data

product_list = shadow_root.find_elements(By.CSS_SELECTOR, value='div[class*="product-card-items-wrapper"]')



# store name, price, set, and link of a single card to different lists
for product in product_list:
    print(product.text)
    card_title.append(product.find_element(By.CSS_SELECTOR, value='span[aria-label*='+thing+']').text)
    card_price.append(product.find_element(By.CSS_SELECTOR, value='div[aria-label*="regular price:"]').text)
    card_set.append(product.find_element(By.CSS_SELECTOR, value='div[class*="vendor"]').text)
    card_link.append(product.find_element(By.CSS_SELECTOR, value='a[href]').get_attribute('href'))

# store cards on page into a csv file
my_dict = {'Title':card_title, 'Set':card_set, 'Price':card_price, 'Link':card_link} 
df_headlines = pd.DataFrame(my_dict)

# os.getcwd() returns path that script is running from.
print(os.getcwd())
df_headlines.to_csv(os.getcwd()+r'/card-list-' + thing + r'.csv') # 'r' before a string tells interpreter to treat backslashes as literal character

time.sleep(3)

driver.close()
driver.quit()

# coding to 

# name
# price
# set name