from Pageobject.lta_fan_zone import TournamentCalender
from testcase.base_test import BaseTest
from utilities.test_data import TestData


class TestFanZone(BaseTest):

    def test_fan_zone_calender(self):
        lta_fan_zone_page = TournamentCalender(self.driver)
        lta_fan_zone_page.lta_username(TestData.Username)
        lta_fan_zone_page.lta_password(TestData.Password)
        lta_fan_zone_page.click_lta_login()
        lta_fan_zone_page.Accept_all_cookies() 
        element = lta_fan_zone_page.find_element(*lta_fan_zone_page.locate.fan_zone)
        lta_fan_zone_page.hover_over_element(element)
        lta_fan_zone_page.all_tournaments()  
        lta_fan_zone_page.tournament_calender() 
        lta_fan_zone_page.tournament_month()
        lta_fan_zone_page.radio_button_checkbox()
        lta_fan_zone_page.location_dropdown()
        lta_fan_zone_page.locate_checkbox()
        lta_fan_zone_page.location_button_apply()
        lta_fan_zone_page.event_type_in_calender()
        lta_fan_zone_page.event_checkbox_click()
        lta_fan_zone_page.event_type_enter()