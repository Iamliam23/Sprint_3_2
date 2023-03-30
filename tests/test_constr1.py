from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
import time


class TestConstructor:
    def test_stellarburgers_check_span_nbr_of_element_is_ok(self, driver):
        # Открываем сайт
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переходим к секции Соберите бургер и нажимаем на спан "Соусы"
        sauces = driver.find_element(*Locators.SAUCES_SPAN)
        sauces.click()

        # Переходим к секции Соберите бургер и нажимаем на спан "Начинки"
        fillings = driver.find_element(*Locators.FILLINGS_SPAN)
        fillings.click()

        # Переходим к секции Соберите бургер и нажимаем на спан "Булки"
        Rolls = driver.find_element(*Locators.ROLLS_SPAN)
        Rolls.click()

        # Ждем появления элементов в разделе Булки
        ingredients_list = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.INGR_LIST_1)))

        # Проверяем, что количество элементов в разделе Булки равно 2
        elements = ingredients_list.find_elements(*Locators.INGR_OBJECT)
        assert len(elements) == 2, f"Expected 2 elements, but found {len(elements)}"

    def test_stellarburgers_scroll_check_nbr_of_elements_is_ok(self, driver):
        # Открываем сайт
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидаем появления контейнера с элементами
        ingredients_list = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Locators.MENU_CONTAINER)))

        # Скроллим контейнер до нужного элемента
        last_link = ingredients_list.find_element(*Locators.MC_LAST_ELEMENT)
        ActionChains(driver).move_to_element(last_link).perform()

        # Ждем пока загрузится последний элемент
        # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.MC_LAST_ELEMENT)))

        # Проверяем общее количество элементов в контейнере
        ingredients = ingredients_list.find_elements(*Locators.INGR_OBJECT)
        assert len(ingredients) == 15

    def test_stellarburgers_check_nbr_of_elements_before_after_is_ok(self, driver):
        # Открываем сайт
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидаем появления элементов DESCENDANTS_UL
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.DESCENDANTS_UL)))

        # Проверяем что количество элементов DESCENDANTS_UL на главной странице равно 2
        span_elements = driver.find_elements(*Locators.DESCENDANTS_UL)
        assert len(span_elements) == 2, "Expected 2 span elements"

        # Ожидаем появления спана Начинки и кликаем на него
        # WebDriverWait(driver,5).until(EC.presence_of_element_located((Locators.FILLINGS_SPAN_2)))
        time.sleep(5)
        fillings = driver.find_element(*Locators.FILLINGS_SPAN_2)
        fillings.click()

        # Ожидаем появления элемента FILLINGS_INGR_2
        # WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.FILLINGS_INGR_2)))
        time.sleep(5)

        # Нажимаем на второй элемент в разделе Начинки, перетаскиваем его в область списка с элементами имеющими заголовки Перетяните булочку сюда, отпускаем элемент
        element_1 = driver.find_element(*Locators.FILLINGS_INGR_2)
        action = ActionChains(driver)
        action.click_and_hold(element_1)
        action.move_by_offset(5, -5)
        action.release()
        action.perform()

        # ActionChains(driver).click_and_hold(element_1).move_to_element(target).release().perform()

        # перемещаем элементы 2
        # time.sleep(3)
        # element_2 = driver.find_element(*Locators.FILLINGS_INGR_4)
        # target = driver.find_element(*Locators.SECTION_2)
        # action.click_and_hold(element_2)
        # action.move_by_offset(5, -5)
        # action.release()
        # action.perform()

        # ActionChains(driver).click_and_hold(element_2).move_to_element(target).release().perform()

        # Ожидаем появления элементов DESCENDANTS_UL
        # WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.DESCENDANTS_UL)))

        # Проверяем что количество элементов DESCENDANTS_UL стало равным 3
        time.sleep(5)
        span_elements = driver.find_elements(*Locators.DESCENDANTS_UL)
        assert len(span_elements) == 3, "Expected 3 span elements"