
from selenium.webdriver.common.by import By

class HomePageLocators:

    ABOUT = (By.XPATH,"//div[@id='global_header']//div[contains(@class, 'content')]//div[contains(@class, 'supernav_container')]//a[@class='menuitem'][1]")[0]
    STORE = (By.XPATH,"//div[@id='global_header']//div[contains(@class, 'content')]//div[contains(@class, 'supernav_container')]//a[contains(@class,'supernav')][1]")[0]
