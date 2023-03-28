from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
class CheckOut:
    textbox_firstname_id = "first-name"
    textbox_lastname_id = "last-name"
    textbox_zippostalcode_id = "postal-code"
    button_continue_id = "continue"


    def __init__ (self,driver): #creating the constructor 
        self.driver=driver 

    def setFirstNamee(self, firstnamee):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(Keys.BACK_SPACE, firstnamee)

    def setLastNamee(self, lastnamee):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(Keys.BACK_SPACE, lastnamee)

    def setZipPostalCodee(self, zippostalcodee):
        self.driver.find_element(By.ID, self.textbox_zippostalcode_id).send_keys(Keys.BACK_SPACE, zippostalcodee)

    def clickContinuee(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()


