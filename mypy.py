from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path= 'D:\Selenium-webdriver\ChromeDriver\chromedriver.exe'
driver=webdriver.Chrome(executable_path= path)

adsURL= "https://github.com/login"
name="suraj7wce"
pwd="sAl@0257"
driver.get(adsURL)

time.sleep(3)


username= driver.find_element(By.XPATH, '//*[@id="login_field"]')
username.send_keys(name)

pswd= driver.find_element(By.XPATH, '//*[@id="password"]')
pswd.send_keys(pwd)

login= driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]').click()

time.sleep(3)