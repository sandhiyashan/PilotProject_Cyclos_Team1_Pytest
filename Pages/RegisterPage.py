from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class RegisterPage(BasePage):

    name_field_xpath = (By.XPATH,"//input-field[@formcontrolname='name']/label-value/div/div/input")
    loginName_field_xpath = (By.XPATH,"//input-field[@formcontrolname='username']/label-value/div/div/input")
    email_field_xpath = (By.XPATH,"//input-field[@formcontrolname='email']/input")
    website_field_css = (By.CSS_SELECTOR,"input[name='website']")
    female_checkbox_xpath = (By.XPATH,"(//input[@name='gender'])[1]")
    male_checkbox_xpath = (By.XPATH,"(//input[@name='gender'])[2]")
    business_type_css = (By.CSS_SELECTOR,"button#business_type")
    clothing_css = (By.CSS_SELECTOR,"a#business_type_clothing")
    mobile_xpath = (By.XPATH,"(//input-field[@formcontrolname='number']/input)[1]")
    landLine_xpath = (By.XPATH,"(//input-field[@formcontrolname='number']/input)[2]")
    address_enable_xpath = (By.XPATH,"(//label[@class='custom-control-label'])[3]")
    address_xpath = (By.XPATH,"(//label-value[@class='label-on-side label-value any-label-value field']/div/div/input)[3]")
    zip_code_css = (By.CSS_SELECTOR,"input#zip")
    city_field_css = (By.CSS_SELECTOR,"input#city")
    region_css = (By.CSS_SELECTOR,"input#region")
    country_css = (By.CSS_SELECTOR,"button#country")
    next_btn_xpath = (By.XPATH,"(//action-button[@class='d-inline-block button']/button)[3]")
    man_next_btn_xpath = (By.XPATH,"(//action-button[@class='d-inline-block button']/button)[2]")
    password_xpath = (By.XPATH,"//input-field[@formcontrolname='value']/label-value/div/div/input")
    confirm_password_xpath = (By.XPATH,"//input-field[@formcontrolname='confirmationValue']/label-value/div/div/input")
    demo_checkbox_xpath = (By.XPATH,"//accept-agreements[@formcontrolname='acceptAgreements']/div/div/div/boolean-field/div/label")
    submit_btn_xpath = (By.XPATH,"(//action-button[@class='d-inline-block button']/button)[1]")
    password_validation_css = (By.CSS_SELECTOR,"li[class='invalid']")
    field_required_css = (By.CSS_SELECTOR,"div[class='invalid-feedback']")
    verify_register_xpath = (By.XPATH,"//div[text()=' User registration ']")
    value = "male"
    value1 = "female"

    def verify_register_page(self):
        '''verify whether the register is opened or not'''
        verify = self.find(self.verify_register_xpath).text
        assert verify == "User registration"

    def fill_required_feilds(self,name,login_name,email):
        '''Fill the required details in the register page'''
        self.send_keys(self.name_field_xpath,name)
        self.send_keys(self.loginName_field_xpath,login_name)
        self.send_keys(self.email_field_xpath,email)

    def fill_remaining_profile(self,website,mobile_number,land_line):
        '''Fill the remaining feilds in profile section'''
        self.send_keys(self.website_field_css,website)
        self.click(self.business_type_css)
        self.click(self.clothing_css)
        self.send_keys(self.mobile_xpath,mobile_number)
        self.send_keys(self.landLine_xpath,land_line)

    def enable_address_feild(self):
        '''method enable the address section'''
        self.click(self.address_enable_xpath)

    def fill_address_fields(self,address,zip1,city,region):
        '''fill the address feilds in address section'''
        self.send_keys(self.address_xpath,address)
        self.send_keys(self.zip_code_css,zip1)
        self.send_keys(self.city_field_css,city)
        self.send_keys(self.region_css,region)

    def click_next_button(self):
        '''method to click next button'''
        self.click(self.next_btn_xpath)

    def fill_password_feild(self,password,cpass):
        '''fill the password feilds in password section'''
        self.send_keys(self.password_xpath,password)
        self.send_keys(self.confirm_password_xpath,cpass)

    def click_confirmation_check_box(self):
        '''click the confirmation check box'''
        self.click(self.demo_checkbox_xpath)

    def click_submit_button(self):
        '''click the submit button'''
        self.click(self.submit_btn_xpath)

    def verify_successful_registration(self):
        '''verify whether a registration is successful or not'''
        verify = self.find(self.field_required_css).text
        assert verify == "This field is required"

    def verify_necessary_fields(self):
        '''verify the necessary feild is filled or not'''
        verify = self.find(self.field_required_css).text
        assert verify == "This field is required"

    def verify_password(self):
        '''verify the password is valid'''
        password = self.find(self.password_validation_css).text
        assert password == "At least 4 characters ✗"

    def verify_confirm_password(self):
        '''verify the confirm password is valid'''
        verify_pass = self.find(self.field_required_css).text
        assert verify_pass == "The passwords don't match"

    def click_next_button_mandatory(self):
        '''click the next button'''
        self.click(self.man_next_btn_xpath)

    def verify_invalid_email(self):
        '''verify a email is valid or not'''
        email = self.find(self.field_required_css).text
        assert email == "This field is invalid"

    def verify_existing_email(self):
        '''verify whether the existing email or not'''
        vemail = self.find(self.field_required_css).text
        assert vemail == "E-Mail must be unique."


