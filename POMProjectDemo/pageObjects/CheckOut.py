from selenium.webdriver.common.by import By
class CheckOut:
    textbox_firstname_id = "first-name"
    textbox_lastname_id = "last-name"
    textbox_zippostalcode_id = "postal-code"
    button_continue_id = "continue"


    def __init__ (self,driver): #creating the constructor 
        self.driver=driver 

    def setFirstNamee(self, firstnamee):
        self.find_element_by_id(self.textbox_firstname_id).clear()
        self.find_element_by_id(self.textbox_firstname_id).send_keys(firstnamee)

    def setLastNamee(self, lastnamee):
        self.find_element_by_id(self.textbox_lastname_id).clear()
        self.find_element_by_id(self.textbox_lastname_id).send_keys(lastnamee)

    def setZipPostalCodee(self, zippostalcodee):
        self.find_element_by_id(self.textbox_zippostalcode_id).clear()
        self.find_element_by_id(self.textbox_zippostalcode_id).send_keys(zippostalcodee)

    def clickContinuee(self):
        self.find_element_by_id(self.button_continue_id).click()
    
    def find_element_by_id(self, value):
        return self.driver.find_element(By.ID, value)

