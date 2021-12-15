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
time.sleep(15)
click('/html/body/div[1]/div/div/div/div/div[3]/button') #您的教育雲端帳號是xxx(我知道了！)

while True:
    click('/html/body/div[3]/div[3]/div[3]/div[2]/div[4]/div/div[3]/button') #攻擊
    time.sleep(3)
    b1 = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/div[3]/div/div[2]/div[1]')
    if b1.get_attribute('class') == 'cursor_pointer choice-button attack_modal_m_sprite btn_3a1 active pgo-style-input-answer-2o3iYm':
        pass
    # time.sleep(3)
    # click('/html/body/div[11]/div/div/div/div/div[3]/div/div[2]/div[1]')
    # time.sleep(1)
    # click('/html/body/div[11]/div/div/div/div/div[3]/div/div[2]/div[2]')
    # time.sleep(3)
    # click('/html/body/div[11]/div/div/div/div/div[3]/div/div[2]/div[3]')
    # time.sleep(1)
    # click('/html/body/div[11]/div/div/div/div/div[3]/div/div[2]/div[4]')
    


