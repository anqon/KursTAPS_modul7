from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By


add_remove_elements_tab = 'addremoveelements-header'
add_remove_elements_content = 'addremoveelements-content'
new_element = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button'


def click_add_remove_elements_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,add_remove_elements_tab)
    elem.click()


def add_remove_elements_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,add_remove_elements_content)
    return elem.is_displayed()


def add_element_test(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance,new_element)
    elem = driver_instance.find_element(By.XPATH, new_element)
    elem.click()


def added_element_is_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, added_element)
    return elem.is_displayed()


def delete_added_element(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, added_element)
    elem = driver_instance.find_element(By.XPATH, added_element)
    elem.click()


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_by_xpath(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False