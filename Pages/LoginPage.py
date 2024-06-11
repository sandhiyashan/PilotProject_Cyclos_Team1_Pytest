from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    username_css = (By.CSS_SELECTOR,"input[placeholder='User']")
    password_css = (By.CSS_SELECTOR,"input[placeholder='Password']")
    submit_btn_xpath = (By.XPATH,"//button[@class='btn d-flex justify-content-center align-items-center w-100 h-100 btn-primary btn-action-primary']")
    forgot_pass_css = (By.CSS_SELECTOR,"a[class='d-block login-margin-top']")
    alert_css = (By.CSS_SELECTOR,"div[class='notification-message']")
    error_css = (By.CSS_SELECTOR,"div[class='invalid-feedback']")

    def __init__(self, driver):
        super().__init__(driver)  
        self.driver = driver

    def fill_the_login_form(self,user,password):
        '''fill the details in login form'''
        try:
            self.send_keys(self.username_css,user)
            self.send_keys(self.password_css,password)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_login_button(self):
        '''click the login button in login page'''
        try:
            self.click(self.submit_btn_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_error_message(self):
        '''verify the pop up message for invalid login credentials'''
        try:
            self.wait_for_element(self.alert_css)
            msg = self.find(self.alert_css).text
            assert msg == "The given name / password are incorrect. Please, try again."
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def check_empty_field(self):
        '''verify the message if the fields are blank'''
        try:
            msg = self.find(self.error_css).text
            assert msg == "This field is required"
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")
