import pytest
import time
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.MyAdvertisementPage import MyAdvertisementPage
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup_teardown")

class TestMyAdvertisement:

    def test_add_new_advertisement(self):

        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        advertisement = MyAdvertisementPage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        log.info("Go to Login Page")
        login.fill_the_login_form("demo","1234")
        log.info("fill the details in login form")
        login.click_login_button()
        log.info("click the login button")
        home.verifyLogin()      
        log.info("verify the login made successful")
        #t.test_valid_login("sandhiyas","Sand@123")
        log.info("Login successfully")
        home.goToMarketPlace()
        log.info("Go to MarketPlace")
        advertisement.click_my_advertisements()
        log.info("Click my advertisement in sub section")
        advertisement.add_new_advertisements()
        log.info("Click add new icon on my advertisement page")
        advertisement.fill_advertisement()
        log.info("fill the details of advertisement")
        advertisement.click_save_button()
        log.info("click on save button")

    def test_search_advertisement(self):

        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        advertisement = MyAdvertisementPage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        log.info("Go to Login Page")
        login.fill_the_login_form("sandhiyas","Sand@123")
        log.info("fill the details in login form")
        login.click_login_button()
        log.info("click the login button")
        home.verifyLogin()      
        log.info("verify the login made successful")
        #t.test_valid_login("sandhiyas","Sand@123")
        log.info("Login successfully")
        home.goToMarketPlace()
        log.info("Go to MarketPlace")
        advertisement.click_my_advertisements()
        log.info("Click my advertisement in sub section")
        time.sleep(5)
        advertisement.search_functionality()
        log.info("send a values to search")
        advertisement.verify_result()
        log.info("verify the searched result")

