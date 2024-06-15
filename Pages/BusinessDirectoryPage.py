from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Pages.BasePage import BasePage

class BusinessDirectoryPage(BasePage):
    business_dir = (By.XPATH,"//div[text()='Business directory']")
    business_dir_title = (By.XPATH,"//div[text()=' Business directory ']")
    business_dir_key = "Business directory"
    input_key = (By.XPATH,"//div[@class='d-flex label-value-value']/input")
    key_error_msg = (By.XPATH,"//div[text()=' No results match the search criteria  ']")
    error_msg = "No results match the search criteria"
    key_error_alert = (By.XPATH,"//div[@class='notification-message']")
    alert_text = "Invalid keywords"
    order_by_xpath = (By.XPATH,"//button[@class='form-control text-left custom-select w-100']")
    relevance_option = (By.XPATH,"//div[@role='listbox']//a[text()='Relevance']")
    relev_results = (By.XPATH,"//div[@class='row tiled-results']")
    expected_relev_res = "shop"
    contact = (By.XPATH,"(//div[@class='row tiled-results']//a)[1]")
    add_to_contact = (By.XPATH,"//div[text()='Add to contacts']")
    add_contact_verify = (By.XPATH,"//div[text()='Remove from contacts']")
    add_contact_key = "Remove from contacts"

    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.driver = driver

    def goToBusinessDirectoryPage(self):
        '''method to click Business Directory option'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.business_dir)))
            self.click(self.business_dir)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_BusinessDirectoryPage(self):
        '''method to verify Business Directory page'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.business_dir_title)))
            bus_dir_title = self.find(self.business_dir_title).text
            assert bus_dir_title == self.business_dir_key
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_key(self,key):
        '''Method to fill the Keyword in input field'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.input_key)))
            self.send_keys(self.input_key,key)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_orderby(self):
        '''Method to click orderby button'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.order_by_xpath)))
            self.click(self.order_by_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    def click_relevance(self):
        '''Method to click relevance option in dropdown list'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.relevance_option)))
            self.click(self.relevance_option)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_relevance_results(self):
        '''Method to verify results'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.relev_results)))
            list_of_elements = self.driver.find_elements(*self.relev_results)
            for element in list_of_elements:
                result = element.text
                assert self.expected_relev_res in result 
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_user_tocontact(self):
        '''Method to click the contact'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.contact)))
            self.click(self.contact)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_add_contact(self):
        '''Method to click add to contact option'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.add_to_contact)))
            self.click(self.add_to_contact)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    def verify_add_contact(self):
        '''Method to verify whether the user is added to contacts'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.add_contact_verify)))
            add_contact = self.find(self.add_contact_verify).text
            assert add_contact == self.add_contact_key
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_key_alert(self):
        '''Method to verify the alert'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.key_error_alert)))
            title = self.find(self.key_error_alert).text
            assert title == self.alert_text
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_key_errormsg(self):
        '''Method to verify the field required error message'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.key_error_msg)))
            title = self.find(self.key_error_msg).text
            assert title == self.error_msg
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")
