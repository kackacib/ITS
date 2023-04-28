
from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    # Get Chrome/Firefox web driver
    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(15)
    base_url = "http://localhost:8080/VALU3S"
    return driver

def before_all(context):
    context.driver = setup_driver()
    context.base_url = "http://localhost:8080/VALU3S"


def after_all(context):
    context.driver.quit()

