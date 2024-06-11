import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.PaymentUser import PaymentUser
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("C:\\cyclos_Pytest_project\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\payment_to_user_testdata.xlsx", "login"))
@pytest.mark.parametrize("user_name,exceeded_amount_data", excelReader.get_data("C:\\cyclos_Pytest_project\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\payment_to_user_testdata.xlsx", "boundary"))

class Test_InvalidPayment:
    def test_PayNow(self,username,password,user_name,exceeded_amount_data):
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
        payment.click_Payment_To_User()
        payment.verify_Payment_To_User()
        log.info("fill the required payment details ")
        payment.fill_ToUser_Field(user_name)
        log.info("Enter the amount which is greater than 500")
        payment.fill_Amount_Field(exceeded_amount_data)
        payment.click_Scheduling()
        payment.select_PayNow()
        log.info("click the next button")
        payment.click_Next_Button()
        log.info("verify the invalid payment error message")
        payment.invalid_Amount_Message()


