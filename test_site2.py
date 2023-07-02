from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.get(URL)

# input_login = driver.find_element(By.ID,  'user-name')
# input_password = driver.find_element(By.ID,  'password')
# input_login.send_keys(LOGIN)
# input_password.send_keys(PASSWORD)
#
# log_button = driver.find_element(By.ID,  'login-button')
# log_button.click()

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
def open_page(driver, url):
    driver.get(URL)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID,  locator)
def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

def element_send_key(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

def login(driver, name, password):
    element_send_key(driver, 'user-name', name)
    element_send_key(driver, 'password', password)
    element_click(driver, 'login-button')

driver = get_driver()
open_page(driver, URL)
#open_login_page()
login(driver=driver, name=LOGIN, password=PASSWORD)

driver.quit()