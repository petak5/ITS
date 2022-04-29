#!/usr/bin/env python3
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from time import sleep

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
    login_as_producer(context)


def after_feature(context, feature):
    logout(context)


def login_as_producer(context):
    driver: webdriver.Remote = context.driver
    driver.get("http://localhost:8080/repo/")
    driver.find_element(By.ID, "personaltools-login").click()
    driver.find_element(By.ID, "__ac_name").click()
    driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


def logout(context):
    driver: webdriver.Remote = context.driver
    driver.get("http://localhost:8080/repo/")
    # element = driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)")
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)")
    # element = driver.find_element(By.ID, "personaltools-logout")
    tools.try_to_click_on(driver, By.ID, "personaltools-logout")
