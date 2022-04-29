from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import tools


@given(u'method state is set to "Private"')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.get(context.method_url)
    assert driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"


@when(u'consumer opens the method page')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    tools.logout(context)
    driver.get(context.method_url)


@then(u'login prompt is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .field span:nth-child(1)").text == "Login Name"
    tools.login_as_producer(context)


@when(u'state is changed to "Published"')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, ".label-state-private > span:nth-child(2)").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, ".label-state-private > span:nth-child(2)")
    # driver.find_element(By.ID, "workflow-transition-publish").click()
    tools.try_to_click_on(driver, By.ID, "workflow-transition-publish")
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Item state changed."


@then(u'method state is "Published"')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Published"


@given(u'method state is set to "Published"')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.get(context.method_url)
    assert driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Published"


@then(u'the method\'s content is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Example method"
    tools.login_as_producer(context)


@when(u'state is changed to "Private"')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-title:nth-child(1)").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, ".plone-toolbar-title:nth-child(1)")
    # driver.find_element(By.ID, "workflow-transition-reject").click()
    tools.try_to_click_on(driver, By.ID, "workflow-transition-reject")
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Item state changed."


@then(u'method state is "Private"')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").text == "Private"
