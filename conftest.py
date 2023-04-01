from selenium import webdriver
import pytest


@pytest.fixture()
def firefox_driver(options):
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def get_the_page(firefox_driver):
    firefox_driver.get("https://stellarburgers.nomoreparties.site/")

