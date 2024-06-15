import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ReceivePaymentPage import ReceivePayPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("to_user,amount,description,username,password", excelReader.get_data("I:\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\receivePay_data.xlsx", "invalid_data"))

class TestinvalidToUserReceivePaymentPage:
    @pytest.mark.regression
    def test_invalidToUserreceive_payment(self, to_user, amount, description, username, password):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        receive_pay  = ReceivePayPage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        login.fill_the_login_form(username,password)
        login.click_login_button()
        log.info("Logged in successfully")
        home.goToBanking()
        log.info("Go to Banking Page")
        home.verifyBankingPage()
        log.info("Banking Page is displayed")
        receive_pay.goToReceivePaymentPage()
        log.info("Go to Receive Payment Page")
        receive_pay.verify_ReceivePaymentPage()
        log.info("Receive Payment Page is displayed")
        receive_pay.fill_user(to_user)
        receive_pay.verify_alert()
        log.info("Alert is verified")
        
