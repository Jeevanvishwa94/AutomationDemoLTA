from selenium.webdriver.common.by import By

class LTAFanZoneLocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    fan_zone =(By.XPATH,"//button[normalize-space()='FAN ZONE']")
    tournaments =(By.XPATH,"//a[contains(text(),'All tournaments')]")
    calender =(By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/form[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]/button[1]")
    month =(By.XPATH,"//input[@id='eventmonth_0_7']")
    radio_button_apply = (By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/form[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]")
    location =(By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/form[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/h3[1]/button[1]")
    checkbox =(By.XPATH,"//input[@id='location_0_2']")
    location_apply =(By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/form[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]")
    event_type =(By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/form[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/h3[1]/button[1]")
    event_checkbox = (By.XPATH,"//input[@id='eventtype_0_2']")
    event_apply = (By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/form[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]")
