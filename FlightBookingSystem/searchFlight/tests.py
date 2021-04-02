from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
import time

class TestSearchFlight(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("C:\\Users\\LENOVO\\chromedriver.exe")

    def test_onewayTrip(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/home')

        driver.find_element_by_name('oneway').click()

        #Testcase 1
        driver.find_element_by_name('from').send_keys('Surat')
        driver.find_element_by_name('to').send_keys('Mumbai')
        driver.find_element_by_name('depdate').send_keys('05-04-2021')
        driver.find_element_by_name('travellers').send_keys('2')
        driver.find_element_by_name('class').send_keys('First')

        #Testcase 2
        # driver.find_element_by_name('from').send_keys('Surat')
        # driver.find_element_by_name('to').send_keys('Mumbai')
        # driver.find_element_by_name('depdate').send_keys('10-04-2021')
        # driver.find_element_by_name('travellers').send_keys('2')
        # driver.find_element_by_name('class').send_keys('First')

        driver.find_element_by_name('submit1').click()

    def test_roundTrip(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/home')

        driver.find_element_by_name('round').click()
        time.sleep(3)

        #Testcase 1
        driver.find_element_by_id('from2').send_keys('Surat')
        driver.find_element_by_id('to2').send_keys('Mumbai')
        driver.find_element_by_id('depdate2').send_keys('05-04-2021')
        driver.find_element_by_id('retdate').send_keys('06-04-2021')
        driver.find_element_by_id('travellers2').send_keys('2')
        driver.find_element_by_name('class2').send_keys('First')

        #Testcase 2
        # driver.find_element_by_id('from2').send_keys('Surat')
        # driver.find_element_by_id('to2').send_keys('Mumbai')
        # driver.find_element_by_id('depdate2').send_keys('10-04-2021')
        # driver.find_element_by_id('retdate').send_keys('15-04-2021')
        # driver.find_element_by_id('travellers2').send_keys('2')
        # driver.find_element_by_name('class2').send_keys('First')

        #Testcase 3
        # driver.find_element_by_id('from2').send_keys('Surat')
        # driver.find_element_by_id('to2').send_keys('Mumbai')
        # driver.find_element_by_id('depdate2').send_keys('05-04-2021')
        # driver.find_element_by_id('retdate').send_keys('10-04-2021')
        # driver.find_element_by_id('travellers2').send_keys('2')
        # driver.find_element_by_name('class2').send_keys('First')

        #Testcase 4
        # driver.find_element_by_id('from2').send_keys('Surat')
        # driver.find_element_by_id('to2').send_keys('Mumbai')
        # driver.find_element_by_id('depdate2').send_keys('04-04-2021')
        # driver.find_element_by_id('retdate').send_keys('06-04-2021')
        # driver.find_element_by_id('travellers2').send_keys('2')
        # driver.find_element_by_name('class2').send_keys('First')

        driver.find_element_by_name('submit2').click()