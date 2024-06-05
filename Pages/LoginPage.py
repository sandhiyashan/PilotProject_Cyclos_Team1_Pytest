import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    username_css = (By.CSS_SELECTOR,"input[placeholder='User']")
    password_css = (By.CSS_SELECTOR,"input[placeholder='Password']")
    submit_btn_xpath = (By.XPATH,"//button[@class='btn d-flex justify-content-center align-items-center w-100 h-100 btn-primary btn-action-primary']")
    forgot_pass_css = (By.CSS_SELECTOR,"a[class='d-block login-margin-top']")
    alert_css = (By.CSS_SELECTOR,"div[class='notification-message']")
    error_css = (By.CSS_SELECTOR,"div[class='invalid-feedback']")

    def fill_the_login_form(self,user,password):
        self.send_keys(self.username_css,user)
        self.send_keys(self.password_css,password)

    def click_login_button(self):
        self.click(self.submit_btn_xpath)

    def verify_error_message(self):
        time.sleep(5)
        msg = self.find(self.alert_css).text
        assert msg == "The given name / password are incorrect. Please, try again."

    def check_empty_field(self):
        msg = self.find(self.error_css).text
        assert msg == "This field is required"

