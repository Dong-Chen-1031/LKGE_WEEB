from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.pagamo.org/')

def click(xpath):
    WebDriverWait(driver, 100000).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    c = driver.find_element_by_xpath(xpath)
    c.click()

def send(xpath,key):
    WebDriverWait(driver, 100000).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    c = driver.find_element_by_xpath(xpath)
    c.click()
    c.clear()
    c.send_keys(key)


click('//*[@id="signin-button"]') #註冊/登入
click('//*[@id="other-accounts-container"]/img[4]') #小豆豆登入
click('/html/body/div[1]/div/div/div/div[2]/div[5]/button') #使用縣市帳號登入
time.sleep(3)
click('//*[@id="id16"]/div/div/div[2]/div/div/div[3]/a') #新北市單一簽入
send('/html/body/div[1]/div/div/div/div[2]/form/div[2]/input','lkes30501') #輸入帳號
send('/html/body/div[1]/div/div/div/div[2]/form/div[3]/input','3.141592653589793') #輸入密碼
time.sleep(10)
click('/html/body/div[1]/div/div/div/div/div[3]/button') #您的教育雲端帳號是xxx

while True:
    click('/html/body/div[3]/div[3]/div[3]/div[2]/div[4]/div/div[3]/button')
    time.sleep(3)


