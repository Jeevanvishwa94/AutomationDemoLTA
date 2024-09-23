from Pageobject.singin_page import SiginPage
from testcase.base_test import BaseTest
from utilities.test_data import TestData
 
class Testjoinuspage(BaseTest):
    def test_joinus_page(self):  
        ppe_sign_page= SiginPage(self.driver)
        ppe_sign_page.ppe_username(TestData.Username)
        ppe_sign_page.ppe_password(TestData.Password)
        ppe_sign_page.click_ppe_login()
        ppe_sign_page.Accept_all_cookies()
        ppe_sign_page.Click_signin_button()
        ppe_sign_page.signin_credential("vijay086")
        ppe_sign_page.enter_signin_credential("Vijayverolt@123")
        ppe_sign_page.ppe_username(TestData.Username)
        ppe_sign_page.ppe_password(TestData.Password)
        ppe_sign_page.click_ppe_login()
        ppe_sign_page.click_avator_button()
        ppe_sign_page.click_add_role_fun()
        ppe_sign_page.click_let_start_button()
        ppe_sign_page.click_parks_activators()
        # ppe_sign_page.click_teacher_radio_button()
        # ppe_sign_page.click_activator()
        # ppe_sign_page.click_next_button()
        # ppe_sign_page.click_get_start_button()
        # ppe_sign_page.click_student_button()
        # ppe_sign_page.click_next_button_again()
        # ppe_sign_page.click_senior_leader_button()
        # ppe_sign_page.click_school_pincode("N48 9EA")
    