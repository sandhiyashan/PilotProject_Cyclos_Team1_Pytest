import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.PaymentUser import PaymentUser
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("../ExcelFiles/payment_to_user_testdata.xlsx", "login"))
@pytest.mark.parametrize("user_name,amount_data", excelReader.get_data("../ExcelFiles/payment_to_user_testdata.xlsx", "validData"))

class Test_paymentToUser:
    def test_PayNow(self,username,password,user_name,amount_data):
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
        payment.fill_Amount_Field(amount_data)
        payment.click_Scheduling()
        payment.select_PayNow()
        log.info("click the next button")
        payment.click_Next_Button()
        log.info("click the submit button")
        payment.click_Confirm_Button()
        payment.verify_succesful_payment()


