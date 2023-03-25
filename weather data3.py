import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
webdriver_path= 'C://Users//jopok//chromedriver.exe'

# Select custom Chrome options
options = webdriver.ChromeOptions()
#options.add_argument('--headless') #run script with browser in background
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
#opening the browser
browser = webdriver.Chrome(webdriver_path, options=options)
row_data=[]
date_data=[]
for i in range(7,16):
    URL='https://www.wunderground.com/history/daily/id/badung/WADD/date/2019-12-{}'.format(i)
    browser.get(URL)
    #let page load
    browser.implicitly_wait(15)

    #tbody= '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody'
    tbody='//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody'
    table_body= browser.find_element(By.XPATH, tbody)
    table_rows= table_body.find_elements(By.TAG_NAME, "tr")
        
    with open("weatherdata.csv","w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in table_rows:
            table_data=row.find_elements(By.XPATH,'.//td[3]')
            table1_data=row.find_elements(By.XPATH,'.//td[1]')
            for data in table_data:
                row_data.append(data.text)
            for data1 in table1_data:
                date_data.append(data1.text)
        for j in range(len(row_data)):    
            writer.writerow([date_data[j],row_data[j]])

            #for j in range(len(row_data)):    
                #writer.writerow(row_data[j])

        '''for tr in table.find_elements(By.XPATH, '//tr' ):
            row=[item.text for item in tr.find_elements(By.XPATH, './/td[3]')]
            data.append(row)
        #print(data)'''
    #print(data)
    #print(rowdata)
print(row_data)
