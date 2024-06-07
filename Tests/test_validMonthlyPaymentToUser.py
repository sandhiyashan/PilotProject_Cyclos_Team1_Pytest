import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.PaymentUser import PaymentUser

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username, password, user_name, amount_data, instal_no", excelReader.get_data("I:\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\payment_to_user_testdata.xlsx", "valid"))

class TestValidMonthlyPaymentToUser:
    def test_Validmonthlypayment_touser(self, username, password, user_name, amount_data, instal_no):
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
        payment.fill_no_of_installment(instal_no)
        log.info("no of install is filled")
        payment.click_Next_Button()
        log.info("Next button is clicked")
        payment.click_Confirm_Button()
        payment.verify_succesful_payment()
        log.info("confirmation page is displayed successfully")
