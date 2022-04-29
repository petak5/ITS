from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def try_to_click_on(driver: webdriver.Remote, by=By.ID, value: str = None):
    element = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((by, value)))
    element.location_once_scrolled_into_view
    element.click()

    return element
