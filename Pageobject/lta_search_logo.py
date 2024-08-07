import time
from Pageobject.base_page import BasePage
from utilities.search_module_locators import SearchLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class LTASearchPage(BasePage):
    def __init__(self, driver):
        self.locate = SearchLocators
        self.actions = ActionChains(driver)
        super().__init__(driver)

    def lta_username(self, lta_username):
        self.set(self.locate.Username, lta_username)

    def lta_password(self, lta_password):
        self.set(self.locate.Password, lta_password)

    def click_lta_login(self):
        self.click(self.locate.Verify_button)
        time.sleep(2)

    def Accept_all_cookies(self):
        self.wait_for_element(self.locate.all_cookies).click()
        time.sleep(2)
        
    def searching_logo(self):
        self.click(self.locate.search_option)
        time.sleep(2)

    def click_search_button(self):
        self.click(self.locate.click_search_logo)
        time.sleep(2)

    def search_LTA_box(self, value):
        self.set(self.locate.lta_searchbox, value)
        time.sleep(2)

    def submit_search(self):
        self.click(self.locate.submit)
        time.sleep(2)

    def hover_over_element(self, element):
        super().hover_over_element(element)

    # def junior_module_option(self):
    #     self.click(self.locate.view_results)
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()

    
        