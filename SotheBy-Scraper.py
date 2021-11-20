from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Scrapes each URL under the SotheBys heading on threestory_FA21 readme.md
# an ID is required to scrape. Should be able to extract ID from the excel spreadsheet.
# Returns the names of the files created in a list.
def Scrape_SotheBys_fromID(ID) -> list():

    urlsToScrape = [
            # Sotheby's Listings
            'https://www.sothebysrealty.com/id/',
            'https://www.goldengatesir.com/id/',
            'https://www.jamesedition.com/ref/',
            'https://www.juwai.com/find-listing-by-source?source=Sothebys&source_id=',
            'https://real-buzz.com/RealEstate-detail-SIR/',
            'http://countrylife.co.uk/international-property/'
            ]

    # scrape images from list of urls.
    driver  = webdriver.Chrome(ChromeDriverManager().install()) # installs chromedriver locally and then initializes it at run time
    imageNumber = 0
    ImageList = list()

    for url in urlsToScrape:
        imageNumber += 1
        driver.get((url + ID))
        driver.save_screenshot(f'Sotheby-{imageNumber}.png')
        ImageList.append(f'Sotheby-{imageNumber}.png')
    driver.close()
    return ImageList

results = Scrape_SotheBys_fromID('LMKHZM') # For test scrape.
print(results)