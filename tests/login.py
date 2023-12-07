import unittest

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from core.testcase import TheTestCase, login
from core.user_actions import login_correct, login_with_credentials


class Login(TheTestCase):
    def test_positive_login(self):
        result = login_correct(self.driver)
        self.assertTrue(result, 'Login unsuccessful')

    def test_negative_login(self):
        login_with_credentials(self.driver, login, '!@^(*%(&^!')
        try:
            element_present = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.error'))
            WebDriverWait(self.driver, 60).until(element_present)
            failure: bool = True
            error_message: str = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
        except TimeoutException:
            failure: bool = False
        print(f'Error message is {error_message}')
        self.assertTrue(failure, 'No error message is shown on wrong login')

if __name__ == '__main__':
    unittest.main()
