from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from Pages.BasePage import BasePage

class HomePage(BasePage):

    register_Xpath = (By.XPATH,"//div[text()=' Register ']")
    login_xpath = (By.XPATH,"(//div[@class='ml-2'])[3]")
    verify_login_xpath = (By.XPATH,"(//div[@class='top-title'])[2]")
    marketPlace_xpath = (By.XPATH,"//div[text()='Marketplace']")
    marketplace_title_xpath = (By.XPATH,"//div[@class='side-menu-title' and text()=' Marketplace ']")
    marketplace_key = "Marketplace"
    Logout_xpath = (By.XPATH,"//a[@aria-label='Logout']//icon//*[name()='svg']")
    banking_page_verify = (By.XPATH,"//div[@class='side-menu-title' and text()=' Banking ']")
    banking_page_keyword = "Banking"
    banking_xpath = (By.XPATH, "//div[text()='Banking']")

    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.driver = driver

    def goToRegister(self):
        try:
            self.click(self.register_Xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def goToLogin(self):
        try:
            self.click(self.login_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verifyLogin(self):
        try:
            title = self.find(self.verify_login_xpath).text
            assert title == 'Cyclos'
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        
    def goToMarketPlace(self):
        try:
            self.click(self.marketPlace_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def verify_marketplace(self):
        '''Method to verify the marketplace page'''
        try:
            self._wait.until(expected_conditions.visibility_of_element_located((self.marketplace_title_xpath)))
            marketplace_title = self.find(self.marketplace_title_xpath).text
            assert marketplace_title == self.marketplace_key
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def click_the_logout(self):
        try:
            self.click(self.Logout_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def goToBanking(self):
        try:
            self.click(self.banking_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    def verifyBankingPage(self):
        try:
            title = self.find(self.banking_page_verify).text
            assert title == self.banking_page_keyword
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
    

