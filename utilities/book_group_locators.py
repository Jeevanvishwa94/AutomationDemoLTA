from re import X
from selenium.webdriver.common.by import By

class BookGroupLocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    play =(By.XPATH,"//button[normalize-space()='PLAY']")
    book_a_group=(By.XPATH,"//a[text()='Book a group lesson']")
    remove_location =(By.XPATH,"//body[1]/main[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg']/*[name()='use']")
    group_check_box =(By.XPATH,"//*[@id='lta-simple-panel-1']/form/div[1]/div/div/div/div/input[3]")
    group_lesson_drops =(By.XPATH,"//div[@class='pac-container pac-logo hdpi']//div[1]")
    find_a_class =(By.XPATH,"//button[contains(text(),'Find a class')]")
    recurring_session =(By.XPATH,"//div[@class='js-lta-filter-panel-scroll-content']//div[2]//div[2]//div[1]//h2[1]//a[1]")
    recurring_checkbox_dropdown =(By.XPATH,"//main[@id='main-content']/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")