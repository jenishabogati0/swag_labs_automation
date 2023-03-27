from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
s = Service('/home/leapfrog/Desktop/python-automation/src/chromedriver/chromedriver')
driver = webdriver.Chrome(service=s, options=options) #creating object for the chrome class
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/") #getting the URL
driver.maximize_window()
driver.find_element(By.NAME, 'user-name').send_keys("standard_user") #finding the username field and passing value
driver.find_element(By.NAME, 'password').send_keys("secret_sauce") #finding the password field and passing value
driver.find_element(By.ID, 'login-button').click() #click login
time.sleep(5)
driver.find_element(By.XPATH, value='(//button[@class="btn btn_primary btn_small btn_inventory"])[1]').click() #Add item 1
driver.find_element(By.XPATH, value='(//button[@class="btn btn_primary btn_small btn_inventory"])[2]').click() #Add item delay
driver.find_element(By.XPATH, value='//a[@class="shopping_cart_link"]').click() #View Cart
time.sleep(5)
driver.find_element(By.XPATH, value='(//button[@class="btn btn_secondary btn_small cart_button"])[2]').click() #Remove item 5
time.sleep(5)
driver.find_element(By.XPATH, value='//div[@class="inventory_item_name"]').click() #View item 1
time.sleep(2)
driver.find_element(By.XPATH, value='//a[@class="shopping_cart_link"]').click() #View Cart
driver.find_element(By.ID, 'checkout').click() #Click Checkout
time.sleep(5)
driver.find_element(By.XPATH, value='(//input[@class="input_error form_input"])[1]').send_keys('Jenny') #Add first name
driver.find_element(By.XPATH, value='(//input[@class="input_error form_input"])[2]').send_keys('Bogati') #Add last name
driver.find_element(By.XPATH, value='(//input[@class="input_error form_input"])[3]').send_keys('44600') #Add zip/postal code
driver.find_element(By.NAME, 'continue').click() #Click continue
time.sleep(5)
driver.find_element(By.NAME, 'finish').click() #Click finish
time.sleep(5)
driver.find_element(By.NAME, 'back-to-products').click() #Click back to homepage
time.sleep(5)
driver.quit()