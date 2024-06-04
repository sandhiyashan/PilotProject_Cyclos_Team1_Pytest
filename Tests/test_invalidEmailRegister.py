import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("name,login,email", excelReader.get_data("E:\PilotProject_Cyclos_Team1_Pytest-1\ExcelFiles\login_data.xlsx", "invalidEmail"))

class TestInvalidEmailRegister:
    def test_invalid_email_register(self,name,login,email):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        register = RegisterPage(self.driver)
        home.goToRegister()
        log.info("Register button is clicked")
        register.verify_register_page()
        log.info("Register page opens")
        register.fill_required_feilds(name,login,email)
        log.info("Required fields are filled")
        register.click_next_button_mandatory()
        log.info("Next button is clicked")
        register.verify_invalid_email()
        log.info("Invalid email is verified")

