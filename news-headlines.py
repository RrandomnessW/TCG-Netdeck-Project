from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





website = "http://www.thesun.co.uk/sport/football"
# r means raw string literal
# path = r"chromedriver.exe"

# lService = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=lService)

# headless-mode
options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)
driver.get(website)

# if there's no activity in the driver, it will automatically quit

# time.sleep(10)
# find_elements returns ALL elements w/ that xpath
containers = driver.find_elements(By.XPATH, value='//div[@class="teaser__copy-container"]')
# iterate through the list 'containers' ^^^

# print(containers)

# lists:
titles = []
subtitles = []
links = []

for container in containers:
    # https://stackoverflow.com/questions/49031553/getting-the-xpath-of-a-span-web-element     <- life saving website
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, './/a/span'))
    # )
    title = container.find_element(By.XPATH, './/a/span').text
    subtitle = container.find_element(By.XPATH, value='.//a/h3').text
    link =  container.find_element(By.XPATH, value='.//a').get_attribute("href")
    # add elements to the lists
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

print(titles)

# dataframe method to export data to csv
my_dict = {'title':titles, 'subtitle':subtitles, 'link':links} # dictionary - includes key and value
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headlines-headless.csv')



driver.quit()