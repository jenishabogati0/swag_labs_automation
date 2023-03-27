from selenium.webdriver.common.by import By

class HomePage:
    button_add_to_cart_id = "add-to-cart-sauce-labs-backpack"
    button_view_cart_xpath = "//a[@class = 'shopping_cart_link']"
    button_click_checkout_id = "checkout"

    def __init__(self, driver):
        self.driver = driver

    def clickAddtoCart(self):
        self.find_element_by_id(self.button_add_to_cart_id).click()

    def clickShoppingCart(self):
        self.find_element_by_class(self.button_view_cart_xpath).click()

    def clickCheckOut(self):
        self.find_element_by_id(self.button_click_checkout_id).click()

    def find_element_by_id(self, value):
        return self.driver.find_element(By.ID, value)
    
    def find_element_by_class(self, value):
        return self.driver.find_element(By.XPATH, value)
    
    