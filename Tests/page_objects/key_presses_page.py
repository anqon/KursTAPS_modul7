from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


key_presses_tab = 'keypresses-header'
key_presses_content =  'keypresses-content'
key_presses_field = 'target'
key_press_result = 'keyPressResult'

def click_key_presses_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_presses_tab)
    elem.click()


def key_presses_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_presses_content)
    return elem.is_displayed()


def key_presses_test_Enter(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_presses_field)
    elem.click()
    elem.send_keys(Keys.ENTER)


def correct_key_presses_result(driver_instance):
    result = driver_instance.find_element(By.ID, key_press_result)
    if result.text == "You entered: ENTER":
        return True
    else:
        return False
