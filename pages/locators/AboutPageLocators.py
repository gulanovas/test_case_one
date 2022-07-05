
from selenium.webdriver.common.by import By

class AboutPageLocators:

    ONLINE_PLAYERS = (By.XPATH,"//div[(@class='online_stats')]//div[(@class='online_stat')][1]")[0]
    PLAYING_NOW = (By.XPATH,"//div[(@class='online_stats')]//div[(@class='online_stat')][2]")[0]