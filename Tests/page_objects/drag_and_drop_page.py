from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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

def drag_and_drop_column(driver_instance):
    source1 = driver_instance.find_element(By.ID, columnA)
    action = ActionChains(driver_instance)


def assert_drag_and_drop(driver_instance):
    target1 = driver_instance.find_element(By.ID, 'column-b')
    assert "B!" in target1.text
