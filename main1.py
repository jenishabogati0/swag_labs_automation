from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
s = Service('/home/leapfrog/Desktop/python-automation/src/chromedriver/chromedriver')
driver = webdriver.Chrome(service=s, options=options) #creating object for the chrome class
driver.maximize_window()
driver.get("https://www.saucedemo.com/") #getting the URL

clickable = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "login-button")))
#clickable = driver.find_element(By.ID, "login-button")
ActionChains(driver).double_click(clickable).perform()

clickandhold = driver.find_element(By.ID, "user-name")   
ActionChains(driver).click_and_hold(clickandhold).perform()

driver.find_element(By.ID , 'user-name').send_keys("standard_user")
driver.find_element(By.ID , 'password').send_keys("secret_sauce")

ActionChains(driver).click(clickable).perform()

#page refresh, forward and backward
driver.refresh()
#time.sleep(2)
driver.back()
#time.sleep(2)
driver.forward()
#time.sleep(2)

#hover
hoverable = driver.find_element(By.XPATH, "(//div[@class= 'inventory_item_name'])[1]")
ActionChains(driver).move_to_element(hoverable).perform()

#scroll_by_given_amount
footer = driver.find_element(By.TAG_NAME, "footer")
delta_y = footer.rect['y']
ActionChains(driver).scroll_by_amount(0, delta_y).perform()
#time.sleep(2)

#right_click
#ActionChains(driver).context_click(hoverable).perform()

driver.find_element(By.ID, 'react-burger-menu-btn').click()
#time.sleep(2)

# driver = webdriver.Chrome(service=s, options=options) #reinitializing the driver if you have closed the driver already
# driver.get("https://nxtgenaiacademy.com/alertandpopup/")

#visiting new URL and 
driver.get("https://nxtgenaiacademy.com/alertandpopup/")
driver.find_element(By.XPATH, '//button[@name = "alertbox"]').click()
#time.sleep(2)
alert = driver.switch_to.alert
text = alert.text
alert.accept()

#take_screenshot
driver.save_screenshot('./image.png')
#time.sleep(2)

#file_upload
driver.get("http://www.csm-testcenter.org/test?do=show&subdo=common&test=file_upload")
driver.find_element(By.XPATH, '(//input[@type = "file"])[1]').send_keys("/home/leapfrog/Desktop/python-automation/src/image.png")
#time.sleep(2)
driver.find_element(By.ID, 'button').submit()
if(driver.page_source.find("File Upload Finished")):
    print("file upload SUCCESS")
else:
    print("file upload NOT SUCCESSFUL")
#time.sleep(2)

#find_element_by_linktext
driver.get("https://www.w3schools.com/")
driver.find_element(By.LINK_TEXT,'Learn HTML').click()

#print_matching_child_webelements_within_the_context_of_parent_element
element = driver.find_element(By.TAG_NAME, 'div')
elements = driver.find_elements(By.TAG_NAME, 'p')
for e in elements:
    print(e.text)

#Add text in input textbox, select checkbox, select radiobutton and select an option from the dropdown
driver.get("https://tutorial.techaltum.com/htmlform.html")
#time.sleep(2)
driver.find_element(By.ID, "uname").send_keys("jenny")
driver.find_element(By.XPATH, "(//input[@type='checkbox'])[5]").click()
driver.find_element(By.XPATH, "(//input[@type='radio'])[11]").click()
select = Select(driver.find_element(By.ID, "city"))
select.select_by_visible_text("New Delhi")
#time.sleep(2)
driver.close()



