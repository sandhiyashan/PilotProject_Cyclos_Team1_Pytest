from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Pages.BasePage import BasePage

class ReceivePayPage(BasePage):
    receive_payment = (By.XPATH,"(//nav[@class='navbar d-flex flex-column align-items-stretch']//a/div)[4]")
    rec_pay_verify = (By.XPATH,"//div[text()=' Receive payment ']")
    rec_pay_verify_keyword =  "Receive payment"
    confirm_button_keyword = "Confirm"
    input_user = (By.XPATH,"//input[@placeholder='Type to search']")
    input_amount = (By.XPATH,"//div[@class='label-value-container']//div[@class='input-group']//input")
    schedue = (By.XPATH,"//button[@class='form-control text-left custom-select w-100']")
    pay_type = (By.XPATH,"//div[@role='listbox']//a[text()=' Pay now ']")
    descrip_xpath = (By.XPATH,"//div[@class='d-flex label-value-value']//textarea")
    next_button = (By.XPATH,"//action-button/button")
    amt_error_mesg = (By.XPATH,"(//div[@class='d-flex label-value-value']/field-errors/div)")
    error_msg = "This field is required"
    user_error_msg = (By.XPATH,"(//div[@class='d-flex label-value-value']//field-errors/div)[1]")
    confirm_button = (By.XPATH,"//span[text()='Confirm']")
    alert_xpath = (By.XPATH,"//notification//div[@class='notification-message']")
    alert_text = "Invalid keywords"
    
    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.driver = driver

    def goToReceivePaymentPage(self):
        '''method to click Receive payment option'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.receive_payment)))
            self.click(self.receive_payment)
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_ReceivePaymentPage(self):
        '''method to verify Receive payment page'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.rec_pay_verify)))
            rec_pay_title = self.find(self.rec_pay_verify).text
            assert rec_pay_title == self.rec_pay_verify_keyword
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_user(self,username):
        '''Method to fill the user name'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.input_user)))
            self.send_keys(self.input_user,username)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_amount(self,amount):
        '''Method to fill the amount'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.input_amount)))
            self.send_keys(self.input_amount,amount)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def select_schedule(self):
        '''Method to click the scheduling dropdown list'''
        try:
            self._wait.until(expected_conditions.element_to_be_clickable((self.schedue)))
            self.click(self.schedue)
            self.click(self.pay_type)
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_description(self,description):
        '''Method to fill the description'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.descrip_xpath)))
            self.send_keys(self.descrip_xpath,description)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_next(self):
        '''Method to click the next button'''
        try:
            self._wait.until(expected_conditions.element_to_be_clickable((self.next_button)))
            self.click(self.next_button)
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_confirmPage(self):
        '''method to verify confirm page'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.confirm_button)))
            confirm_button_title = self.find(self.confirm_button).text
            assert confirm_button_title == self.confirm_button_keyword
            self.click(self.confirm_button)
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_user_req_msg(self):
        '''method to verify the user field required error message'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.user_error_msg)))
            title = self.find(self.user_error_msg).text
            assert title == self.error_msg
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_amount_req_msg(self):
        '''method to verify the amount required error message'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.amt_error_mesg)))
            title = self.find(self.amt_error_mesg).text
            assert title == self.error_msg
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_alert(self):
        '''method to verify the alert for invalid input'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.alert_xpath)))
            title = self.find(self.alert_xpath).text
            assert title == self.alert_text
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

