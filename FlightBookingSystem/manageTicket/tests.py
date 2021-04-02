from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time

class TestTicket(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("C:\\Users\\LENOVO\\chromedriver.exe")

    def test_view_ticket(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_name('username').send_keys('aumth')
        driver.find_element_by_name('password').send_keys('123')
        
        driver.find_element_by_name('submit').click()
        
        driver.find_element_by_name('view_ticket').click()

    def test_cancel_ticket(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_name('username').send_keys('aumth')
        driver.find_element_by_name('password').send_keys('123')
        
        driver.find_element_by_name('submit').click()
        
        driver.find_element_by_name('view_ticket').click()

        driver.find_element_by_name('ticket_id').send_keys('1')
        driver.find_element_by_name('submit').click()

        driver.find_element_by_name('username').send_keys('aumth')
        driver.find_element_by_name('password').send_keys('123')
        driver.find_element_by_name('submit').click()