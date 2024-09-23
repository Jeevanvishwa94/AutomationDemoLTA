from Pageobject.join_us_page import ADEJoinUs
from testcase.base_test import BaseTest
from utilities.test_data import TestData
 
class Testjoinuspage(BaseTest):
    def test_joinus_page(self):  
        ade_joinus_page= ADEJoinUs(self.driver)
        ade_joinus_page.ade_username(TestData.Username)
        ade_joinus_page.ade_password(TestData.Password)
        ade_joinus_page.click_ade_login()
        ade_joinus_page.Accept_all_cookies()
        ade_joinus_page.click_on_joinus()
        ade_joinus_page.enter_the_joinnow()
        ade_joinus_page.joinnow_first_name("Jeeva")
        ade_joinus_page.now_last_name("kvj")
        ade_joinus_page.enter_the_date("04")
        ade_joinus_page.enter_the_month("04")
        ade_joinus_page.enter_the_year("1994")
        ade_joinus_page.click_on_the_gender()
        ade_joinus_page.enter_the_email("jeevan.v@verolt.com")
        ade_joinus_page.create_a_username("Viswa094")
        ade_joinus_page.create_a_password("Keni@123")
        # ade_joinus_page.click_robot_button()
        # ade_joinus_page.click_join_now_button()
        ade_joinus_page .click_join_us_button_js()