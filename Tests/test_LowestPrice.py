import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.AdvertisementPage import Advertisement

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("C:\\cyclos_Pytest_project\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\payment_to_user_testdata.xlsx", "login"))

class Test_Advertisement:
    def test_lowestPrice(self,username,password):
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
        log.info("click the show Advertisment option")
        ads.click_show_advertisement()
        log.info("click the dropdown button order by")
        ads.click_orderBy()
        log.info("select the lowest price option")
        ads.click_lowest_price()
        log.info("verify the lowest price")
        ads.verify_lowest_price()

