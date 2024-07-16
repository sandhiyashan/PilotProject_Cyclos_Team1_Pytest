import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities import read_config
from Pages.MemberAccountPage import MemberAccountPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("../ExcelFiles/login_data.xlsx", "validLogin"))

class TestMemberAccount:
    @pytest.mark.smoke
    def test_membAccount(self,username,password):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        member_acc  = MemberAccountPage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        login.fill_the_login_form(username,password)
        login.click_login_button()
        log.info("Logged in successfully")
        home.goToBanking()
        log.info("Go to Banking Page")
        home.verifyBankingPage()
        log.info("Banking Page is displayed")
        member_acc.gotTo_memberaccount()
        log.info("Member account Page is displayed")
        member_acc.verify_balance()
        log.info("Balance is verified")
        member_acc.verify_transaction()
        log.info("Transaction history is verified")



