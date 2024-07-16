import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.AdvertisementPage import Advertisement

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("../ExcelFiles/payment_to_user_testdata.xlsx", "login"))
@pytest.mark.parametrize("keyword_data", excelReader.get_data("../ExcelFiles/advertisement_testdata.xlsx", "valid_data"))

class Test_Advertisement:
    @pytest.mark.smoke
    def test_Advertisement(self,username,password,keyword_data):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        login = LoginPage(self.driver)
        ads = Advertisement(self.driver)
        log.info("click the login page")
        home.goToLogin()
        log.info("Fill the required details in login page")
        login.fill_the_login_form(username,password)
        log.info("click the loggin button")
        login.click_login_button()
        log.info("click the marketplace option in homepage")
        home.goToMarketPlace()
        log.info("click the Advertisment option in marketplace")
        ads.click_Advertisement()
        log.info("Enter the keyword into the keyword field")
        ads.enter_keyword(keyword_data)
        log.info("verify the keyword based element displayed ")
        ads.verify_keyword_based_element()


