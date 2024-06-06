import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ReceivePaymentPage import ReceivePayPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("to_user,amount,description,username,password", excelReader.get_data("I:\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\receivePay_data.xlsx", "valid_data"))

class TestValidReceivePaymentPage:
    def test_validreceive_payment(self, to_user, amount, description, username, password):
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
        log.info("To user is filled")
        receive_pay.click_next()
        log.info("next button is clicked")
        receive_pay.verify_user_req_msg()
        log.info("verify the error message username required")
        receive_pay.verify_amount_req_msg()
        log.info("verify the error message amount required ")
