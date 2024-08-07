from Pageobject.booking_page import TennisBookingCourt
from testcase.base_test import BaseTest
from utilities.test_data import TestData


class TestBookingCourt(BaseTest):

    def test_booking_tennis_court(self):
        lta_booking_page = TennisBookingCourt(self.driver)
        lta_booking_page.lta_username(TestData.Username)
        lta_booking_page.lta_password(TestData.Password)
        lta_booking_page.click_lta_login()
        lta_booking_page.Accept_all_cookies()
        element = lta_booking_page.find_element(*lta_booking_page.locate.play)
        lta_booking_page.hover_over_element(element)
        lta_booking_page.play_module()
        element = lta_booking_page.find_element(*lta_booking_page.locate.remove_location)
        lta_booking_page.hover_over_element(element)
        lta_booking_page.checkbox_locate("London,UK")
        lta_booking_page.check_box_dropdown()
        # lta_booking_page.checkbox_locate()
        lta_booking_page.click_the_calender()
        element = lta_booking_page.find_element(*lta_booking_page.locate.enter_date)
        lta_booking_page.hover_over_element(element)
        lta_booking_page.enter_the_date()
        lta_booking_page.time_drop_options()
        lta_booking_page.booking_time_slot()
        lta_booking_page.find_a_court()
        
        

        