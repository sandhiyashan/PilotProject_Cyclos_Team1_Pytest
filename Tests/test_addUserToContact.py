import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.BusinessDirectoryPage import BusinessDirectoryPage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("key,username,password,non", excelReader.get_data("I:\\PilotProject_Cyclos_Team1_Pytest\\ExcelFiles\\busDir_data.xlsx", "valid_data"))

class TestAddUserToContact:
    @pytest.mark.smoke
    def test_adduser_tocontact(self, key, username, password,non):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        business_dir  = BusinessDirectoryPage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        login.fill_the_login_form(username,password)
        login.click_login_button()
        log.info("Logged in successfully")
        home.goToMarketPlace()
        log.info("Go to Market Place")
        home.verify_marketplace()
        log.info("Market Place Page is displayed")
        business_dir.goToBusinessDirectoryPage()
        log.info("Go to Business directory")
        business_dir.verify_BusinessDirectoryPage()
        log.info("Business Directory Page is displayed")
        business_dir.fill_key(key)
        log.info("Filled the key")
        business_dir.click_user_tocontact()
        log.info("Clicked on user") 
        business_dir.click_add_contact()
        log.info("Clicked on add to contact")
        business_dir.verify_add_contact()
        log.info("User added to contact is verified")
    
        
