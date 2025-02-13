from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import os
from selenium.common.exceptions import NoSuchElementException

class Card:
    # TCG
    # name
    # driver
    
    shdw_wait_const = 0.3

    website = r'https://store.401games.ca/pages/search-results?q='
    filter_401_min_max = r'&sort=price_min_to_max'
    filter_401_pkmn_sngl = r'Category,Pokemon+Singles'
    filter_401_in_stock = r'In+Stock,True'
    # filter_401 = r'&filters=' + filter_401_in_stock + ',' + filter_401_pkmn_sngl
    filter_401 = r'&filters=' + filter_401_pkmn_sngl

    def __init__(self, driver, TCG, card_name):
        self.driver = driver
        self.TCG = TCG                  # TCG type
        self.card_name = card_name
        
        self.card_title = []
        self.card_price = []
        self.card_set = []
        self.card_link = []
        
        pass # used as 'empty code'

    # argument passed to a function is assigned to a new local variable within the function
    # returns shadow root
    def get_shadow_root(self, element):
        return self.driver.execute_script('return arguments[0].shadowRoot', element)

    # clicks a button in a shadow root
    # Unused for now.
    def shdw_rt_click_btn(self, element):
        self.driver.execute_script('arguments[0].click();',element)

    # code to scrape card data on 1 single 401games page. 
    def scrape_single_page(self):
        self.driver.get(self.website + self.card_name + self.filter_401)
        
        # wait until website has finished loading
        self.driver.implicitly_wait(10) # sets implicit wait time when searching for elements to 10 s
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

        # Find the shadow host and shadow root.
        shadow_host = self.driver.find_element(By.XPATH, value='//div[@id="fast-simon-serp-app"]')
        shadow_root = self.get_shadow_root(shadow_host)

        time.sleep(self.shdw_wait_const)

        # find elements for div class*=checkbox
        # look through and check if the attribute Pokemon Singles exists
        # if not, click on show more
        # check again
        # done so cause if there is no show more and the attribute is visible right away, trying to find the show more could crash the program.
        # make sure things have loaded before taking the html data

        product_list = shadow_root.find_elements(By.CSS_SELECTOR, value='div[class*="product-card-items-wrapper"]')
        for product in product_list:
            print(product.text) # debug text
            # so not all cards will have the name in the text, thus selenium will break !!
            # I think when we encounter a card that doesn't contain that name, we break the loop
            # also case sensitive so if the card name is 'Charizard ex' is different from 'Charizard EX'

            try: 
                self.card_title.append(product.find_element(By.CSS_SELECTOR, value='span[aria-label*="'+self.card_name+'"]').text)
            except NoSuchElementException as e:
                print('No more cards with the name found')
                break

            self.card_price.append(product.find_element(By.CSS_SELECTOR, value='div[aria-label*="regular price:"]').text)
            self.card_set.append(product.find_element(By.CSS_SELECTOR, value='div[class*="vendor"]').text)
            self.card_link.append(product.find_element(By.CSS_SELECTOR, value='a[href]').get_attribute('href'))

        # store cards on page into a csv file
        my_dict = {'Title':self.card_title, 'Set':self.card_set, 'Price':self.card_price, 'Link':self.card_link} 
        df_headlines = pd.DataFrame(my_dict)

        # os.getcwd() returns path that script is running from.
        # print(os.getcwd())
        df_headlines.to_csv(os.getcwd()+r'/card-list-' + self.card_name + r'.csv') # 'r' before a string tells interpreter to treat backslashes as literal character
        #Raging Bolt ex
        #Raging Bolt ex