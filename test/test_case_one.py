from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from pages.CaseOne import CaseOne

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()
  
@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass
class Test_URL_Chrome(Basic_Chrome_Test):
            def test_case_one(self):
                
                case_one = CaseOne(self.driver)

                # go to home page
                case_one.go_to_home_page()

                # click about button
                case_one.click_about_button()

                # get online now
                case_one.get_online_now()

                # get playing now 
                case_one.get_playing_now()

                # click store button
                case_one.click_store_button()
