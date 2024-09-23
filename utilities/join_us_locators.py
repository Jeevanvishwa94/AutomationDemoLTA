from selenium.webdriver.common.by import By
 
class ADEjoinLocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    join_us =(By.XPATH,"//a[@class='lta-btn lta-mega-nav__btn--outline-joinus u-px-5 u-bg-lta-accent-purple u-text-white u-hstack u-p-3']")
    join_now =(By.XPATH,"//a[@class='rt-button--inverse lta-btn--block']")
    first_name =(By.XPATH,"//input[@id='firstName']")
    last_name = (By.XPATH,"//input[@id='lastName']")
    on_date = (By.XPATH,"//input[@id='TextInputDay']")
    in_month = (By.XPATH,"//input[@id='TextInputMonth']")
    in_year = (By.XPATH,"//input[@id='TextInputYear']")
    gender = (By.XPATH,"//*[@id='gender1']")
    email = (By.XPATH,"//input[@id='email']")
    join_username = (By.XPATH,"//input[@id='username']")
    join_password = (By.XPATH,"//input[@id='password']")
    # robot = (By.XPATH,"//div[@id='google_recaptcha']")
    # join_button = (By.XPATH,"//button[contains(text(),'Join now')][1]")
    join_button = (By.CLASS_NAME,"js-create-submit")
 