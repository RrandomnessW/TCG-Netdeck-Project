# Code to check only 1 page on 401 games for single card products only

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

import card

driver = webdriver.Firefox()
single1 = card.Card(driver,1,'Teal Mask Ogerpon ex')
single2 = card.Card(driver,1,'Charizard ex')
single3 = card.Card(driver,1,'Irida')
single4 = card.Card(driver,1,'Frosmoth')
single1.scrape_single_page()
single2.scrape_single_page()
single3.scrape_single_page()
single4.scrape_single_page()

driver.close()
driver.quit()