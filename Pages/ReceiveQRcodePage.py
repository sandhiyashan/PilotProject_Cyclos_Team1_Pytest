from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
        '''method to click Receive QR code option'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.receive_qr)))
            self.click(self.receive_qr)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_ReceiveQrcodPage(self):
        '''method to verify Receive QR code page'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.receive_qr_key_xpath)))
            receive_qr_title = self.find(self.receive_qr_key_xpath).text
            assert receive_qr_title == self.receive_qr_keyword
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_the_receive_qr_form(self,amount,description):
        '''method to fill the receive qr form'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.amount_css)))
            self.send_keys(self.amount_css,amount)
            self._wait.until(expected_conditions.visibility_of_element_located((self.descript_css)))
            self.send_keys(self.descript_css,description)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_gen_qrcode(self):
        '''method to click generate qr code button'''
        try:
            self._wait.until(expected_conditions.element_to_be_clickable((self.gen_qr)))
            self.click(self.gen_qr)
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_qr_display(self):
        '''method to verify QR code'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.gen_qr)))
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_error_mesg(self):
        '''method to verify the field required error message'''
        try:
            title = self.find(self.error_msg_xpath).text
            assert title == self.error_msg
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")
