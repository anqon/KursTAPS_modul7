from Tests.helpers.support_functions import *
from selenium.webdriver.common.by import By


add_remove_elements_tab = 'addremoveelements-header'
add_remove_elements_content = 'addremoveelements-content'
add_element = '//*[@id="addremoveelements-content"]/div/div/button'
delete_element = '//*[@id="elements"]/button'


def click_add_remove_elements_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,add_remove_elements_tab)
    elem.click()

def add_remove_elements_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,add_remove_elements_content)
    return elem.is_displayed()

def add_element_test(driver_instance):
    elem = wait_for_clicable_of_element_by_xpath(driver_instance,add_element)
    elem.click()
#błąd 1 TypeError: visibility_of_element_located() takes 1 positional argument but 2 were given
def add_element_displayed(driver_instance):
    elem1 = wait_for_clicable_of_element_by_xpath(driver_instance, delete_element)
    return elem1.is_displayed()
#po zmianie na poniższy kod otrzymuje błąd 2  TypeError: Object of type function is not JSON serializable
    #elem1 = wait_for_clicable_of_element_by_xpath(driver_instance, delete_element)
    #return elem1.is_displayed()


def delete_element(driver_instance):
    elem = wait_for_clicable_of_element_by_xpath(By.XPATH, delete_element)
    elem.click()
    wait_for_invisibility_of_element_by_xpath(driver_instance,delete_element)

def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_by_xpath(driver_instance,delete_element)
        return True
    except NoSuchElementException:
        return False