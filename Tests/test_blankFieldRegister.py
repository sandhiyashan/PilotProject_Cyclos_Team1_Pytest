import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("website,mobile,land_line,address,zip1,city,region", excelReader.get_data("E:\PilotProject_Cyclos_Team1_Pytest-1\ExcelFiles\login_data.xlsx", "validatingBlank"))

class TestBlankFieldRegister:
    @pytest.mark.regression
    def test_blank_field_register(self,website,mobile,land_line,address,zip1,city,region):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        register = RegisterPage(self.driver)
        home.goToRegister()
        log.info("Register button is clicked")
        register.verify_register_page()
        log.info("Register page opens")
        register.fill_remaining_profile(website,mobile,land_line)
        log.info("fill the remaining field in the profile except mandatory field")
        register.enable_address_feild()
        log.info("enable the address section")
        register.fill_address_fields(address,zip1,city,region)
        log.info("Fill the address field")
        register.click_next_button()
        log.info("click the next button")
        register.verify_necessary_fields()
        log.info("verify the mandatory fields gives a alert message")