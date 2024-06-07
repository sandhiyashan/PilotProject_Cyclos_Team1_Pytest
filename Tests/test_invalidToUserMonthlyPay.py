import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.PaymentUser import PaymentUser

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username, password, user_name", excelReader.get_data("I:\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\payment_to_user_testdata.xlsx", "invalidUser_data"))

class TestInvalidToUserMonthlyPayUser:
    def test_invalidToUsermonthlypay_user(self, username, password, user_name):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        payment  = PaymentUser(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        login.fill_the_login_form(username,password)
        login.click_login_button()
        log.info("Logged in successfully")
        home.goToBanking()
        log.info("Go to Banking Page")
        home.verifyBankingPage()
        log.info("Banking Page is displayed")
        payment.click_Payment_To_User()
        log.info("Clicking the payment to user")
        payment.verify_Payment_To_User()
        log.info("Payment to user is displayed")
        payment.fill_ToUser(user_name)
        log.info("To user is filled")
        payment.verify_alert()
        log.info("Alert is displayed")
