import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# NEW AS OF 12/1##########
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# And added scrape_homefinder function.

# Maxium seconds to wait for something to load.
MAX_DELAY = 5

def scrape_homes(terms):
    '''Searches homes.com for 'terms' and returns the filename of the screenshot of the result.
    Example terms: "737 Center Dr, Palo Alto, CA", "1975 Webster St, Palo Alto, CA"
    '''
    # Get the latest chrome driver
    driver  = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.homes.com/")
    driver.maximize_window()

    # The page has some code to auto-enter your location. Have to wait
    # for that to finish.
    class value_to_change(object):
        def __init__(self, locator, text):
            self.locator = locator
            self.text = text

        def __call__(self, driver):
            elem = ec._find_element(driver, self.locator)
            actual_text = elem.get_property("value")
            return actual_text != self.text
    _ = WebDriverWait(driver, MAX_DELAY).until(value_to_change((By.TAG_NAME, "input"), ""))

    # Looking for 1975 Webster St, Palo Alto, CA, which has a LISTING ID of LMKHZM
    # but that one's gone, so look for 737 Center Dr, Palo Alto, CA
    elem = driver.find_element_by_tag_name("input")
    elem.clear()
    elem.send_keys(terms)

    # It wants to load up possible addresses, so wait until it does that.
    _ = WebDriverWait(driver, MAX_DELAY).until(ec.visibility_of_element_located((By.ID, "listbox:0")))
    elem.send_keys(Keys.ENTER)

    # Wait for new page to load
    _ = WebDriverWait(driver, MAX_DELAY).until(ec.presence_of_element_located((By.XPATH, "//img[@class='block radius-6 full-size overflow-hidden']")))
    _ = WebDriverWait(driver, MAX_DELAY).until(ec.invisibility_of_element_located((By.XPATH, "//img[@class='site-loader radius-1/2']")))

    # Should have a page with the correct listing.
    now = datetime.now()
    filename = f"homes-dot-com_{now.year}-{now.month}-{now.day}.png"
    driver.save_screenshot(filename)
    driver.quit()
    return {'filename': filename, 'date': f"{now.month}/{now.day}/{now.year}", 'property': terms}

def scrape_homefinder(terms):
    '''Searches homefinder.com for 'terms' and returns the filename of the screenshot of the result.
    Example terms: "737 Center Dr, Palo Alto, CA", "1975 Webster St, Palo Alto, CA"
    '''
    # Get the latest chrome driver
    driver  = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.homefinder.com/")
    driver.maximize_window()

    # The website duplicates the search bar element exactly. We need the second one.
    search_bar = driver.find_elements_by_xpath("//input[@type='search']")[1]
    search_bar.clear()
    search_bar.send_keys(terms)
    search_bar.send_keys(Keys.ENTER)

    # Wait for new page to load
    max_delay = 5
    _ = WebDriverWait(driver, MAX_DELAY).until(ec.presence_of_element_located((By.XPATH, "//img[@class='img-fluid w-100 d-block']")))
    time.sleep(.5)

    # Take and save screenshot
    now = datetime.now()
    filename = f"homefinder-dot-com_{now.year}-{now.month}-{now.day}.png"
    driver.save_screenshot(filename)
    driver.quit()
    return {'filename': filename, 'date': f"{now.month}/{now.day}/{now.year}", 'property': terms}

known_sites = ["Homes.com", "Homefinder.com"]
scrape_functions = [scrape_homes, scrape_homefinder]

def main():
    search_terms = input("What to search for? ")
    print("Here are the scrapable sites: ")
    for index, site in enumerate(known_sites):
        print(f'[{index}]: {site}')
    index = int(input("Which number to scrape? "))
    scrape_functions[index](search_terms)

if __name__ == "__main__":
    main()
