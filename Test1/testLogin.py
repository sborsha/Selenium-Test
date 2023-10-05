import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testing.genofax.com/")
#dely
time.sleep(2)
#full windows
driver.maximize_window()
#time.sleep(5)
popup_alert = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[2]/button[2]').click()
time.sleep(5)
myacntbtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div[3]/a[2]').click()
time.sleep(2)
driver.find_element(By.ID, 'email').send_keys('user@example.com')
driver.find_element(By.ID, 'password').send_keys('password')
lgnbtn = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/div[4]/button').click()
time.sleep(2)
print('Login Successfully...........!')