from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By

home_content = 'accordion_child'
tutaj_link = '//*[@id="test-content"]/div/p/a'

def wait_for_visibility_of_main_page_content(driver_instance):
    elem = wait_for_visibility_of_element_by_class_name(driver_instance, home_content)
    return elem.is_displayed()


def link_tutaj_clicable(driver_instance):
    elem = wait_for_clicable_of_element_by_xpath(driver_instance, tutaj_link)
    elem.click()


def page_open_after_click_tutaj(driver_instance):
    elem = driver_instance.title
    if elem == 'KURS TAPS - Fabryka Testów':
        return True
    else:
        return False