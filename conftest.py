import pytest
from selenium import webdriver
from utilities.test_data import TestData




@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")         
    request.cls.driver = driver
    print("Browser:", request.param)
    driver.get(TestData.ppeurl)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()
    
