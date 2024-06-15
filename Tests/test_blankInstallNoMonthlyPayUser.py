import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.PaymentUser import PaymentUser

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username, password", excelReader.get_data("..\ExcelFiles\payment_to_user_testdata.xlsx", "login"))
@pytest.mark.parametrize("user_name, amount_data", excelReader.get_data("..\ExcelFiles\payment_to_user_testdata.xlsx", "validData"))

class TestblankInstNoMonthlyPaymentToUser:
    @pytest.mark.smoke
    def test_blankinstno_monthlypayment_user(self, username, password, user_name, amount_data):
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
        payment.fill_ToUser_Field(user_name)
        log.info("To user is filled")
        payment.fill_Amount_Field(amount_data)
        log.info("amount is filled")
        payment.click_Scheduling()
        log.info("Schedule is clicked")
        payment.select_monthlyInstall()
        log.info("Monthly install is clicked")
        payment.click_Next_Button()
        log.info("Next button is clicked")
        payment.instalno_required_error_msg()
        log.info("No of Installments Error message is displayed")
