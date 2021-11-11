import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    time.sleep(1)
    # Looking for 1975 Webster St, Palo Alto, CA, which has a LISTING ID of LMKHZM
    # but that one's gone, so look for 737 Center Dr, Palo Alto, CA
    elem = driver.find_element_by_tag_name("input")
    elem.clear()
    elem.send_keys(terms)
    # It wants to load up possible addresses, so wait until it does that.
    time.sleep(.5)
    elem.send_keys(Keys.ENTER)
    # Wait for the new page to load
    time.sleep(1)
    # Should have a page with the correct listing.
    now = datetime.now()
    filename = f"homes-dot-com_on_{now.year}_{now.month}_{now.day}.png"
    driver.save_screenshot(filename)
    driver.quit()
    return filename

known_sites = ["Homes.com"]
scrape_functions = [scrape_homes]

def main():
    search_terms = input("What to search for? ")
    print("Here are the scrapable sites: ")
    for index, site in enumerate(known_sites):
        print(f'[{index}]: {site}')
    index = int(input("Which number to scrape? "))
    scrape_functions[index](search_terms)

if __name__ == "__main__":
    main()
