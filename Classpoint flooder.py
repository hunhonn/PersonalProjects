from lib2to3.pgen2 import driver
from sqlite3 import paramstyle
from selenium import webdriver
from selenium.common.exceptions import *
from IPython.display import display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
webdriver_path= 'C://Users//jopok//chromedriver.exe'
URL= 'https://classpoint.app/join'
class_code= input("Input Classpoint code:")
class_name="namee1"
for i in range(20):
    
# Select custom Chrome options
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless') #run script with browser in background
    options.add_argument('start-maximized') 
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    # Open the Chrome browser
    browser = webdriver.Chrome(webdriver_path, options=options)
    browser.get(URL)
    #waits for 3 seconds for the page to load
    browser.implicitly_wait(3)
    search_bar=browser.find_element_by_xpath("//input[@placeholder='Class Code']").send_keys(class_code)
    

    name_bar=browser.find_element_by_xpath("//input[@placeholder='Your Name']").send_keys(class_name)
    
    button=browser.find_element_by_css_selector(".btn.btn-primary.btn-block.btn-lg.mt-20.mb-10.waves-effect.waves-light.waves-round")
    button.click()
    browser.implicitly_wait(30)
