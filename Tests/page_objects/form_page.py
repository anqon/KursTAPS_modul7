from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


form_tab = 'form-header'
form_conttent = 'form-content'
first_name = 'fname'
first_name_data = 'aaa'
last_name = 'lname'
last_name_data = 'bbb'
submit = 'formSubmitButton'


def click_form_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, form_tab)
    elem.click()


def form_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, form_conttent)
    return elem.is_displayed()


def submit_user_data(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, form_conttent)
    fname = driver_instance.find_element(By.ID, first_name)
    fname.send_keys(first_name_data)
    lname = driver_instance.find_element(By.ID, last_name)
    lname.send_keys(last_name_data)
    submit_button = driver_instance.find_element(By.ID, submit)
    submit_button.click()


def alert_accept(driver_instance):
    alert = Alert(driver_instance)
    print('Komunikat ze strony http://simpletestsite.fabrykatestow.pl/: ' + alert.text)
    alert.accept()