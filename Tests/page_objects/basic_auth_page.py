from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By

username = 'admin'
password = 'admin'
basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
username_field = 'ba_username'
password_field = 'ba_password'
login_button = '//*[@id="content"]/button'
not_loggedin_message = 'loginFormMessage'
loggedin_message = 'loggedInMessage'
return_main_page_button = 'retrun button'


#cliknięcie w tab
def click_basic_auth_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_tab)
    elem.click()


#content visibility
def basic_auth_content_display(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_content)
    return elem.is_displayed()


#poprawne logowanie
def correct_login_data(driver_instance):
    elem_username = driver_instance.find_element(By.ID, username_field)
    elem_username.send_keys(username)
    elem_password = driver_instance.find_element(By.ID, password_field)
    elem_password.send_keys(password)
    elem_login_button = driver_instance.find_element(By.XPATH, login_button)
    elem_login_button.click()


def correct_login_page(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, loggedin_message)
    return elem.is_displayed()

#błędne logowanie
def incorrect_login_data(driver_instance):
    elem_username = driver_instance.find_element(By.ID, username_field)
    elem_username.send_keys('aaa')
    elem_password = driver_instance.find_element(By.ID, password_field)
    elem_password.send_keys('aaa')
    elem_login_button = driver_instance.find_element(By.XPATH, login_button)
    elem_login_button.click()


def incorrect_login_info(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, not_loggedin_message)
    return elem.is_displayed()

#powrót z poprawnego logowanie - wyświetlenie main_page
def return_to_main_page_button(driver_instance):
    elem = driver_instance.find_element(By.ID, return_main_page_button)
    elem.click()