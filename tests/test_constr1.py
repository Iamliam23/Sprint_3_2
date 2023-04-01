from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestConstructor:

    def test_stellarburgers_check_span_nbr_of_element_is_ok(self, firefox_driver, get_the_page):
        sauces = firefox_driver.find_element(*Locators.SAUCES_SPAN)
        sauces.click()
        fillings = firefox_driver.find_element(*Locators.FILLINGS_SPAN)
        fillings.click()
        rolls = firefox_driver.find_element(*Locators.ROLLS_SPAN)
        rolls.click()
        ingredients_list = WebDriverWait(firefox_driver, 3).until(expected_conditions.visibility_of_element_located((Locators.INGR_LIST_1)))
        elements = ingredients_list.find_elements(*Locators.INGR_OBJECT)
        assert len(elements) == 2, f"Expected 2 elements, but found {len(elements)}"

    def test_stellarburgers_scroll_check_nbr_of_elements_is_ok(self, firefox_driver, get_the_page):
        ingredients_list = WebDriverWait(firefox_driver, 3).until(expected_conditions.visibility_of_element_located((Locators.MENU_CONTAINER)))
        last_link = ingredients_list.find_element(*Locators.MC_LAST_ELEMENT)
        ActionChains(firefox_driver).move_to_element(last_link).perform()
        ingredients = ingredients_list.find_elements(*Locators.INGR_OBJECT)
        assert len(ingredients) == 15

    def test_stellarburgers_check_nbr_of_elements_before_after_is_ok(self, firefox_driver, get_the_page):
        WebDriverWait(firefox_driver, 3).until(expected_conditions.visibility_of_element_located((Locators.DESCENDANTS_UL)))
        span_elements = firefox_driver.find_elements(*Locators.DESCENDANTS_UL)
        assert len(span_elements) == 2, "Expected 2 span elements"
        fillings = WebDriverWait(firefox_driver, 5).until(expected_conditions.visibility_of_element_located((Locators.FILLINGS_SPAN_2)))
        fillings.click()
        element_1 = WebDriverWait(firefox_driver, 5).until(expected_conditions.visibility_of_element_located((Locators.FILLINGS_INGR_2)))
        action = ActionChains(firefox_driver)
        action.click_and_hold(element_1)
        action.move_by_offset(5, -5)
        action.release()
        action.perform()
        span_elements = WebDriverWait(firefox_driver, 5).until(expected_conditions.visibility_of_element_located((Locators.DESCENDANTS_UL)))
        assert len(span_elements) == 3, "Expected 3 span elements"