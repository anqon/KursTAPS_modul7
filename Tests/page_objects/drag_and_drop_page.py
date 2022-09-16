from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
columnA = 'column-a'
columnB = 'column-b'
first_column_text = '//*[@id="column-a"]/header'
second_column_text = '523' \
                     '//*[@id="column-b"]/header'
def click_drag_and_drop_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_content)
    return elem.is_displayed


def check_drag_and_drop(driver_instance):
    driver_instance.implicitly_wait(10)

    with open(os.path.abspath('drag_and_drop.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    sleep(2)
    return True

