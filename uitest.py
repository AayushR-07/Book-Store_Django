import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """Fixture to manage WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(driver):
    driver.get("http://127.0.0.1:5500/index.html")

    driver.find_element(By.NAME, 'username').send_keys('Aayush')
    driver.find_element(By.NAME, 'password').send_keys('pass123')
    driver.find_element(By.ID, 'login-button').click()
    
    message = driver.find_element(By.ID, 'welcome').text
    assert 'Welcome' in message and 'test user' in message.lower()



