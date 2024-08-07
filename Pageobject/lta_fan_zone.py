import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Pageobject.base_page import BasePage
from utilities.fan_zone import LTAFanZoneLocators


class TournamentCalender(BasePage):
    def __init__(self, driver):
        self.locate = LTAFanZoneLocators
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

    def hover_over_element(self, element):
        super().hover_over_element(element)
    
    def all_tournaments(self):
        self.click(self.locate.tournaments)
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    def tournament_calender(self):
        self.click(self.locate.calender)
        time.sleep(2)

    def tournament_month(self):
        self.wait_for_element(self.locate.month).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    
    def hover_over_element(self, element):
        super().hover_over_element(element)

    def radio_button_checkbox(self):
        self.click(self.locate.radio_button_apply)
        time.sleep(2)

    def location_dropdown(self):
        self.click(self.locate.location)
        time.sleep(2)
    
    def locate_checkbox(self):
        self.click(self.locate.checkbox)
        time.sleep(2)

    def location_button_apply(self):
        self.click(self.locate.location_apply)
        time.sleep(2)

    def event_type_in_calender(self):
        self.click(self.locate.event_type)
        time.sleep(2)

    def event_checkbox_click(self):
        self.click(self.locate.event_checkbox)
        time.sleep(2)

    def event_type_enter(self):
        self.click(self.locate.event_apply)
        time.sleep(2)