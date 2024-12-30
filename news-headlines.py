from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

website = "http://www.thesun.co.uk/sport/football"
# r means raw string literal
# path = r"chromedriver.exe"

# lService = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=lService)

# headless-mode
options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()

driver.get(website)

# if there's no activity in the driver, it will automatically quit

# find_elements returns ALL elements w/ that xpath
containers = driver.find_elements(By.XPATH, value='//div[@class="teaser__copy-container"]')
# iterate through the list 'containers' ^^^

print(containers)

# lists:
titles = []
subtitles = []
links = []

print('\n\n'+ containers[0].get_attribute('outerHTML') + '\n')
print(containers[0].find_element(By.XPATH, value='./a/span').text + '\n')
print(containers[1].find_element(By.XPATH, value='./a/span').text + '\n')

#  handle cases where the structure deviates (e.g., a <span> instead of an <a> tag). Issue occured because div class="teaser ... was followed by a span tag instead of an a tag. 
# It also does not appear on the website and is a ghost article. Good thing this was found, now I know how to deal with it. Doing XPATH './/a/span' also doesn't seem to bypass issue.
# Maybe just put in a try catch statement?

containsBool = True

for container in containers:
    # https://stackoverflow.com/questions/49031553/getting-the-xpath-of-a-span-web-element     <- life saving website
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, './/a'))
    # )
    print('\n' + container.get_attribute('outerHTML') + '\n')

    # Check if the a tag exists for current container object
    a_elements = container.find_elements(By.XPATH, './a')
    # if the returned list is non-empty. AKA if there exists a sequential a tag
    if a_elements: 
        title = container.find_element(By.XPATH, value='.//a/span').text
        subtitle = container.find_element(By.XPATH, value='.//a/h3').text
        link =  container.find_element(By.XPATH, value='.//a').get_attribute("href")
        # add elements to the lists
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
    else:
        print('No a element')
    
    
print('loop finished')
print(titles)

# dataframe method to export data to csv
my_dict = {'title':titles, 'subtitle':subtitles, 'link':links} # dictionary - includes key and value
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv(os.getcwd()+r'/headlines-headless.csv')

driver.close()
driver.quit()