from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By


data_picker_tab = 'datepicker-header'
data_picker_content = 'datepicker-content'
data_picker_field = '//*[@id="start"]'

def click_data_picker_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,data_picker_tab)
    elem.click()

def data_picker_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,data_picker_content)
    return elem.is_displayed()

def data_picker_correct_test(driver_instance):
    elem = wait_for_clicable_of_element_by_xpath(driver_instance,data_picker_field)
    elem.click()
    elem.send_keys('12-12-2020')
    input = elem.get_attribute('value')
    print(input)
    if '2020-11-12' == input:
        return True
    else:
        return False


def data_picker_incorrect_test(driver_instance):
    elem = wait_for_clicable_of_element_by_xpath(driver_instance,data_picker_field)
    elem.click()
    elem.send_keys('33.33.1111')
    input = elem.get_attribute('value')
    if '33.33.1111' == input:
        return False
    else:
        return True