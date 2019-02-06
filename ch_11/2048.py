from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://play2048.co/')

gameContainerEl = driver.find_element_by_tag_name('body')

while True:
    gameContainerEl.send_keys(Keys.UP)
    gameContainerEl.send_keys(Keys.RIGHT)
    gameContainerEl.send_keys(Keys.DOWN)
    gameContainerEl.send_keys(Keys.LEFT)
