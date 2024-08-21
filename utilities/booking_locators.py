from selenium.webdriver.common.by import By

class BookingLocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    play =(By.XPATH,"//button[normalize-space()='PLAY']")
    book_a_court =(By.XPATH,"//a[text()='Book a court']")
    remove_location =(By.XPATH,"//button[@aria-label='reset search']")
    check_box =(By.XPATH,"//*[@id='lta-simple-panel-1']/form/div[1]/div/div/div/div/input[3]")
    search_drop_button =(By.XPATH,"//div[@class='pac-container pac-logo hdpi']//div[1]")
    calender_dropdown =(By.XPATH,"//main[@id='main-content']/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    enter_date =(By.XPATH,"//tbody/tr[2]/td[5]/button[1]")
    time_dropdown =(By.XPATH,"//div[@role='combobox']")
    booking_slot =(By.XPATH,"//*[@id='lta-select-items-example-three-sm']/div[4]")
    click_a_court =(By.XPATH,"//button[contains(text(),'Find a court')]")
    
    

