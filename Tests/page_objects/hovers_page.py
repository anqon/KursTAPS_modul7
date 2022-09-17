from Tests.helpers.support_functions import *


hover_header = 'hovers-header'
hover_content = 'hovers-content'
first_pic = '//*[@id="hovers-content"]/div/div[1]/img'
first_pic_link = '//*[@id="hovers-content"]/div/div[1]/div/a'
second_pic = '//*[@id="hovers-content"]/div/div[2]/img'
second_pic_link = '//*[@id="hovers-content"]/div/div[2]/div/a'
third_pic = '//*[@id="hovers-content"]/div/div[3]/img'
third_pic_link = '//*[@id="hovers-content"]/div/div[3]/div/a'


def click_hovers_tab(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, hover_header)
    elem.click()


def hovers_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance,hover_content)
    return elem.is_displayed()


def hover_over_first_pic_and_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance,first_pic)
    hover_over_element_by_xpath(driver_instance, first_pic)
    elem = driver_instance.find_element(By.XPATH, first_pic_link).click()


def hover_over_second_pic_and_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance,second_pic)
    hover_over_element_by_xpath(driver_instance, second_pic)
    elem = driver_instance.find_element(By.XPATH, second_pic_link).click()


def hover_over_third_pic_and_click(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance,third_pic)
    hover_over_element_by_xpath(driver_instance, third_pic)
    elem = driver_instance.find_element(By.XPATH, third_pic_link).click()


def error_page(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, 'container')
    return elem.is_displayed()