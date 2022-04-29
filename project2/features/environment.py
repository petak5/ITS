#!/usr/bin/env python3
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

import tools


URL = "http://localhost:8080/repo"


def get_driver():
    '''Get Firefox/Chrome driver from Selenium Hub'''
    try:
        driver: webdriver.Remote = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    driver.implicitly_wait(5)

    return driver


def before_all(context):
    context.driver = get_driver()
    context.driver.get(URL)


def after_all(context):
    context.driver.close()


def before_feature(context, feature):
    # Log in as producer (majority of tests use this role)
    tools.login_as_producer(context)

    driver: webdriver.Remote = context.driver
    if feature.name == "Visibility":
        # Add method and save its URL
        driver.get("http://localhost:8080/repo/method/++add++method")

        driver: webdriver.Remote = context.driver
        driver.find_element(By.ID, "form-widgets-IBasic-title").click()
        driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Example method")
        driver.find_element(By.ID, "form-widgets-method_purpose").click()
        driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("To be an example")
        driver.switch_to.frame(3)
        driver.find_element(By.CSS_SELECTOR, "html").click()
        driver.switch_to.default_content()
        driver.switch_to.frame(3)
        element = driver.find_element(By.ID, "tinymce")
        driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'An example method'}", element)
        driver.switch_to.default_content()
        driver.switch_to.frame(2)
        driver.find_element(By.CSS_SELECTOR, "html").click()
        element = driver.find_element(By.ID, "tinymce")
        driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'There are none'}", element)
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
        driver.find_element(By.CSS_SELECTOR, "html").click()
        element = driver.find_element(By.ID, "tinymce")
        driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'There are also none'}", element)
        driver.switch_to.default_content()

        driver.find_element(By.ID, "form-buttons-save").click()

        context.method_url = driver.current_url



def after_feature(context, feature):
    driver: webdriver.Remote = context.driver
    if feature.name == "Visibility":
        # Delete method
        driver.get(context.method_url)

        tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title")
        tools.try_to_click_on(driver, By.ID, "plone-contentmenu-actions-delete")

        driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()

    tools.logout(context)
