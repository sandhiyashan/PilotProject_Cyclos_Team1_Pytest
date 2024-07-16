import pytest
from Utilities import consolelogger
from Utilities import excelReader
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ReceiveQRcodePage import ReceiveQRcodePage

@pytest.mark.usefixtures("test_setup_teardown")
@pytest.mark.parametrize("amount,description,username,password", excelReader.get_data("../ExcelFiles/qrcode.xlsx", "valid_data"))

class TestValidReceiveQRCode:
    @pytest.mark.smoke
    def test_validreceive_qr_code(self, username, password, amount, description):
        log = consolelogger.get_logger()
        home = HomePage(self.driver)
        receive_qr  = ReceiveQRcodePage(self.driver)
        login = LoginPage(self.driver)
        home.goToLogin()
        login.fill_the_login_form(username,password)
        login.click_login_button()
        log.info("Logged in successfully")
        home.goToBanking()
        log.info("Go to Banking Page")
        home.verifyBankingPage()
        log.info("Banking Page is displayed")
        receive_qr.goToReceiveQrcodPage()
        log.info("Go to Receive QR Code Page")
        receive_qr.verify_ReceiveQrcodPage()
        log.info("Receive QR Code Page is displayed")
        receive_qr.fill_the_receive_qr_form(amount,description)
        receive_qr.click_gen_qrcode()
        receive_qr.verify_qr_display()
        log.info("QR Code is generated successfully")
