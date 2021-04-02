from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time

class TestPaymentModule(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("C:\\Users\\LENOVO\\chromedriver.exe")

    def test_view_payment_history(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        #Testcase 1
        driver.find_element_by_name('username').send_keys('vivek')
        driver.find_element_by_name('password').send_keys('sonani')
        
        driver.find_element_by_name('submit').click()
        
        driver.find_element_by_name('view_payment_history').click()