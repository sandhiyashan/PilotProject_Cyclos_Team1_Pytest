import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from Pages.BasePage import BasePage


class Advertisement(BasePage):

    advertisment_xpath = (By.XPATH , "//div[text()='Advertisements']")
    keyword_xpath = (By.XPATH , "(//div[@class='d-flex label-value-value']//input)[1]")
    keyword_based_xpath = (By.XPATH, "//div[text()=' Orange ']")
    invalid_msg_xpath = (By.XPATH, "//div[text()='Invalid keywords']")


    def __init__(self, driver):
        super().__init__(driver)  
        self.driver = driver 
    

    def click_Advertisement(self):
        self._wait.until(ec.visibility_of_element_located((self.advertisment_xpath)))
        self.click(self.advertisment_xpath)

    def enter_keyword(self,data):
        self._wait.until(ec.visibility_of_element_located((self.keyword_xpath)))
        time.sleep(3)
        self.send_keys(self.keyword_xpath, data)



    def verify_keyword_based_element(self):
        self._wait.until(ec.visibility_of_element_located((self.keyword_xpath)))
        time.sleep(5)
        elements = self.find_Elements(self.keyword_based_xpath)
        for element in elements:
            assert element.text == "Orange"


    def verify_invalid_keyword_error_msg(self):
        self._wait.until(ec.visibility_of_element_located((self.invalid_msg_xpath)))
        error_msg = self.find(self.invalid_msg_xpath).text
        assert error_msg == "Invalid keywords"