from time import sleep
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

import tools


@given(u'"Add Use Case" page is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.get("http://localhost:8080/repo/use-cases/++add++use_case")
    # For some reason the element becomes obscured when trying to click it, will resort to direct link until resolved
    # Method has the same problem
    # driver.get("http://localhost:8080/repo/use-cases")
    # driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    # tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title")
    # driver.find_element(By.ID, "use_case").click()
    # tools.try_to_click_on(driver, By.ID, "use_case")


@given(u'use case required fields are not filled out')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # TODO: leave this empty?


@when(u'producer clicks on "Save" use case button')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.ID, "form-buttons-save").click()


@then(u'use case error message is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Error There were some errors."


@given(u'use case required fields are filled out')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Example use case")
    driver.switch_to.frame(0)
    driver.find_element(By.CSS_SELECTOR, "html").click()
    element = driver.find_element(By.ID, "tinymce")
    driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'An example use case'}", element)
    driver.switch_to.default_content()


@then(u'use case info notification "Item created" is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Item created"


@given(u'"Edit Use Case" page is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)")


@when(u'use case text in "Title" input field is changed')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    element = driver.find_element(By.ID, "form-widgets-IBasic-title")
    element.click()
    element.clear()
    element.send_keys("Changed example use case")


@then(u'the use case has the new title')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Changes saved"
    assert driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Changed example use case"


@given(u'use case delete modal popup is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title")
    # driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    tools.try_to_click_on(driver, By.ID, "plone-contentmenu-actions-delete")


@when(u'producer clicks on "Delete" use case button')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()


@then(u'info notification "use case has been deleted" is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Changed example use case has been deleted."
