from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_registration_invalid_input_error_message(self, firefox_driver, get_the_page):
        enter_button = firefox_driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        enter_button.click()
        register_button = firefox_driver.find_element(*Locators.REG_BUTTON)
        register_button.click()
        name_input = firefox_driver.find_element(*Locators.NAME_INPUT_REG)
        name_input.send_keys("Yury")
        email_input = firefox_driver.find_element(*Locators.EMAIL_INPUT_REG)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input = firefox_driver.find_element(*Locators.PASS_INPUT_REG)
        password_input.send_keys("Dpxu")
        submit_button = firefox_driver.find_element(*Locators.REG_BUTTON_2)
        submit_button.click()
        error_message = WebDriverWait(firefox_driver, 3).until(EC.visibility_of_element_located((Locators.ERROR_MES)))
        assert error_message.is_displayed()

    def test_registration_valid_input_success_login(self, firefox_driver, get_the_page):
        enter_button = firefox_driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        enter_button.click()
        register_button = firefox_driver.find_element(*Locators.REG_BUTTON)
        register_button.click()
        name_input = firefox_driver.find_element(*Locators.NAME_INPUT_REG)
        name_input.send_keys("Yury")
        email_input = firefox_driver.find_element(*Locators.EMAIL_INPUT_REG)
        email_input.send_keys("iamliam11111172@yandex.ru")
        password_input = firefox_driver.find_element(*Locators.PASS_INPUT_REG)
        password_input.send_keys("Dpxu11111172")
        submit_button = firefox_driver.find_element(*Locators.REG_BUTTON_2)
        submit_button.click()
        assert firefox_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_get_plcholders_elements_text_is_ok(self, firefox_driver, get_the_page):
        enter_button = firefox_driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        enter_button.click()
        register_button = firefox_driver.find_element(*Locators.REG_BUTTON)
        register_button.click()
        name_label = firefox_driver.find_element(*Locators.NAME_PLCHOLDER)
        assert name_label.text == 'Имя'
        email_label = firefox_driver.find_element(*Locators.EMAIL_PLCHOLDER)
        assert email_label.text == 'Email'
        password_label = firefox_driver.find_element(*Locators.PASS_PLCHOLDER)
        assert password_label.text == 'Пароль'