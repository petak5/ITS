from time import sleep
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

import tools


@given(u'"Add Tool" page is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.get("http://localhost:8080/repo/tools")
    # driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title")
    # driver.find_element(By.ID, "tool").click()
    tools.try_to_click_on(driver, By.ID, "tool")


@given(u'tool required fields are not filled out')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # TODO: leave this empty?


@when(u'producer clicks on "Save" tool button')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.ID, "form-buttons-save").click()


@then(u'tool error message is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Error There were some errors."


@given(u'tool required fields are filled out')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Example tool")
    driver.find_element(By.ID, "form-widgets-tool_purpose").click()
    driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("To be an example")
    driver.switch_to.frame(3)
    driver.find_element(By.CSS_SELECTOR, "html").click()
    element = driver.find_element(By.ID, "tinymce")
    driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'An example tool'}", element)
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


@then(u'tool info notification "Item created" is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Item created"


@given(u'"Edit Tool" page is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)")


@when(u'tool text in "Title" input field is changed')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    driver.find_element(By.ID, "form-widgets-IDublinCore-title").clear()
    driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Edited example tool")


@then(u'the tool has the new title')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Edited example tool"


@given(u'tool delete modal popup is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title")
    # driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    tools.try_to_click_on(driver, By.ID, "plone-contentmenu-actions-delete")


@when(u'producer clicks on "Delete" tool button')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()


@then(u'info notification "tool has been deleted" is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Edited example tool has been deleted."
