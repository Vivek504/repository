from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time

class TestAccount(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("C:\\Users\\LENOVO\\chromedriver.exe")

    def test_login(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        #Testcase 1
        driver.find_element_by_name('username').send_keys('vivek')
        driver.find_element_by_name('password').send_keys('sonani')

        #Testcase 2
        # driver.find_element_by_name('username').send_keys('vivek')
        # driver.find_element_by_name('password').send_keys('123')

        driver.find_element_by_name('submit').click()

    def test_register(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        time.sleep(3)

        driver.find_element_by_name('register').click()
        time.sleep(3)
        
        #Testcase 1
        driver.find_element_by_name('username').send_keys('vivek1')
        driver.find_element_by_name('password1').send_keys('1234')
        driver.find_element_by_name('password2').send_keys('1234')
        driver.find_element_by_name('email').send_keys('viveksonani302@gmail.com')

        #Testcase 2
        # driver.find_element_by_name('username').send_keys('vivek')
        # driver.find_element_by_name('password1').send_keys('1234')
        # driver.find_element_by_name('password2').send_keys('1234')
        # driver.find_element_by_name('email').send_keys('viveksonani302@gmail.com')

        driver.find_element_by_name('submit').click()

    def test_logout(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_name('username').send_keys('aum')
        driver.find_element_by_name('password').send_keys('123')

        driver.find_element_by_name('submit').click()

        driver.find_element_by_name('logout').click()