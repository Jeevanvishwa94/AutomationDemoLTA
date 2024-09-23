import time
from selenium.webdriver.common.keys import Keys
from Pageobject.base_page import BasePage
from utilities.signin_locstors import SiginLocators
 
class SiginPage(BasePage):
    def __init__(self, driver):
        self.locate = SiginLocators
        super().__init__(driver)
 
    def ppe_username(self, ppe_username):
        self.set(self.locate.Username, ppe_username)
 
    def ppe_password(self, ppe_password):
        self.set(self.locate.Password, ppe_password)
 
    def click_ppe_login(self):
        self.click(self.locate.Verify_button)
        time.sleep(2)
 
    def Accept_all_cookies(self):
        self.wait_for_element(self.locate.all_cookies).click()
        time.sleep(2)
     
    def Click_signin_button(self):
        self.wait_for_element(self.locate.sigin_button).click()
        time.sleep(2) 
           
    def signin_credential(self,value):    
        self.set(self.locate.signin_username,value)
        
    def enter_signin_credential(self,value):     
        self.set(self.locate.signin_password,value)
        self.wait_for_element(self.locate.click_signin_button).click()
        time.sleep(3)    
    
    def ppe_username(self, ppe_username):
        self.set(self.locate.Username, ppe_username)
 
    def ppe_password(self, ppe_password):
        self.set(self.locate.Password, ppe_password)
 
    def click_ppe_login(self):
        self.click(self.locate.Verify_button)
        time.sleep(2)    
    
    def click_avator_button(self):
        self.click(self.locate.click_avator)
        time.sleep(2)    
            
    def click_add_role_fun(self):
        self.click(self.locate.click_add_new_role)
        time.sleep(2)        
    
    def click_let_start_button(self):
        self.wait_for_element(self.locate.click_let_start_button).click()  
    
    def click_parks_activators(self):
        self.wait_for_element(self.locate.click_parks_activators).click()    
        time.sleep(5) 
    
    # def click_teacher_radio_button(self):
    #     self.click(self.locate.click_teacher_radio_button) 
    
    # def click_activator(self):
    #     self.click(self.locate.click_activator_button) 
    
    # def click_next_button(self):
    #     self.click(self.locate.click_next_button) 
           
    # def click_get_start_button(self):
    #     self.click(self.locate.click_get_start_button)  
    
    # def click_student_button(self):
    #     self.click(self.locate.click_teacher_student_button)     
    
    # def click_next_button_again(self):
    #     self.click(self.locate.click_next_button_again)  
    
    # def click_senior_leader_button(self):
    #     self.click(self.locate.click_senior_leader_button)    
    
    # def click_school_pincode(self,value):
    #     self.set(self.locate.enter_school_pincode,value)            