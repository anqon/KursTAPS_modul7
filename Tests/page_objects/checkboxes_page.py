from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By

checkboxes_tab = 'checkbox-header'
checkboxes_content = 'checkbox-content'
checkboxes = 'checkboxes'
checkbox1 = '//*[@id="checkboxes"]/input[1]'
checkbox2 = '//*[@id="checkboxes"]/input[2]'


def click_checkboxes_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, checkboxes_tab)
    elem.click()


def checkboxes_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, checkboxes_content)
    return elem.is_displayed()


def checkbox1_click_if_unchecked(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, checkboxes)
    elem = driver_instance.find_element(By.XPATH, checkbox1)
    if elem.get_attribute("checked") != "null":
        elem.click()


def checkbox2_click_if_checked(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, checkboxes)
    elem = driver_instance.find_element(By.XPATH, checkbox2)
    if elem.get_attribute("checked") == "true":
        elem.click()
