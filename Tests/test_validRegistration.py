import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("name,login,email,website,mobile,land_line,address,zip1,city,region,password,confirm_password", excelReader.get_data("E:\PilotProject_Cyclos_Team1_Pytest-1\ExcelFiles\login_data.xlsx", "validRegister"))

class TestValidRegister:
    @pytest.mark.smoke
    def test_valid_register(self, name, login, email, website, mobile, land_line, address, zip1, city, region, password, confirm_password):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        register = RegisterPage(self.driver)
        home.goToRegister()
        log.info("Register page opens")
        register.verify_register_page()
        register.fill_required_feilds(name, login, email)
        log.info("Required fields are filled")
        register.fill_remaining_profile(website, mobile, land_line)
        log.info("Remaining fields are filled")
        register.enable_address_feild()
        log.info("Address field is enabled")
        register.fill_address_fields(address, zip1, city, region)
        log.info("Address section is filled")
        register.click_next_button()
        log.info("Next button is clicked")
        register.fill_password_feild(password, confirm_password)
        log.info("Password section is filled")
        register.click_confirmation_check_box()
        register.click_submit_button()
        register.verify_successful_registration()
        log.info("Registration is successfully completed")
