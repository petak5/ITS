from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


# Admin menu sometimes does not contain items right after loading is done, thus resulting in failed test
# This method resolves the issue
def try_to_click_on(driver: webdriver.Remote, by=By.ID, value: str = None):
    element = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((by, value)))
    element.location_once_scrolled_into_view
    element.click()

    return element


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
    try_to_click_on(driver, By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)")
    # element = driver.find_element(By.ID, "personaltools-logout")
    try_to_click_on(driver, By.ID, "personaltools-logout")
