from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestAuthorization:
    def test_login_with_enter_in_acc_element_has_founded(self, driver):
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

        # Ждем появления секции Соберите бургер на главной странице
        ingredients_section = WebDriverWait(driver,5).until(EC.presence_of_element_located((Locators.SECTION_1)))

        # Проверяем что секция Соберите бургер отображается на главной странице
        assert ingredients_section.is_displayed()

    def test_login_with_profile_button_element_has_founded(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидаем появления кнопки Личный Кабинет и нажимаем на нее
        profile_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.PROFILE_BUTTON)))
        profile_link.click()

        # Вводим данные для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем на кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # Ждем появления списка с двумя элементами имеющими заголовки Перетяните булочку на главной странице
        basket_section = WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SECTION_2)))

        # Проверяем что список отображается на главной странице
        assert basket_section.is_displayed()

    def test_login_with_enter_2_button_element_text_is_ok(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку Войти в аккаунт
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()

        # Нажимаем на кнопку Регистрация
        reset_pswrd = driver.find_element(*Locators.REG_BUTTON)
        reset_pswrd.click()

        # Нажимаем кнопку Войти
        reset_pswrd = driver.find_element(*Locators.ENTER_BUTTON_2)
        reset_pswrd.click()

        # Вводим email и пароль для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем на кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # Ожидаем наличия элемента ASSEMBLE_BURGER на странице
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.ASSEMBLE_BURGER)))

        # Проверяем наличие корректного текста у заголовка Соберите бургер на главной странице
        assert element.text == "Соберите бургер"

    def test_auth_with_reset_pswrd_button_image_link_is_ok(self, driver):
        # Открываем страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку Войти в аккаунт
        Enter_button = driver.find_element(*Locators.ENTER_IN_ACC_BUTTON)
        Enter_button.click()

        # Нажимаем на кнопку Восстановить пароль
        reset_pswrd = driver.find_element(*Locators.RESET_PSWRD_BUTTON)
        reset_pswrd.click()

        # Нажимаем на кнопку Войти
        enter_button = driver.find_element(*Locators.ENTER_BUTTON_2)
        enter_button.click()

        # Вводим логин и пароль для авторизации
        email_input = driver.find_element(*Locators.NAME_INPUT_AUTH)
        password_input = driver.find_element(*Locators.PSWRD_INPUT_AUTH)
        email_input.send_keys("iamliam9876@yandex.ru")
        password_input.send_keys("DpxutfsW9876")

        # Нажимаем кнопку Войти
        login_button = driver.find_element(*Locators.ENTER_BUTTON)
        login_button.click()

        # В списке с элементами имеющими заголовки Перетяните булочку на главной странице проверяем наличие файла свг у анимированных элементов
        images = driver.find_elements(*Locators.DRAG_BUN_IMG)
        for image in images:
            assert "./static/media/loading.89540200.svg" in image.get_attribute('src')



# Проходит
