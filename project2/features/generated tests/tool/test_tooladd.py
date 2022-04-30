# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTooladd():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tooladd(self):
    self.driver.get("http://localhost:8080/repo/tools")
    self.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    self.driver.find_element(By.ID, "tool").click()
    self.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    self.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Example tool")
    self.driver.find_element(By.ID, "form-widgets-tool_purpose").click()
    self.driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("To be an example")
    self.driver.switch_to.frame(3)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'An example tool'}", element)
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'There are none'}", element)
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'There are also none'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "form-buttons-save").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".portalMessage").text == "Info Item created"
  