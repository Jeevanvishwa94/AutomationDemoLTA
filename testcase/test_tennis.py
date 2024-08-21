from Pageobject.lta_tennis import LTATennisPage
from testcase.base_test import BaseTest
from utilities.test_data import TestData
from selenium.webdriver.common.by import By


class TestLogin(BaseTest):

    def test_lta_login(self):
        lta_tennis = LTATennisPage(self.driver)
        lta_tennis.lta_username(TestData.Username)
        lta_tennis.lta_password(TestData.Password)
        lta_tennis.click_lta_login()
        lta_tennis.Accept_all_cookies()       
        element = lta_tennis.find_element(*lta_tennis.locate.compete)
        lta_tennis.hover_over_element(element)
        lta_tennis.compete_module()
        lta_tennis.LTA_Youth_Competitions()
        lta_tennis.individual_match_competition()
        element = lta_tennis.find_element(*lta_tennis.locate.submit_lta)
        lta_tennis.hover_over_element(element)
        lta_tennis.enter_a_LTA()
        lta_tennis.lta_tennis_privacy()
        lta_tennis.tournaments_module()
        lta_tennis.search_tournaments()
        lta_tennis.leamington_lta_youth()
        lta_tennis.enter_leamington_lta()

        