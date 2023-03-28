#from selenium import webdriver
#page object class for login page
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
class LoginPage:
    textbox_username_name= "user-name"
    textbox_password_name= "password"
    button_login_id= "login-button" #all the locators of login page are identified

    def __init__ (self,driver): #creating the constructor 
        self.driver=driver #self.driver will be used to write all action methods for the above login elements

    def setUserNamee(self,username): #creating the action method and these action methods we have to call from actual test case later
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(Keys.BACK_SPACE, username)

    def setPasswordd(self,password): 
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(Keys.BACK_SPACE,password)

    def clickLoginn(self):
        self.driver.find_element(By.ID, self.button_login_id).click()
