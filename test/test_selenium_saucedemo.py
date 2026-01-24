import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

def test_login_correct_credentials(driver):
    driver.get("https://www.saucedemo.com")

    user_name = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    user_name.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)

    assert "inventory.html" in driver.current_url
    logging.info(f"\nCurrent URL contains 'inventory.html'")

@pytest.mark.parametrize("username, password, error_message" , [
    ("wrong-user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard-user", "wrong_sauce", "Epic sadface: Username and password do not match any user in this service")
])
def test_login_wrong_username(driver, username, password, error_message):
    driver.get("https://www.saucedemo.com")

    user_name_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    user_name_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    error = driver.find_element(By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')
    assert error.text == error_message