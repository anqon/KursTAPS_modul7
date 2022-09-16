import unittest

from selenium import webdriver
from Tests.page_objects import main_page,data_picker,hovers_page,inputs_page,basic_auth_page,iframe_page,checkboxes_page,form_page,dropdown_list_page,key_presses_page,drag_and_drop_page,add_remove_elements_page,status_codes_page
from time import sleep
from Tests.helpers.support_functions import *



class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = 'http://simpletestsite.fabrykatestow.pl/index.html'
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
        checkboxes_page.checkbox1_click_if_unchecked(self.driver)

    def test5_checkboxes2_click_if_checked(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        checkboxes_page.checkbox2_click_if_checked(self.driver)

    def test6_data_picker(self):
        self.driver.find_element(By.ID, 'datepicker-header').click()
        self.driver.find_element(By.XPATH, '//*[@id="start"]')

    def test7_hovers_content_visibility(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_displayed(self.driver))

    def test8_hovers_first_pic_and_click_link(self):
        hovers_page.click_hovers_tab(self.driver)
        hovers_page.hover_over_first_pic_and_click(self.driver)
        self.assertTrue(hovers_page.error_page(self.driver))
        sleep(3)

    def test9_hovers_second_pic_and_click_link(self):
        hovers_page.click_hovers_tab(self.driver)
        hovers_page.hover_over_second_pic_and_click(self.driver)
        self.assertTrue(hovers_page.error_page(self.driver))

    def test10_hovers_third_pic_and_click_link(self):
        hovers_page.click_hovers_tab(self.driver)
        hovers_page.hover_over_third_pic_and_click(self.driver)
        self.assertTrue(hovers_page.error_page(self.driver))

    def test11_inputs_content_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.inputs_content_visibility(self.driver))

    def test12_inputs_send_correct_value(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_value_to_input(self.driver))

    def test13_inputs_send_correct_value(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_value_to_input(self.driver))

    def test14_basic_auth_visibility(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_display(self.driver))

    def test15_basic_auth_correct_logged(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        basic_auth_page.correct_login_data(self.driver)
        self.assertTrue(basic_auth_page.correct_login_page(self.driver))

    def test16_basic_auth_incorrect_logged(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        basic_auth_page.incorrect_login_data(self.driver)
        self.assertTrue(basic_auth_page.incorrect_login_info(self.driver))

    def test17_basic_auth_correct_logged_return_to_main_page_button(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        basic_auth_page.correct_login_data(self.driver)
        basic_auth_page.return_to_main_page_button(self.driver)
        self.assertTrue(main_page.wait_for_visibility_of_main_page_content(self.driver))

    def test18_form_page_content_visibility(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visibility(self.driver))

    def test19_form_page_submit_user_data(self):
        form_page.click_form_tab(self.driver)
        form_page.submit_user_data(self.driver)
        form_page.alert_accept(self.driver)

    def test20_dropdown_list_content_visibility(self):
        dropdown_list_page.click_dropdown_list(self.driver)
        self.assertTrue(dropdown_list_page.dropdown_list_content_visibility(self.driver))

    def test21_dropdown_list_select_option1(self):
        dropdown_list_page.click_dropdown_list(self.driver)
        dropdown_list_page.select_option1_from_dropdown_list(self.driver)
        dropdown_list_page.assert_select(self.driver)

    def test22_key_presses_content_visibility(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visibility(self.driver))

    def test23_tested_correct_key_presses_Enter_test(self):
        key_presses_page.click_key_presses_tab(self.driver)
        key_presses_page.key_presses_test_Enter(self.driver)
        self.assertTrue(key_presses_page.correct_key_presses_result(self.driver))

    def test24_drag_and_drop_content_visibility(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visibility(self.driver))

    def test25_drag_and_drop_changed(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.check_drag_and_drop(self.driver))

    def test26_add_remove_elements_content_visibility(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_elements_content_visibility(self.driver))

    def test27_add_element(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        add_remove_elements_page.add_element_test(self.driver)
        self.assertTrue(add_remove_elements_page.added_element_is_displayed(self.driver))

    def test28_delete_element(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        add_remove_elements_page.add_element_test(self.driver)
        self.assertTrue(add_remove_elements_page.added_element_is_displayed(self.driver))
        add_remove_elements_page.delete_added_element(self.driver)
        self.assertTrue(add_remove_elements_page.element_invisible(self.driver))

    def test29_data_picker_visibility(self):
        data_picker.click_data_picker_tab(self.driver)
        self.assertTrue(data_picker.data_picker_content_visibility(self.driver))

    def test30_data_picker_correct_value(self):
        data_picker.click_data_picker_tab(self.driver)
        data_picker.data_picker_correct_test(self.driver)

    def test31_data_picker_incorrect_value(self):
        data_picker.click_data_picker_tab(self.driver)
        data_picker.data_picker_incorrect_test(self.driver)

    def test32_status_codes_content_visibility(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visibility(self.driver))

    def test33_status_codes_200(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.status_codes_200_click_button(self.driver)
        status_codes_page.status_code_200_error_expected(self.driver)

    def test34_status_codes_305(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.status_codes_305_clik_button(self.driver)
        status_codes_page.status_code_305_error_expected(self.driver)

    def test35_status_codes_404(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.status_codes_404_click_button(self.driver)
        status_codes_page.status_code_404_error_expected(self.driver)

    def test36_status_codes_500(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.status_codes_500_click_button(self.driver)
        status_codes_page.status_code_500_error_expected(self.driver)

    def test37_click_iframe(self):
        iframe_page.click_iframe_tag(self.driver)
        self.assertTrue(iframe_page.iframe_content_visibility(self.driver))

    def test38_iframe_click_button1(self):
        iframe_page.click_iframe_tag(self.driver)
        self.assertTrue(iframe_page.click_button1_inside_iframe(self.driver))
        iframe_page.make_screen(self.driver)

    def test39_iframe_click_button2(self):
        iframe_page.click_iframe_tag(self.driver)
        self.assertTrue(iframe_page.click_button2_inside_iframe(self.driver))
        iframe_page.make_screen(self.driver)

