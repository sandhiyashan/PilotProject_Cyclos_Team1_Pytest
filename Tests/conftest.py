import pytest
from Utilities import read_config
from selenium import webdriver

@pytest.fixture()
def test_setup_teardown(request):
    browser=read_config.get_config("basic info","browser")
    driver=None
    if browser.__eq__("chrome"):
        driver=webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver=webdriver.Firefox
    elif browser.__eq__("edge"):
        driver=webdriver.Edge
    else:
        print("Other browser")
    driver.maximize_window()
    driver.implicitly_wait(5)   
    app_url=read_config.get_config("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()