# This script will scrape and dump pokemon set abbrievations into a csv file.
# for website https://pkmncards.com/sets/
# //a[contains(@href, "https://pkmncards.com/set/")]
# write it to a file.

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os;

website = 'https://pkmncards.com/sets/'

# headless-mode
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox() # to launch without headless

driver.get(website) 

# Find all sets and their abbrievations using the xpath
containers = driver.find_elements(By.XPATH, value='//a[contains(@href, "https://pkmncards.com/set/")]')

# Removed faulty entries at the start
print("Removed these two entries as they are faulty")
print(containers[0].text)
print(containers[1].text)
sets = containers[2:]

set_title = []
set_abbrv = []

# Loop through each html element in text form and store them into the lists above.
for set in sets:
    
    # check if text from html only contains a set title.
    if " (" not in set.text:
        set_title.append(set.text)
        set_abbrv.append("")
    else:
        names = set.text.split(" (")
        set_title.append(names[0])
        # remove the last character of the abbrv. A list of char, with the last character removed.
        names[1] = names[1][:-1]
        set_abbrv.append(names[1])
    # print(set.text)

# print(set_title)
# print(set_abbrv)

# Create a csv file for the set names and abbrievations
my_dict = {'Abbreviation':set_abbrv, 'Set_Title':set_title}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv(os.getcwd()+r'/Pokemon_Set_Abbreviations.csv')

driver.close()
driver.quit()