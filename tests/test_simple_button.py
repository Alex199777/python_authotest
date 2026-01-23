from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

@pytest.fixture()
def driver():
    edge_browser = webdriver.Edge()
    return edge_browser

def test_simple_button(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    driver.find_element(By.ID, 'submit-id-submit').click()
    assert 'Submitted' == driver.find_element(By.ID, 'result-text').text