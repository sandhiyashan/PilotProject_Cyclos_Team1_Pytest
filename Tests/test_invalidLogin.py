import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("username,password", excelReader.get_data("../ExcelFiles/login_data.xlsx", "invalidLogin"))

class TestInvalidLogin:
    @pytest.mark.regression
    def test_invalid_login(self,username,password):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        log.info("Go to Login Page")
        login.fill_the_login_form(username,password)
        log.info("fill the details in login form")
        login.click_login_button()
        log.info("click the login button")
        login.verify_error_message()
        log.info("verify whether the functionality check invalid credentials")
