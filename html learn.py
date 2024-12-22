import time
from bs4 import BeautifulSoup
import requests



# html_text = requests.get('https://store.401games.ca/pages/search-results?q=frosmoth&sort=price_min_to_max').text
# #print(html_text)

# soup = BeautifulSoup(html_text, 'lxml')
# products = soup.find_all('div', class_ = 'product-card fs-results-product-card fs-product-card fs-result-page-17x79ur product-card-border-hover fs-product-has-compare-price')
# print(products)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

browser = webdriver.Firefox()
browser.get('https://store.401games.ca/pages/search-results?q=frosmoth&sort=price_min_to_max')
try:
    # elem = browser.find_element(By.CLASS_NAME,'title-container fs-serp-product-title fs-result-page-mihllj')
    # elem = browser.find_element
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# next steps here:
# put on github, find out how to use ssh again!!
# for now, copy your files and new obsidian files created on here.
# observe xpath of pokemon cards.
# find and store cards to a list. Store quantity available. Store price
# learn how to click on cards (buttons) to check additional properties on 401 games
# learn