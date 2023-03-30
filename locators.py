from selenium.webdriver.common.by import By

class Locators():

# Авторизация прошла с ошибкой
    ENTER_IN_ACC_BUTTON = By.XPATH, ".//button[text() = 'Войти в аккаунт']"   # кнопка Войти в аккаунт на главной
    REG_BUTTON = By.LINK_TEXT, "Зарегистрироваться"   # кнопка Зарегистрироваться на странице авторизации
    NAME_INPUT_REG = By.XPATH, ".//fieldset[1]//input"   # инпут Имя на странице регистрации
    EMAIL_INPUT_REG = By.XPATH, ".//fieldset[2]//input"   # инпут Email на странице регистрации
    PASS_INPUT_REG = By.XPATH, ".//fieldset[3]//input"   # инпут Пароль на странице регистрации
    REG_BUTTON_2 = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"   # кнопка Зарегистрироваться на странице регистрации
    ERROR_MES = By.XPATH, ".//fieldset[3]//p[@class = 'input__error text_type_main-default']"   # сообщение об ошибке Некорректный пароль

# Авторизация прошла успешно
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
#driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
#driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("Yury")
#driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys('iamliam1357901@yandex.ru')
#driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys("DpxutfsW1357901")
#driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click()
    ENTER_TITLE = By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2"   # заголовок Вход на странице авторизации

# Проверка плейсхолдеров при регистрации

    NAME_PLCHOLDER = By.XPATH, ".//fieldset[1]/div/div/label[@class = 'input__placeholder text noselect text_type_main-default']"   # названия плейсхолдеров на странице регистрации
    EMAIL_PLCHOLDER = By.XPATH, ".//fieldset[2]/div/div/label[@class = 'input__placeholder text noselect text_type_main-default']"
    PASS_PLCHOLDER = By.XPATH, ".//fieldset[3]/div/div/label[@class = 'input__placeholder text noselect text_type_main-default']"

# Вход
# вход по кнопке «Войти в аккаунт» на главной
#enter_in_acc_button = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    NAME_INPUT_AUTH = By.NAME, "name"   # инпут Email на странице авторизации
    PSWRD_INPUT_AUTH = By.NAME, "Пароль"   # инпут Пароль на странице авторизации
    ENTER_BUTTON = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"   # кнопка Войти на странице авторизации
    SECTION_1 = By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']"   # секция Соберите бургер на главной

# вход через кнопку «Личный кабинет»
    PROFILE_BUTTON = By.XPATH, ".//header/nav/a[@class = 'AppHeader_header__link__3D_hX']"   # кнопка Личный кабинет на главной
#driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    ENTER_BUTTON_2 = By.CLASS_NAME, "Auth_link__1fOlj"   # кнопка Войти на странице регистрации/восстановления пароля
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    ASSEMBLE_BURGER = By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"   # заголовок секции Соберите бургер на главной

# вход через кнопку в форме регистрации
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
#driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
#driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    SECTION_2 = By.XPATH, ".//section[2]/ul[@class ='BurgerConstructor_basket__list__l9dp_']"   # список с элементами имеющими заголовки Перетяните булочку сюда на главной

# вход через кнопку в форме восстановления пароля
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
    RESET_PSWRD_BUTTON = By.XPATH, ".//main/div/div/p[2]/a[@class = 'Auth_link__1fOlj']"   # кнопка Восстановить пароль на странице авторизации
#driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    DRAG_BUN_IMG = By.XPATH, ".//img[@class = 'constructor-element__image']"   # анимированный элемент в списке с элементами имеющими заголовки Перетяните булочку сюда

# Переход в личный кабинет
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901234@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901234")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
#driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    #HISTORY_BUTTON = By.LINK_TEXT, "История заказов"

# Переход из личного кабинета в Конструктор
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901234@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901234")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
#driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    CONSTR_BUTTON = By.XPATH, ".//p[text() = 'Конструктор']"   # кнопка Конструктор в хэдере
#WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']")))

# Переход из личного кабинета на логотип Stellar Burgers
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901234@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901234")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
#driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    LOGO_BUTTON = By.XPATH, ".//div/a"   # логотип Stellar burgers в хедэре
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"   # кнопка Оформить заказ на главной

# Выход из аккаунта
#driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
#driver.find_element(By.NAME, "name").send_keys('iamliam1357901234@yandex.ru')
#driver.find_element(By.NAME, "Пароль").send_keys("DpxutfsW1357901234")
#driver.find_element(By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
#driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    LOGOUT_BUTTON = By.XPATH, ".//div/nav/ul/li[3]/button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']"    # кнопка Выход в Личной Кабинете
#WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2")))

# Раздел «Конструктор». Проверь, что работают переходы к разделам:
#«Соусы»,
    SAUCES_SPAN = By.XPATH, ".//span[text() = 'Соусы']"   # cпан Соусы в секции Соберите бургер на главной
    INGR_LIST_2 = By.XPATH, ".//div/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'][2]"
#«Начинки».
    FILLINGS_SPAN = By.XPATH, ".//span[text() = 'Начинки']"   # cпан Начинки в секции Соберите бургер на главной
    FILLINGS_SPAN_2 = By.XPATH, ".//main/section/div/div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][2]"
    INGR_LIST_3 = By.XPATH, ".//div/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'][3]"
#«Булки»,
    ROLLS_SPAN = By.XPATH, ".//section[1]/div[1]/div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Булки']"   # cпан Булки в секции Соберите бургер на главной
    INGR_LIST_1 = By.XPATH, ".//div/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'][1]"

    INGR_OBJECT = By.XPATH,".//a[@class = 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"   # отдельный ингредиент контейнера в секции Соберите бургер на главной

    MENU_CONTAINER = By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']"   # контейнер с ингредиентами в секции Соберите бургер на главной
    MC_LAST_ELEMENT = By.XPATH, ".//ul[3]/a[last()]"    # последний ингредиент контейнера в секции Соберите бургер на главной
#WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//ul[3]/a[last()]")))

    #burger_constr = By.XPATH, ".//section[2]/ul[@class ='BurgerConstructor_basket__list__l9dp_']"
    DESCENDANTS_UL = By.XPATH, ".//ul//span[@class = 'constructor-element__row']"   # искомый элемент
    FILLINGS_INGR_2 = By.XPATH, ".//div/ul[3]/a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][2]"   #список ингредиентов в разделе Начинки контейнера в секции Соберите бургер на главной
#target = driver.find_element_by_xpath(".//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    #FILLINGS_INGR_4 = By.XPATH, ".//div/ul[3]/a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'][4]"
    #DESCENDANTS_UL_2 = ".//section[2]/ul/span[@class='BasketItem_basketItem__listItem__3yMU_ mb-4 mr-2']"

#ul//span[constructor-element__row] == 2
#ul//span[constructor-element__row] == 4




