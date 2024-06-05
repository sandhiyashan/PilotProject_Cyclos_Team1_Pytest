from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):

    register_Xpath = (By.XPATH,"//div[text()=' Register ']")
    login_xpath = (By.XPATH,"(//div[@class='ml-2'])[3]")
    verify_login_xpath = (By.XPATH,"(//div[@class='top-title'])[2]")
    marketPlace_xpath = (By.XPATH,"//div[text()='Marketplace']")
    Logout_xpath = (By.XPATH,"//a[@aria-label='Logout']//icon//*[name()='svg']")
    #banking_Xpath = (By.XPATH,"//a[@id='menu_banking']")
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
        
    def goToMarketPlace(self):
        self.click(self.marketPlace_xpath)

    def click_the_logout(self):
        self.click(self.Logout_xpath)

    def goToBanking(self):
        self.click(self.banking_xpath)
    
    def verifyBankingPage(self):
        title = self.find(self.banking_page_verify).text
        assert title == self.banking_page_keyword
    

