import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if (len(sys.argv) < 3):
    print('There should be more than 2 arguments')
    sys.exit()

recepientEmail = sys.argv[1]
emailContent = ' '.join(sys.argv[2:])

driver = webdriver.Firefox()
driver.get('http://gmail.com')

emailEl = driver.find_element_by_class_name('whsOnd')
emailEl.send_keys('enter email here')
emailEl.send_keys(Keys.ENTER)

time.sleep(3)

passEl = driver.find_element_by_class_name('whsOnd')
passEl.send_keys('enter password here')
passEl.send_keys(Keys.ENTER)

time.sleep(10)

composeButtEl = driver.find_elements_by_css_selector(
        ".aic > .z0 > .T-I")
composeButtEl[0].click()

time.sleep(20)

recepientEl = driver.find_element_by_css_selector('textarea[name="to"]')
recepientEl.send_keys(recepientEmail)

contentEl = driver.find_element_by_css_selector('div.editable[role="textbox"]')
contentEl.send_keys(emailContent)

sendButtonEl = driver.find_element_by_css_selector(
        'div.btA > div[role="button"]')
sendButtonEl.click()
