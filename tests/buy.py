import unittest
from typing import List

from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from core.testcase import TheTestCase
from core.user_actions import login_correct

operations_timeout = 60

class MyTestCase(TheTestCase):


    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        login_correct(cls.driver)

    def test_buy_remove_all_goods(self):
        add_to_card_buttons: List[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, '[id^=add-to-cart]')
        for button in add_to_card_buttons:
            WebDriverWait(self.driver, operations_timeout).until(expected_conditions.element_to_be_clickable(button))
            button.location_once_scrolled_into_view
            button.click()

        shopping_card_count_element: WebElement = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')

        goods_in_bucket = int(shopping_card_count_element.text)
        self.assertEqual(6, goods_in_bucket)  # add assertion here

        remove_buttons: List[WebElement] = self.driver.find_elements(By.CSS_SELECTOR, '[id^=remove]')
        for button in remove_buttons:
            button.location_once_scrolled_into_view
            button.click()

        result = WebDriverWait(self.driver, 10).until(expected_conditions.staleness_of(shopping_card_count_element))
        self.assertTrue(result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
