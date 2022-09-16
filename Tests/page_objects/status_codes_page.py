from Tests.helpers.support_functions import *
import requests

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
code200 = '200siteAnchor'
code305 = '305siteAnchor'
code404 = '404siteAnchor'
code500 = '500siteAnchor'


def click_status_codes_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,status_codes_tab)
    elem.click()


def status_codes_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_codes_content)
    return elem.is_displayed()


def status_codes_200_click_button(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,code200)
    elem.click()


def status_code_200_error_expected(driver_instance):
    try:
        get_url = driver_instance.current_url
        code = requests.get(get_url)
        odp = code.status_code
        if odp == 200:
            print('status code: ' + str(odp))
            return True
        else:
            print('status code: ' + str(odp))
            return False
    except requests.ConnectionError:
        print("Can't connect to the site, try again later")
        return False


def status_codes_305_clik_button(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,code305)
    elem.click()


def status_code_305_error_expected(driver_instance):
    try:
        get_url = driver_instance.current_url
        code = requests.get(get_url)
        odp = code.status_code
        if odp == 305:
            print('status code: ' + str(odp))
            return True
        else:
            print('status code: ' + str(odp))
            return False
    except requests.ConnectionError:
        print("Can't connect to the site, try again later")
        return False


def status_codes_404_click_button(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,code404)
    elem.click()


def status_code_404_error_expected(driver_instance):
    try:
        get_url = driver_instance.current_url
        code = requests.get(get_url)
        odp = code.status_code
        if odp == 404:
            print('status code: ' + str(odp))
            return True
        else:
            print('status code: ' + str(odp))
            return False
    except requests.ConnectionError:
        print("Can't connect to the site, try again later")
        return False


def status_codes_500_click_button(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,code500)
    elem.click()


def status_code_500_error_expected(driver_instance):
    try:
        get_url = driver_instance.current_url
        code = requests.get(get_url)
        odp = code.status_code
        if odp == 500:
            print('status code: ' + str(odp))
            return True
        else:
            print('status code: ' + str(odp))
            return False
    except requests.ConnectionError:
        print("Can't connect to the site, try again later")
        return False