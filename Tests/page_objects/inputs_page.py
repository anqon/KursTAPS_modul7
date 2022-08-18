from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By

inputs_tab = 'inputs-header'
inputs_content = 'inputs-content'
inputs_box = '//*[@id="inputs-content"]/div/input'

def click_inputs_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, inputs_tab)
    elem.click()


def inputs_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, inputs_content)
    return elem.is_displayed()


def send_correct_value_to_input(driver_instance):
    wait_for_clicable_of_element_by_xpath(driver_instance, '//*[@id="inputs-content"]/div/input')
    elem = driver_instance.find_element(By.XPATH, inputs_box)
    elem.send_keys('12345')
    if elem.get_attribute('value') == '12345':
        return True
    else:
        return False

def send_incorrect_value_to_input(driver_instance):
    wait_for_clicable_of_element_by_xpath(driver_instance, '//*[@id="inputs-content"]/div/input')
    elem = driver_instance.find_element(By.XPATH, inputs_box)
    elem.send_keys('abc')
    if 'abc' == elem.get_attribute('value'):
        return False
    else:
        return True
