from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Pages.BasePage import BasePage

class ReceiveQRcodePage(BasePage):
    receive_qr =   (By.XPATH,"//div[text()='Receive QR-code']")
    receive_qr_keyword = "Receive QR-code payment"
    receive_qr_key_xpath = (By.XPATH,"//div[text()=' Receive QR-code payment ']")
    amount_css =  (By.CSS_SELECTOR,"div[class='input-group'] input")
    descript_css = (By.CSS_SELECTOR,"div[class='label-value-container'] textarea")
    gen_qr = (By.XPATH,"//button[@class='btn d-flex justify-content-center align-items-center w-100 h-100 btn-primary']")
    error_msg_xpath = (By.XPATH,"(//div[@class='d-flex label-value-value']/field-errors/div)")
    error_msg = "This field is required"

    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.driver = driver

    def goToReceiveQrcodPage(self):
        self._wait.until(expected_conditions.visibility_of_element_located((self.receive_qr)))
        self.click(self.receive_qr)

    def verify_ReceiveQrcodPage(self):
        self._wait.until(expected_conditions.visibility_of_element_located((self.receive_qr_key_xpath)))
        receive_qr_title = self.find(self.receive_qr_key_xpath).text
        assert receive_qr_title == self.receive_qr_keyword

    def fill_the_receive_qr_form(self,amount,description):
        self._wait.until(expected_conditions.visibility_of_element_located((self.amount_css)))
        self.send_keys(self.amount_css,amount)
        self._wait.until(expected_conditions.visibility_of_element_located((self.descript_css)))
        self.send_keys(self.descript_css,description)

    def click_gen_qrcode(self):
        self._wait.until(expected_conditions.element_to_be_clickable((self.gen_qr)))
        self.click(self.gen_qr)

    def verify_qr_display(self):
        self._wait.until(expected_conditions.visibility_of_element_located((self.gen_qr)))

    def verify_error_mesg(self):
        title = self.find(self.error_msg_xpath).text
        assert title == self.error_msg
