from selenium.webdriver.common.by import By


class LTALocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    compete = (By.XPATH,"//button[contains(text(), 'COMPETE')]")
    junior = (By.XPATH,"//a[contains(text(),'Juniors')]")
    youth_Competitions = (By.XPATH,"//main[@id='main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/p[1]/span[1]/*[1]")
    youth_match_play = (By.XPATH,"//*[@id='main-content']/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/p[1]/span[1]/*[name()='svg'][1]/*[name()='use'][1]")
    submit_lta =(By.XPATH,"//span[text()='Enter a LTA Youth Matchplay Competition']")
    accept =(By.XPATH,"//span[contains(text(),'Accept')]")
    tournaments =(By.XPATH,"//span[contains(text(),'Tournaments')]")
    entry_open =(By.XPATH,"//a[normalize-space()='Entry open']")
    leamington_tennis_club =(By.XPATH,"//li[1]//div[1]//div[1]//div[1]//h4[1]//a[1]//span[1]")
    enter_leamington =(By.XPATH,"//span[text()='Enter']")

    