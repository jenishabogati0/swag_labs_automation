from selenium.webdriver.common.by import By

class HomePage:
    button_add_to_cart_id = "add-to-cart-sauce-labs-backpack"
    button_view_cart_xpath = "//a[@class = 'shopping_cart_link']"
    button_click_checkout_id = "checkout"

    def __init__(self, driver):
        self.driver = driver

    def clickAddtoCart(self):
        self.driver.find_element(By.ID, self.button_add_to_cart_id).click()

    def clickShoppingCart(self):
        self.driver.find_element(By.XPATH, self.button_view_cart_xpath).click()

    def clickCheckOut(self):
        self.driver.find_element(By.ID, self.button_click_checkout_id).click()

    