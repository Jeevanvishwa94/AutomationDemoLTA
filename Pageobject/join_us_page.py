import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Pageobject.base_page import BasePage
from utilities.join_us_locators import ADEjoinLocators
 
class ADEJoinUs(BasePage):
    def __init__(self, driver):
        self.locate = ADEjoinLocators
        self.actions = ActionChains(driver)
        super().__init__(driver)
 
    def ade_username(self, ade_username):
        self.set(self.locate.Username, ade_username)
 
    def ade_password(self, ade_password):
        self.set(self.locate.Password, ade_password)
 
    def click_ade_login(self):
        self.click(self.locate.Verify_button)
        time.sleep(2)
 
    def Accept_all_cookies(self):
        self.wait_for_element(self.locate.all_cookies).click()
        time.sleep(2)
 
    def click_on_joinus(self):
        self.click(self.locate.join_us)
        time.sleep(2)
 
    def enter_the_joinnow(self):
        self.click(self.locate.join_now)
        time.sleep(2)
 
    def joinnow_first_name(self,value):
        self.set(self.locate.first_name,value)
        time.sleep(2)
 
    def now_last_name(self,value):
        self.set(self.locate.last_name,value)
        time.sleep(2)
   
    def enter_the_date(self,value):
        self.set(self.locate.on_date,value)
        time.sleep(2)
   
    def enter_the_month(self,value):
        self.set(self.locate.in_month,value)
        time.sleep(2)
   
    def enter_the_year(self,value):
        self.set(self.locate.in_year,value)
        time.sleep(2)
 
    def click_on_the_gender(self):
        self.actions.send_keys(Keys.PAGE_DOWN).perform()
        self.click(self.locate.gender)
        time.sleep(2)
 
    def enter_the_email(self,value):
        self.set(self.locate.email,value)
        time.sleep(2)
 
    def create_a_username(self,value):
        self.set(self.locate.join_username,value)
        time.sleep(2)
 
    def create_a_password(self,value):
        self.set(self.locate.join_password,value)
        time.sleep(2)
   
    # def click_robot_button(self):
    #     time.sleep(5)
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()
    #     self.wait_for_element(self.locate.robot).click()
    #     time.sleep(5)
 
    # def click_join_now_button(self):
    #     time.sleep(5)
    #     self.actions.send_keys(Keys.PAGE_DOWN).perform()
    #     self.click(self.locate.join_button)
    #     time.sleep(7)
    # def scroll_and_click_join_us(self):
    #     # Use the base page method to scroll and click
    #     self.scroll_into_view_and_click(self.locate.join_button)
    #     time.sleep(3)    
    def click_join_us_button_js(self):
        time.sleep(3)  
        self.js_click(self.locate.join_button)    
        time.sleep(3)  