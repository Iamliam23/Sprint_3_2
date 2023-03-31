from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestProfile:
    def test_login_enter_in_profile_url_is_ok(self, driver, get_the_page):
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()
        profile_url = "https://stellarburgers.nomoreparties.site/account/profile"
        WebDriverWait(driver,3).until(EC.url_to_be(profile_url))
        assert driver.current_url == profile_url

    def test_login_enter_in_profile_constructor_element_has_founded(self, driver, get_the_page):
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()
        constructor_link = driver.find_element(*Locators.CONSTR_BUTTON)
        constructor_link.click()
        ingredients_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.SECTION_1)))
        assert ingredients_section.is_displayed()

    def test_login_enter_in_profile_logo_element_has_founded(self, driver, get_the_page):
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()
        stellar_link = driver.find_element(*Locators.LOGO_BUTTON)
        stellar_link.click()
        ingredients_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.MAKE_ORDER_BUTTON)))
        assert ingredients_section.is_displayed()

    def test_login_enter_in_profile_logout_url_is_ok(self, driver, get_the_page):
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))
        logout_button = driver.find_element(*Locators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.ENTER_TITLE)))
        assert 'login' in driver.current_url

