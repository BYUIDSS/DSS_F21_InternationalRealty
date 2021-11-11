from selenium import webdriver



list = ["https://www.sothebysrealty.com/eng/sales/detail/180-l-3001-39v5xn/12160-kate-drive-los-altos-hills-ca-94022", 
"https://www.goldengatesir.com/eng/sales/detail/561-l-3001-39v5xn/12160-kate-drive-los-altos-hills-ca-94022", 
"https://www.juwai.com/58135931.htm",
"https://real-buzz.com/RealEstate-detail/12160-Kate-Drive_Los-Altos-Hills_California_94022_house-for-sale_USD_183003924"]


driver = webdriver.Chrome("/Users/davidbell/Downloads/chromedriver 2")

image_list = []

i = 0

for url in list:
    driver.get(url)
    driver.save_screenshot(image_list)

driver.close()

