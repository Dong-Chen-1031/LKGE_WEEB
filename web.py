from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.pagamo.org/')
action = ActionChains(driver)
lodin = driver.find_elements_by_id('signin-button')
while True:
    action.click(lodin)
    action.perform()
time.sleep(100)

