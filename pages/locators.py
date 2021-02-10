from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_CONFIRM = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    CART_COST = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main>p[class="price_color"]')
