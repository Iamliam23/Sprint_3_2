from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestProfile:
    def test_login_enter_in_profile_url_is_ok(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку Войти в аккаунт
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()

        # Вводим данные для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем на кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # Нажимаем на кнопку Личный Кабинет
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()

        # Проверяем URL последней страницы
        profile_url = "https://stellarburgers.nomoreparties.site/account/profile"
        WebDriverWait(driver,3).until(EC.url_to_be(profile_url))
        assert driver.current_url == profile_url

    def test_login_enter_in_profile_constructor_element_has_founded(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку Войти в аккаунт
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()

        # Вводим данные для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем на кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # Нажимаем на кнопку Личный Кабинет
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()

        # Переходим в раздел Конструктор в хедэре
        constructor_link = driver.find_element(*Locators.CONSTR_BUTTON)
        constructor_link.click()

        # Проверяем что секция Соберите бургер отображается на главной странице
        ingredients_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.SECTION_1)))
        assert ingredients_section.is_displayed()

    def test_login_enter_in_profile_logo_element_has_founded(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку Войти в аккаунт
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()

        # Вводим данные для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем на кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # Нажимаем на кнопку Личный Кабинет
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()

        # Нажимаем на лого Stellar Burgers в хедэре
        stellar_link = driver.find_element(*Locators.LOGO_BUTTON)
        stellar_link.click()

        # Проверяем что кнопка Оформить заказ отображается на главной странице
        ingredients_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.MAKE_ORDER_BUTTON)))
        assert ingredients_section.is_displayed()

    def test_login_enter_in_profile_logout_url_is_ok(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку Войти в аккаунт
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()

        # Вводим данные для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем на кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # Нажимаем на кнопку Личный Кабинет
        login_button2 = driver.find_element(*Locators.PROFILE_BUTTON)
        login_button2.click()

        # Ожидаем появления кнопки Выход
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))

        # Нажимаем на кнопку Выход
        logout_button = driver.find_element(*Locators.LOGOUT_BUTTON)
        logout_button.click()

        # Ожидаем переход на страницу логина
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.ENTER_TITLE)))

        # Проверяем наличие "login" в текущем урле
        assert 'login' in driver.current_url

