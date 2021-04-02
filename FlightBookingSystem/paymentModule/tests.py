from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time

class TestPaymentModule(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("C:\\Users\\vivek\\chromedriver.exe")

    def test_view_payment_history(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_name('username').send_keys('vivek')
        driver.find_element_by_name('password').send_keys('sonani')
        driver.find_element_by_name('submit').click()
        
        driver.find_element_by_name('view_payment_history').click()

    def test_onewayTrip_payment(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_name('username').send_keys('vivek')
        driver.find_element_by_name('password').send_keys('sonani')
        driver.find_element_by_name('submit').click()

        driver.find_element_by_name('oneway').click()
        driver.find_element_by_name('from').send_keys('Surat')
        driver.find_element_by_name('to').send_keys('Mumbai')
        driver.find_element_by_name('depdate').send_keys('05-04-2021')
        driver.find_element_by_name('travellers').send_keys('2')
        driver.find_element_by_name('class').send_keys('First')
        driver.find_element_by_name('submit1').click()

        driver.find_element_by_xpath('/html/body/form/div/div/table/tbody/tr[2]/td[4]/a').click()

        driver.find_element_by_name('fname').send_keys('Vivek')
        driver.find_element_by_name('lname').send_keys('Sonani')
        driver.find_element_by_name('mobno').send_keys('9879730662')
        driver.find_element_by_name('email').send_keys('viveksonani302@gmail.com')
        driver.find_element_by_name('paymethod').send_keys('debit')
        driver.find_element_by_name('continue').click()

        driver.find_element_by_name('cardno').send_keys('12345678901234567')
        driver.find_element_by_name('cvv').send_keys('123')
        driver.find_element_by_name('make_payment').click()

    def test_roundTrip_payment(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        
        driver.find_element_by_name('username').send_keys('vivek')
        driver.find_element_by_name('password').send_keys('sonani')
        driver.find_element_by_name('submit').click()

        driver.find_element_by_name('round').click()
        time.sleep(3)
        driver.find_element_by_id('from2').send_keys('Surat')
        driver.find_element_by_id('to2').send_keys('Mumbai')
        driver.find_element_by_id('depdate2').send_keys('05-04-2021')
        driver.find_element_by_id('retdate').send_keys('06-04-2021')
        driver.find_element_by_id('travellers2').send_keys('2')
        driver.find_element_by_name('class2').send_keys('First')
        driver.find_element_by_name('submit2').click()

        driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[2]/td[4]/input').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[2]/td[4]/input').click()
        driver.find_element_by_name('select').click()
        driver.find_element_by_xpath('//*[@id="select"]/a').click()

        driver.find_element_by_name('fname').send_keys('Vivek')
        driver.find_element_by_name('lname').send_keys('Sonani')
        driver.find_element_by_name('mobno').send_keys('9879730662')
        driver.find_element_by_name('email').send_keys('viveksonani302@gmail.com')
        driver.find_element_by_name('paymethod').send_keys('debit')
        driver.find_element_by_name('continue').click()

        driver.find_element_by_name('cardno').send_keys('12345678901234567')
        driver.find_element_by_name('cvv').send_keys('123')
        driver.find_element_by_name('make_payment').click()