import unittest

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from core.testcase import TheTestCase
from core.user_actions import login_correct

NUMBER_OF_ITERATIONS = 100

class MultipleGetPage(TheTestCase):
    def test_100_login_page_open(self):
        iteration = 0
        while iteration < NUMBER_OF_ITERATIONS:
            iteration += 1
            self.get_main_page()
            try:
                element_present = expected_conditions.presence_of_element_located((By.ID, 'user-name'))
                WebDriverWait(self.driver, 30).until(element_present)
                opened: bool = True
            except TimeoutException:
                opened: bool = False
            self.assertTrue(opened)

    def test_login_10_times(self):
        iteration = 0
        result = False
        while iteration < NUMBER_OF_ITERATIONS:
            login_correct(self.driver)
            self.driver.delete_all_cookies()
            self.get_main_page()
            iteration += 1
        else:
            result = True

        self.assertTrue(result, "100 iterations of login happened")

if __name__ == '__main__':
    unittest.main()
