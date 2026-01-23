from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
#sgsgsg
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    edge_browser = webdriver.Edge(options=options)
    return edge_browser

def test_simple_button(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.ID, 'submit-id-submit')))
    button.click()
    assert 'Submitted' == driver.find_element(By.ID, 'result-text').text