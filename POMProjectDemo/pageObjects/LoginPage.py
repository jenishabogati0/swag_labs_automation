#from selenium import webdriver
#page object class for login page
from selenium.webdriver.common.by import By
class LoginPage: 
    textbox_username_name= "user-name"
    textbox_password_name= "password"
    button_login_id= "login-button" #all the locators of login page are identified

    def __init__ (self,driver): #creating the constructor 
        self.driver=driver #self.driver will be used to write all action methods for the above login elements

    def setUserNamee(self,username): #creating the action method and these action methods we have to call from actual test case later
        self.find_element_by_name(self.textbox_username_name).clear()
        self.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setPasswordd(self,password): 
        self.find_element_by_name(self.textbox_password_name).clear()
        self.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clickLoginn(self):
        self.find_element_by_id(self.button_login_id).click()

    def find_element_by_name(self, value):
        return self.driver.find_element(By.NAME, value)
    
    def find_element_by_id(self, value):
        return self.driver.find_element(By.ID, value)
