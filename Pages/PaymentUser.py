import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from Pages.BasePage import BasePage

class PaymentUser(BasePage):
    payment_to_user_xpath = (By.XPATH,"//div[text()='Payment to user']")
    payment_title_xpath = (By.XPATH,"//div[@class='content-title d-flex']//div")
    to_User_xpath = (By.XPATH,"//input[@placeholder='Type to search']")
    select_user_xpath = (By.XPATH,"//div[@class='dropdown-menu show']//a[1]")
    amount_xpath = (By.XPATH,"//div[@class='input-group']//input")
    scheduling_xpath = (By.XPATH,"//button[@class='form-control text-left custom-select w-100']")
    pay_now_xpath = (By.XPATH,"//a[text()=' Pay now ']")
    recurringPayment_xpath = (By.XPATH, "//a[text()=' Recurring payments ']")
    monthly_inst_xpath = (By.XPATH,"//div[@role='listbox']//a[text()=' Monthly installments ']")
    no_of_inst_xpath = (By.XPATH,"//div[@class='d-flex label-value-value']//input[@type='number']")
    next_button_xpath = (By.XPATH , "//action-button[@class='d-inline-block button']/button")
    confirm_button_xpath = (By.XPATH , "//span[text()='Confirm']")
    toUser_error_msg = (By.XPATH, "(//div[@class='invalid-feedback'])[1]")
    amount_error_msg = (By.XPATH, "(//div[@class='invalid-feedback'])[2]")
    no_of_instal_error_msg = (By.XPATH, "(//div[@class='invalid-feedback'])[1]")
    invalid_amount_error_msg = (By.CSS_SELECTOR, "div[class='invalid-feedback']")
    alert_xpath = (By.XPATH,"//notification//div[@class='notification-message']")
    alert_text = "Invalid keywords"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_Payment_To_User(self):
        '''click the payment to user option'''
        try:
            self.wait_for_element(self.payment_to_user_xpath)
            self.click(self.payment_to_user_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")
        
    def verify_Payment_To_User(self):
        '''Verify the payment to user page open'''
        try:
            paymentpage_title = self.wait_for_element(self.payment_title_xpath).text
            assert  paymentpage_title == "Payment to user"
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def fill_ToUser_Field(self, toUser):
        '''Enter the username in the to user field'''
        try:
            self.wait_for_element(self.to_User_xpath)
            time.sleep(3)
            self.send_keys(self.to_User_xpath, toUser)
            self.click(self.select_user_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def fill_Amount_Field(self,amount):
        '''Enter the amount in the amount field'''
        try:
            self.wait_for_element(self.amount_xpath)
            self.send_keys(self.amount_xpath, amount)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_Scheduling(self):
        '''Click the scheduling dropdown list'''
        try:
            self.wait_for_element(self.scheduling_xpath)
            self.click(self.scheduling_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def select_PayNow(self):
        '''Select the paynow option in dropdown list'''
        try:
            self.wait_for_element(self.pay_now_xpath)
            self.click(self.pay_now_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def select_monthlyInstall(self):
        '''Method to monthly install option'''
        try:
            self._wait.until(expected_conditions.element_to_be_clickable((self.monthly_inst_xpath)))
            self.click(self.monthly_inst_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_no_of_installment(self,instal_no):
       '''Method to fill the no of installments'''
       try:
           self._wait.until(expected_conditions.visibility_of_element_located((self.no_of_inst_xpath)))
           self.send_keys(self.no_of_inst_xpath,instal_no)
       except NoSuchElementException as e:
            print(f"Element not found: {e}")
       except Exception as e:
            print(f"Error: {e}")

    def verify_alert(self):
        '''Method to verify the alert'''
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

    def select_Recurring_Payment(self):
        '''Select the select_Recurring_Payment option in dropdown list'''
        try:
            self.wait_for_element(self.recurringPayment_xpath)
            self.click(self.recurringPayment_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_Next_Button(self):
        '''Click the next button'''
        try:
            self.click(self.next_button_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_Confirm_Button(self):
        '''click the confirm button'''
        try:
            time.sleep(3)
            self.click(self.confirm_button_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")
    
    def verify_succesful_payment(self):
        '''Verify the successful payment message'''
        try:
            succesful_pay = self.find(self.confirm_button_xpath).text
            assert succesful_pay == 'Confirm'
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def toUser_required_error_msg(self):
        '''Verify the to To user required error message'''
        try:
            error_msg = self.wait_for_element(self.toUser_error_msg).text
            assert error_msg == 'This field is required'
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def amount_required_error_msg(self):
        '''Verify the amount field required error message is displayed'''
        try:
            error_msg = self.wait_for_element(self.amount_error_msg).text
            assert error_msg == 'This field is required'
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def instalno_required_error_msg(self):
        '''Verify the to To user required error message'''
        try:
            error_msg = self.wait_for_element(self.no_of_instal_error_msg).text
            assert error_msg == 'This field is required'
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def invalid_Amount_Message(self):
        '''Verify the invalid amount error message is displayed'''
        try:
            error_msg = self.wait_for_element(self.invalid_amount_error_msg).text
            assert error_msg == "Amount must be less or equal to 500,00 IU's."
        except NoSuchElementException as e:
            print(f"Element cannot be found: {e}")
        except Exception as e:
            print(f"Error Message: {e}")