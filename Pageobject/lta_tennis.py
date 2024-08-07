import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Pageobject.base_page import BasePage
from utilities.Tennis_cout import LTALocators






class LTATennisPage(BasePage):
    def __init__(self, driver):
        self.locate = LTALocators
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

    def compete_module(self):
        self.wait_for_element(self.locate.junior).click()
        time.sleep(2)

    def LTA_Youth_Competitions(self):
        self.click(self.locate.youth_Competitions)
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    
    def individual_match_competition(self):
        self.click(self.locate.youth_match_play)
        time.sleep(2)

    def hover_over_element(self, element):
        super().hover_over_element(element)

    def enter_a_LTA(self):
        self.wait_for_element(self.locate.submit_lta).click()
        time.sleep(2)
    
    def lta_tennis_privacy(self):
        self.click(self.locate.accept)
        time.sleep(2)

    def tournaments_module(self):
        self.click(self.locate.tournaments)
        time.sleep(2)
    
    def search_tournaments(self):
        self.wait_for_element(self.locate.entry_open).click()
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
    
    def leamington_lta_youth(self):
        self.click(self.locate.leamington_tennis_club)
        time.sleep(2)
    
    def enter_leamington_lta(self):
        self.click(self.locate.enter_leamington)
        time.sleep(2)

    
