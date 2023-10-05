import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import pytest
class GenofaxTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
    def test_homePageTitle(self):
        self.driver.get('https://www.genofax.com/')
        #self.assertEqual("Genfax", self.driver.title,"webpage title is not matching")
    def test_why_genofax(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/nav/a[1]').click()
        #self.assertEqual("Genofax", self.driver.title, "webpage title is not matching")

    def test_products(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/nav/a[2]').click()
    def test_learn(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/nav/a[3]').click()

    def test_support(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div[3]/a[1]').click()

    def test_myaccount(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div[3]/a[2]').click()

    def test_shop(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div[3]/a[3]').click()

    def test_career(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[1]/ul/li[3]/a').click()

    def test_ourScience(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[2]/ul/li[1]/a').click()

    def test_blog(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[2]/ul/li[2]/a').click()

    def test_news(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[2]/ul/li[3]/a').click()

    def test_Affiliates(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[3]/ul/li[1]/a').click()

    def test_Distributors(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[3]/ul/li[2]/a').click()

    def test_Contact_Us(self):
        self.driver.get('https://www.genofax.com/')
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/footer/div/div[1]/div[2]/div/div[4]/ul/li[2]/a').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Compeleted....")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Teleaus\\PycharmProjects\\Genofax_UnitTest\\Reports'))
