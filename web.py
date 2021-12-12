from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://www.pagamo.org/')

def cli(xpath):
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    c = driver.find_element_by_xpath(xpath)
    c.click()

cli('//*[@id="signin-button"]') # 註冊/登入
cli('//*[@id="other-accounts-container"]/img[4]') # 小豆豆登入
cli('/html/body/div[1]/div/div/div/div[2]/div[5]/button') # 使用縣市帳號登入
cli('/html/body/div[1]/div/div/div/div[2]/div[6]/div/div/div[2]/div/div/div[3]') # 新北市政府教育局單一簽入服務

# time.sleep(100)

