import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.PaymentUser import PaymentUser

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username, password", excelReader.get_data("..\ExcelFiles\payment_to_user_testdata.xlsx", "login"))

class TestBlankFieldMonthlyPaymentToUser:
    @pytest.mark.smoke
    def test_blankfieldmonthlypayment_touser(self, username, password):
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
        payment.click_Next_Button()
        log.info("Next button is clicked")
        payment.toUser_required_error_msg()
        log.info("To User Error message is displayed")
        payment.amount_required_error_msg()
        log.info("Amount Error message is displayed")
