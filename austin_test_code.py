from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.instagram.com/')