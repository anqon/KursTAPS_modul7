from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


dropdown_list_tab = 'dropdownlist-header'
dropdown_list_content = 'dropdownlist-content'
select_an_option = 'dropdown'
option1 = '//*[@id="dropdown"]/option[1]'
option2 = '//*[@id="dropdown"]/option[2]'


def click_dropdown_list(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, dropdown_list_tab)
    elem.click()


def dropdown_list_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, dropdown_list_content)
    return elem.is_displayed


def select_option1_from_dropdown_list(driver_instance):
    elem_list = Select(driver_instance.find_element(By.ID,select_an_option))
    wait_for_visibility_of_element_by_id(driver_instance, select_an_option)
    elem_list.select_by_index(1)
    sleep(2)


def assert_select(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, select_an_option)
    elem.text
    print(elem)