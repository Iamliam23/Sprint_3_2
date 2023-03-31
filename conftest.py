from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

DEFAULT_WINDOW_SIZE = {
    1920: "--window-size=1920,1080"
}


@pytest.fixture()
def options():
    options = Options()
    options.add_argument(DEFAULT_WINDOW_SIZE[1920])
    options.add_argument(DEFAULT_WINDOW_SIZE[1080])
    return options

@pytest.fixture()
def driver(request, options):
    driver = webdriver.Chrome(options=options)
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture()
def get_the_page():
    driver.get("https://stellarburgers.nomoreparties.site/")

