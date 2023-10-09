import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import pytest
class GenofaxLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
    def test_userlogin(self):
        self.driver.get('https://testing.genofax.com/')
        popup_alert = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[2]/button[2]').click()
        time.sleep(10)
        myacntbtn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div[3]/a[2]').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'email').send_keys('user@example.com')
        self.driver.find_element(By.ID, 'password').send_keys('password')
        lgnbtn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/div[4]/button').click()
        time.sleep(2)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Compeleted....")