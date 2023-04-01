from selenium.webdriver.common.by import By

class Locators():

    ENTER_IN_ACC_BUTTON = By.XPATH, ".//button[text() = 'Войти в аккаунт']"   # кнопка Войти в аккаунт на главной
    REG_BUTTON = By.LINK_TEXT, "Зарегистрироваться"   # кнопка Зарегистрироваться на странице авторизации
    NAME_INPUT_REG = By.XPATH, ".//fieldset[1]//input"   # инпут Имя на странице регистрации
    EMAIL_INPUT_REG = By.XPATH, ".//fieldset[2]//input"   # инпут Email на странице регистрации
    PASS_INPUT_REG = By.XPATH, ".//fieldset[3]//input"   # инпут Пароль на странице регистрации
    REG_BUTTON_2 = By.XPATH, "/html/body/div[1]/div/main/div/form/button]"   # кнопка Зарегистрироваться на странице регистрации
    ERROR_MES = By.XPATH, ".//fieldset[3]//p[@class = 'input__error text_type_main-default']"   # сообщение об ошибке Некорректный пароль
    ENTER_TITLE = By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2"   # заголовок Вход на странице авторизации
    NAME_PLCHOLDER = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/label"   # названия плейсхолдеров на странице регистрации
    EMAIL_PLCHOLDER = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/label"
    PASS_PLCHOLDER = By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/label"
    NAME_INPUT_AUTH = By.NAME, "name"   # инпут Email на странице авторизации
    PSWRD_INPUT_AUTH = By.NAME, "Пароль"   # инпут Пароль на странице авторизации
    ENTER_BUTTON = By.XPATH, "/html/body/div[1]/div/main/div/form/button"   # кнопка Войти на странице авторизации
    SECTION_1 = By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']"   # секция Соберите бургер на главной
    PROFILE_BUTTON = By.XPATH, ".//header/nav/a[@class = 'AppHeader_header__link__3D_hX']"   # кнопка Личный кабинет на главной
    ENTER_BUTTON_2 = By.CLASS_NAME, "Auth_link__1fOlj"   # кнопка Войти на странице регистрации/восстановления пароля
    ASSEMBLE_BURGER = By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"   # заголовок секции Соберите бургер на главной
    SECTION_2 = By.XPATH, ".//section[2]/ul[@class ='BurgerConstructor_basket__list__l9dp_']"   # список с элементами имеющими заголовки Перетяните булочку сюда на главной
    RESET_PSWRD_BUTTON = By.XPATH, ".//main/div/div/p[2]/a[@class = 'Auth_link__1fOlj']"   # кнопка Восстановить пароль на странице авторизации
    DRAG_BUN_IMG = By.XPATH, ".//img[@class = 'constructor-element__image']"   # анимированный элемент в списке с элементами имеющими заголовки Перетяните булочку сюда
    CONSTR_BUTTON = By.XPATH, ".//p[text() = 'Конструктор']"   # кнопка Конструктор в хэдере
    LOGO_BUTTON = By.XPATH, ".//div/a"   # логотип Stellar burgers в хедэре
    MAKE_ORDER_BUTTON = By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button"   # кнопка Оформить заказ на главной
    LOGOUT_BUTTON = By.XPATH, "/html/body/div[1]/div/main/div/nav/ul/li[3]/button"    # кнопка Выход в Личной Кабинете
    SAUCES_SPAN = By.XPATH, ".//span[text() = 'Соусы']"   # cпан Соусы в секции Соберите бургер на главной
    INGR_LIST_2 = By.XPATH, ".//div/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'][2]"
    FILLINGS_SPAN = By.XPATH, ".//span[text() = 'Начинки']"   # cпан Начинки в секции Соберите бургер на главной
    FILLINGS_SPAN_2 = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[3]"
    INGR_LIST_3 = By.XPATH, ".//div/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'][3]"
    ROLLS_SPAN = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[1]"   # cпан Булки в секции Соберите бургер на главной
    INGR_LIST_1 = By.XPATH, ".//div/ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'][1]"
    INGR_OBJECT = By.XPATH,"/html/body/div[1]/div/main/section[1]/div[2]/ul[1]/a[2]"   # отдельный ингредиент контейнера в секции Соберите бургер на главной
    MENU_CONTAINER = By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']"   # контейнер с ингредиентами в секции Соберите бургер на главной
    MC_LAST_ELEMENT = By.XPATH, ".//ul[3]/a[last()]"    # последний ингредиент контейнера в секции Соберите бургер на главной
    DESCENDANTS_UL = By.XPATH, ".//ul//span[@class = 'constructor-element__row']"   # искомый элемент
    FILLINGS_INGR_2 = By.XPATH, "/html/body/div[1]/div/main/section[1]/div[2]/ul[3]/a[2]"   #список ингредиентов в разделе Начинки контейнера в секции Соберите бургер на главной




