from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#import pytest


def setup():
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome'
    s = Service('/home/leapfrog/Desktop/python-automation/src/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=s, options=options) #creating object for the chrome class
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver