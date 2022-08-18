import unittest

from selenium import webdriver
from Tests.page_objects import main_page,data_picker,hovers_page,inputs_page,basic_auth_page,iframe_page,checkboxes_page,form_page,dropdown_list_page,key_presses_page,drag_and_drop_page,add_remove_elements_page

from selenium.webdriver.common.by import By
from time import sleep
from Tests.helpers.support_functions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = 'http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test1_home_content_visibility(self):
        self.assertTrue(main_page.wait_for_visibility_of_main_page_content(self.driver))

    def test2_home_link_tutaj_verify(self):
        main_page.link_tutaj_clicable(self.driver)
        self.assertTrue(main_page.page_open_after_click_tutaj(self.driver))
        self.url = self.driver.current_url
        print('Pomyślnie przekierowało na stronę '+self.url)


    def test3_checkboxes_content_visibility(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_content_visibility(self.driver))

    def test4_checkboxes1_click_if_not_checked(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_content_visibility(self.driver))
        checkboxes_page.checkbox1_click_if_unchecked(self.driver)

    def test5_checkboxes2_click_if_checked(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_content_visibility(self.driver))
        checkboxes_page.checkbox2_click_if_checked(self.driver)

    def test6_data_picker(self):
        self.driver.find_element(By.ID, 'datepicker-header').click()
        self.driver.find_element(By.XPATH, '//*[@id="start"]')


    def test7_hovers_content_visibility(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_displayed(self.driver))

    def test8_hovers_first_pic_and_click_link(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_displayed(self.driver))
        hovers_page.hover_over_first_pic_and_click(self.driver)
        self.assertTrue(hovers_page.error_page(self.driver))
        sleep(3)

    def test9_hovers_second_pic_and_click_link(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_displayed(self.driver))
        hovers_page.hover_over_second_pic_and_click(self.driver)
        self.assertTrue(hovers_page.error_page(self.driver))

    def test10_hovers_third_pic_and_click_link(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_displayed(self.driver))
        hovers_page.hover_over_third_pic_and_click(self.driver)
        self.assertTrue(hovers_page.error_page(self.driver))

    def test11_inputs_content_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.inputs_content_visibility(self.driver))

    def test12_inputs_send_correct_value(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.inputs_content_visibility(self.driver))
        self.assertTrue(inputs_page.send_correct_value_to_input(self.driver))

    def test13_inputs_send_correct_value(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.inputs_content_visibility(self.driver))
        self.assertTrue(inputs_page.send_incorrect_value_to_input(self.driver))

    def test14_basic_auth_visibility(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_display(self.driver))


    def test15_basic_auth_correct_logged(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_display(self.driver))
        basic_auth_page.correct_login_data(self.driver)
        self.assertTrue(basic_auth_page.correct_login_page(self.driver))

    def test16_basic_auth_incorrect_logged(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_display(self.driver))
        basic_auth_page.incorrect_login_data(self.driver)
        self.assertTrue(basic_auth_page.incorrect_login_info(self.driver))

    def test17_basic_auth_correct_logged_return_to_main_page_button(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_display(self.driver))
        basic_auth_page.correct_login_data(self.driver)
        self.assertTrue(basic_auth_page.correct_login_page(self.driver))
        basic_auth_page.return_to_main_page_button(self.driver)
        self.assertTrue(main_page.wait_for_visibility_of_main_page_content(self.driver))

    def test18_form_page_content_visibility(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visibility(self.driver))

    def test19_form_page_submit_user_data(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visibility(self.driver))
        form_page.submit_user_data(self.driver)
        form_page.alert_accept(self.driver)

    def test20_dropdown_list_content_visibility(self):
        dropdown_list_page.click_dropdown_list(self.driver)
        self.assertTrue(dropdown_list_page.dropdown_list_content_visibility(self.driver))


    def test21_dropdown_list_select_option1(self):
        dropdown_list_page.click_dropdown_list(self.driver)
        self.assertTrue(dropdown_list_page.dropdown_list_content_visibility(self.driver))
        dropdown_list_page.select_option1_from_dropdown_list(self.driver)
        dropdown_list_page.assert_select(self.driver)
        sleep(2)

    def test22_key_presses_content_visibility(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visibility(self.driver))

    def test23_tested_correct_key_presses_Enter_test(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visibility(self.driver))
        key_presses_page.key_presses_test_Enter(self.driver)
        self.assertTrue(key_presses_page.correct_key_presses_result(self.driver))

    def test25_drag_and_drop_content_visibility(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visibility(self.driver))

    def test26_drag_and_drop_content_visibility(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visibility(self.driver))
        source1 = self.driver.find_element(By.ID, 'column-a')
        target1 = self.driver.find_element(By.ID, 'column-b')
        action = ActionChains(self.driver)
        action.drag_and_drop(source1, target1).perform()
       # action.drag_and_drop_by_offset(source1, 170, 10).perform()
       # action.click_and_hold(source1).pause(2).move_to_element(target1).perform()
        self.assertEqual("A!", target1.text)



        #drag = WebDriverWait(self.driver, 20).until(
        #    EC.element_to_be_clickable((By.ID, "column-a")))
        #drop = WebDriverWait(self.driver, 20).until(
        #   EC.element_to_be_clickable((By.ID, "column-b")))
        #ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        sleep(4)

    def test27_add_remove_elements_content_visibility(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_elements_content_visibility(self.driver))

    def test27_add_element(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_elements_content_visibility(self.driver))
        add_remove_elements_page.add_element_test(self.driver)
        sleep(2)
        self.assertTrue(add_remove_elements_page.add_element_displayed(self.driver))
        sleep(2)

    def test28_delete_element(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_elements_content_visibility(self.driver))
        add_remove_elements_page.add_element_test(self.driver)
        add_remove_elements_page.delete_element(self.driver)
        self.assertTrue(wait_for_visibility_of_element_by_id(self.driver))
        sleep(3)



    def test30_data_picker_visibility(self):
        data_picker.click_data_picker_tab(self.driver)
        self.assertTrue(data_picker.data_picker_content_visibility(self.driver))


    def test31_data_picker_correct_value(self):
        data_picker.click_data_picker_tab(self.driver)
        self.assertTrue(data_picker.data_picker_content_visibility(self.driver))
        data_picker.data_picker_correct_test(self.driver)
        sleep(6)
    def test31_data_picker_incorrect_value(self):
        data_picker.click_data_picker_tab(self.driver)
        self.assertTrue(data_picker.data_picker_content_visibility(self.driver))
        data_picker.data_picker_incorrect_test(self.driver)
        sleep(6)

    def test32_click_iframe(self):
        iframe_page.click_iframe_tag(self.driver)
        self.assertTrue(iframe_page.iframe_content_visibility(self.driver))

    def test33_iframe_click_button1(self):
        iframe_page.click_iframe_tag(self.driver)
        self.assertTrue(iframe_page.click_button1_inside_iframe(self.driver))
        iframe_page.make_screen(self.driver)

    def test34_iframe_click_button2(self):
        iframe_page.click_iframe_tag(self.driver)
        self.assertTrue(iframe_page.click_button2_inside_iframe(self.driver))
        iframe_page.make_screen(self.driver)

