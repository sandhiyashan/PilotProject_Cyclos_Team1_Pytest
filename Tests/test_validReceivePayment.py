import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ReceivePaymentPage import ReceivePayPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("to_user,amount,description,username,password", excelReader.get_data("../ExcelFiles/receivePay_data.xlsx", "valid_data"))

class TestValidReceivePaymentPage:
    @pytest.mark.smoke
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
        receive_pay.fill_amount(amount)
        log.info("amount is entered")
        receive_pay.select_schedule()
        log.info("schedule is selected")
        receive_pay.fill_description(description)
        log.info("description is entered")
        receive_pay.click_next()
        log.info("next button is clicked")
        receive_pay.verify_confirmPage()
        log.info("confirmation page is displayed successfully")
