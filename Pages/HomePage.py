from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Pages.BasePage import BasePage

class HomePage(BasePage):

    register_Xpath = (By.XPATH,"//div[text()=' Register ']")
    login_xpath = (By.XPATH,"(//div[@class='ml-2'])[3]")
    verify_login_xpath = (By.XPATH,"(//div[@class='top-title'])[2]")
    marketPlace_xpath = (By.XPATH,"//a[@id='menu_marketplace']")
    marketplace_title_xpath = (By.XPATH,"//div[@class='side-menu-title' and text()=' Marketplace ']")
    marketplace_key = "Marketplace"
    Logout_xpath = (By.XPATH,"//a[@aria-label='Logout']//icon//*[name()='svg']")
    banking_page_verify = (By.XPATH,"//div[@class='side-menu-title' and text()=' Banking ']")
    banking_page_keyword = "Banking"
    banking_xpath = (By.XPATH, "//div[text()='Banking']")

    def goToRegister(self):
        self.click(self.register_Xpath)

    def goToLogin(self):
        self.click(self.login_xpath)

    def verifyLogin(self):
        title = self.find(self.verify_login_xpath).text
        assert title == 'Cyclos'
        
    def click_the_logout(self):
        self.click(self.Logout_xpath)

    def goToBanking(self):
        self.click(self.banking_xpath)
    
    def verifyBankingPage(self):
        title = self.find(self.banking_page_verify).text
        assert title == self.banking_page_keyword
    
    def goToMarketPlace(self):
        self._wait.until(expected_conditions.visibility_of_element_located((self.marketPlace_xpath)))
        self.click(self.marketPlace_xpath)

    def verify_marketplace(self):
        self._wait.until(expected_conditions.visibility_of_element_located((self.marketplace_title_xpath)))
        marketplace_title = self.find(self.marketplace_title_xpath).text
        assert marketplace_title == self.marketplace_key


