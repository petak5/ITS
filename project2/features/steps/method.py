from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import tools


@given(u'"Add Method" page is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.get("http://localhost:8080/repo/method/++add++method")
    # For some reason the element becomes obscured when trying to click it, will resort to direct link until resolved
    # driver.get("http://localhost:8080/repo/method")
    # sleep(0.5)
    # tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title")
    # tools.try_to_click_on(driver, By.ID, "method")


@given(u'required fields are not filled out')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # TODO: keep this empty?


@when(u'producer clicks on "Save" button')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.ID, "form-buttons-save").click()


@then(u'error message is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Error There were some errors."


@given(u'required fields are filled out')
def step_impl(context):
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


@then(u'info notification "Item created" is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Item created"


@then(u'new method is added to list of methods on "Methods" page')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Example method"


@given(u'"Edit Method" page is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)")


@when(u'text in "Title" input field is changed')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    element = driver.find_element(By.ID, "form-widgets-IBasic-title")
    element.clear()
    element.send_keys("Changed method title")


@then(u'the method has the new title')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading").text == "Changed method title"


@given(u'method delete modal popup is shown')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    # driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    tools.try_to_click_on(driver, By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title")
    # driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    tools.try_to_click_on(driver, By.ID, "plone-contentmenu-actions-delete")


@when(u'producer clicks on "Delete" button')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()


@then(u'the method is deleted')
def step_impl(context):
    driver: webdriver.Remote = context.driver
    assert driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Changed method title has been deleted."


# @given(u'tool is added in "Relations" tab')
# def step_impl(context):
#     driver: webdriver.Remote = context.driver
#     raise NotImplementedError("Not implemeted")


# @then(u'the tool is added to list of tools')
# def step_impl(context):
#     driver: webdriver.Remote = context.driver
#     raise NotImplementedError("Not implemeted")
