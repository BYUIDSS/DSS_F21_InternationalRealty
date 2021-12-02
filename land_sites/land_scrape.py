from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from time import sleep
from datetime import datetime

def lands_of_america(terms):
    image_file = "lands_of_america.png"
    
    # open webpage
    driver.get("https://www.landsofamerica.com/")

    # search terms
    driver.find_element_by_class_name('c2b08').click()
    search(terms)

    # wait for page to load
    sleep(1)

    driver.save_screenshot(image_file)

    return {'filename': image_file, 
            'date': datetime.now().strftime("%d %b %Y"), 
            'property': terms}

def land_watch(terms):
    image_file = "land_watch.png"

    # open webpage
    driver.get("https://www.landwatch.com/")

    # search terms
    driver.find_element_by_class_name('_3a9e8').click()
    search(terms)

    # wait for page to load
    sleep(1)

    driver.save_screenshot(image_file)

    return {'filename': image_file, 
            'date': datetime.now().strftime("%d %b %Y"),
            'property': terms}

def land_and_farm(terms):
    image_file = "land_and_farms.png"

        # open webpage
    driver.get("https://www.landandfarm.com/")

    # search terms
    driver.find_element_by_class_name('input-group add-on ui-front home-search-input-group').click()
    search(terms)

    # wait for page to load
    sleep(1)

    driver.save_screenshot(image_file)

    return {'filename': image_file, 
            'date': datetime.now().strftime("%d %b %Y"), 
            'property': terms}

def search(terms):
    driver.find_element_by_xpath("//input[@type='text']").send_keys(terms)
    driver.find_element_by_xpath("//input[@type='text']").send_keys(Keys.ENTER)

driver = webdriver.Chrome(ChromeDriverManager().install())
terms = "Idaho"

print(lands_of_america(terms))
print(land_watch(terms))
# print(land_and_farm(terms))

driver.close()