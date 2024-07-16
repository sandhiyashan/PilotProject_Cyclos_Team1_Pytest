import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.PaymentUser import PaymentUser
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("../ExcelFiles/payment_to_user_testdata.xlsx", "login"))

class Test_paymentToUser:
    @pytest.mark.smoke
    def test_BlankFields(self,username,password):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        payment = PaymentUser(self.driver)
        login = LoginPage(self.driver)
        log.info("click the login page")
        home.goToLogin()
        log.info("Fill the required details in login page")
        login.fill_the_login_form(username,password)
        log.info("click the loggin button")
        login.click_login_button()
        log.info("click the banking option in homepage")
        home.goToBanking()
        log.info("click the payment to user")
        payment.click_Payment_To_User()
        payment.verify_Payment_To_User()
        log.info("click the next button")
        payment.click_Next_Button()
        log.info("verify the error message for the blank to User field")
        payment.toUser_required_error_msg()
        log.info("verify the error message for the blank amount field")
        payment.amount_required_error_msg()


