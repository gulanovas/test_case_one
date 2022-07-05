
from SeleniumExtended import SeleniumExtended
from configs.config import get_base_url
from pages.locators.HomePageLocators import HomePageLocators
from pages.locators.AboutPageLocators import AboutPageLocators

class CaseOne(HomePageLocators, AboutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_about_button(self):
        self.sl.wait_and_click(self.ABOUT)

    def get_online_now(self):
        self.sl.wait_and_get_text(self.ONLINE_PLAYERS) 
        
    def get_playing_now(self):
        self.sl.wait_and_get_text(self.PLAYING_NOW) 
        
    def click_store_button(self):
        self.sl.wait_and_click(self.STORE)
