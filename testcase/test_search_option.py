from Pageobject.lta_search_logo import LTASearchPage
from testcase.base_test import BaseTest
from utilities.test_data import TestData


class TestSearchLogin(BaseTest):
    def test_search_page(self):  
        lta_search_page= LTASearchPage(self.driver)
        lta_search_page.lta_username(TestData.Username)
        lta_search_page.lta_password(TestData.Password)
        lta_search_page.click_lta_login()
        lta_search_page.Accept_all_cookies()       
        lta_search_page.searching_logo()
        lta_search_page.click_search_button()
        lta_search_page.search_LTA_box("Juniors")
        lta_search_page.submit_search()
        element = lta_search_page.find_element(*lta_search_page.locate.view_results)
        lta_search_page.hover_over_element(element)
        # lta_search_page.junior_module_option()
        