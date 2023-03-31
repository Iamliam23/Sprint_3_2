from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestAuthorization:
    def test_login_with_enter_in_acc_element_has_founded(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        ingredients_section = WebDriverWait(driver,5).until(EC.presence_of_element_located((Locators.SECTION_1)))
        assert ingredients_section.is_displayed()

    def test_login_with_profile_button_element_has_founded(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        profile_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.PROFILE_BUTTON)))
        profile_link.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        basket_section = WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SECTION_2)))
        assert basket_section.is_displayed()

    def test_login_with_enter_2_button_element_text_is_ok(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        reset_pswrd = driver.find_element(*Locators.REG_BUTTON)
        reset_pswrd.click()
        reset_pswrd = driver.find_element(*Locators.ENTER_BUTTON_2)
        reset_pswrd.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.ASSEMBLE_BURGER)))
        assert element.text == "Соберите бургер"

    def test_auth_with_reset_pswrd_button_image_link_is_ok(self, driver, get_the_page):
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()
        reset_pswrd = driver.find_element(*Locators.RESET_PSWRD_BUTTON)
        reset_pswrd.click()
        enter_button = driver.find_element(*Locators.ENTER_BUTTON_2)
        enter_button.click()
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()
        images = driver.find_elements(*Locators.DRAG_BUN_IMG)
        for image in images:
            assert "./static/media/loading.89540200.svg" in image.get_attribute('src')