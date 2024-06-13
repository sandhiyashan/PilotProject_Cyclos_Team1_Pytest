from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException 
from Pages.BasePage import BasePage

class MemberAccountPage(BasePage):
    member_acc_xpath = (By.XPATH,"//div[text()='Member account']")
    verify_memberacc_xpath = (By.XPATH,"//div[text()=' Member account ']")
    member_acc_keyword = "Member account"
    balance_xpath = (By.XPATH,"//div[@class='status-label col-6 col-sm-3']/following-sibling::div")
    table_xpath = (By.XPATH,"//table[@class='table table-hover cursor-pointer']")

    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.driver = driver

    def gotTo_memberaccount(self):
        '''Method to verify member account page'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.member_acc_xpath)))
            self.click(self.member_acc_xpath)
            mem_acc_title = self.find(self.verify_memberacc_xpath).text
            assert mem_acc_title == self.member_acc_keyword
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_balance(self):
        '''Method to verify balance'''
        try:
            self._wait.until(expected_conditions.presence_of_element_located((self.balance_xpath)))
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_transaction(self):
        '''Method to verify transaction'''
        try:
            self._wait.until(expected_conditions.presence_of_all_elements_located((self.table_xpath)))
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")




    