from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from core import testcase

def login_with_credentials(driver: WebDriver, username: str, password: str):
    driver: WebDriver = driver
    username_textbox: WebElement = driver.find_element(By.ID, 'user-name')
    username_textbox.clear()
    username_textbox.send_keys(username)
    password_textbox: WebElement = driver.find_element(By.ID, 'password')
    password_textbox.clear()
    password_textbox.send_keys(password)
    login_button: WebElement = driver.find_element(By.ID, 'login-button')
    login_button.click()

def login_correct(driver):
    login_with_credentials(driver, testcase.login, testcase.password)
    try:
        element_present = expected_conditions.presence_of_element_located((By.ID, 'inventory_container'))
        WebDriverWait(driver, 60).until(element_present)
        result: bool = True
    except TimeoutException:
        result: bool = False

    return result