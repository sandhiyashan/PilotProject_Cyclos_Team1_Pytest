import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
#import time

class PaymentUser(BasePage):
    payment_to_user_xpath = (By.XPATH,"//div[text()='Payment to user']")
    payment_title_xpath = (By.XPATH,"//div[@class='content-title d-flex']//div")
    to_User_xpath = (By.XPATH,"//input[@placeholder='Type to search']")
    select_user_xpath = (By.XPATH,"//div[@class='dropdown-menu show']//a[1]")
    amount_xpath = (By.XPATH,"//div[@class='input-group']//input")
    scheduling_xpath = (By.XPATH,"//button[@class='form-control text-left custom-select w-100']")
    pay_now_xpath = (By.XPATH,"//a[text()=' Pay now ']")
    recurringPayment_xpath = (By.XPATH, "//a[text()=' Recurring payments ']")
    next_button_xpath = (By.XPATH , "//action-button[@class='d-inline-block button']/button")
    confirm_button_xpath = (By.XPATH , "//span[text()='Confirm']")
    toUser_error_msg = (By.XPATH, "(//div[@class='invalid-feedback'])[1]")
    amount_error_msg = (By.XPATH, "(//div[@class='invalid-feedback'])[2]")
    invalid_amount_error_msg = (By.CSS_SELECTOR, "div[class='invalid-feedback']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_Payment_To_User(self):
        time.sleep(5)
        self.click(self.payment_to_user_xpath)

    def verify_Payment_To_User(self):
        time.sleep(5)
        paymentpage_title = self.find(self.payment_title_xpath).text
        assert  paymentpage_title == "Payment to user"

    def fill_ToUser_Field(self, toUser):
        time.sleep(5)
        self.send_keys(self.to_User_xpath, toUser)
        self.click(self.select_user_xpath)

    def fill_Amount_Field(self,amount):
        time.sleep(3)
        self.send_keys(self.amount_xpath, amount)

    def click_Scheduling(self):
        time.sleep(5)
        self.click(self.scheduling_xpath)

    def select_PayNow(self):
        time.sleep(3)
        self.click(self.pay_now_xpath)
    
    def select_Recurring_Payment(self):
        time.sleep(3)
        self.click(self.recurringPayment_xpath)


    def click_Next_Button(self):
        self.click(self.next_button_xpath)
    
    def click_Confirm_Button(self):
        time.sleep(5)
        self.click(self.confirm_button_xpath)
    

    def verify_succesful_payment(self):
        succesful_pay = self.find(self.confirm_button_xpath).text
        assert succesful_pay == 'Confirm'
    
    def toUser_required_error_msg(self):
        time.sleep(4)
        error_msg = self.find(self.toUser_error_msg).text
        assert error_msg == 'This field is required'

    def amount_required_error_msg(self):
        time.sleep(4)
        error_msg = self.find(self.amount_error_msg).text
        assert error_msg == 'This field is required'
        
    def invalid_Amount_Message(self):
        time.sleep(3)
        error_msg = self.find(self.invalid_amount_error_msg).text
        assert error_msg == "Amount must be less or equal to 500,00 IU's."