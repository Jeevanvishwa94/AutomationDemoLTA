from selenium.webdriver.common.by import By


class SearchLocators:
    Username = (By.ID, "u")
    Password = (By.ID, "p")
    Verify_button = (By.XPATH, "//input[@type='submit']")
    all_cookies =(By.XPATH,"//button[@id='lta-cookies-button']")
    search_option = (By.XPATH,"//button[@class='lta-btn lta-btn--lg lta-btn--link lta-btn--icon lta-btn--icon-before lta-mega-nav__btn--search']//*[name()='svg']")
    click_search_logo = (By.XPATH,"//button[@type='submit']")
    lta_searchbox = (By.XPATH,"//main[@id='main-content']/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]")
    submit = (By.XPATH,"//main[@id='main-content']/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button")
    view_results = (By.XPATH,"//main[@id='main-content']/div[1]/form[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/a[1]")