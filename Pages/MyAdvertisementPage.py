import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class MyAdvertisementPage(BasePage):

    advertisements_xpath = (By.XPATH,"//div[text()='My advertisements']")
    add_new_xpath = (By.XPATH,"//div[text()='Add new']")
    title_xpath = (By.XPATH,"//input-field[@formcontrolname='name']/label-value/div/div/input")
    category_xpath = (By.XPATH,"//single-selection-field[@formcontrolname='categories']/label-value/div/div/div/button")
    item_xpath = (By.XPATH,"(//a[@class='select-option leaf level0 mt-1'])[1]")
    price_css = (By.CSS_SELECTOR,"input[type='tel']")
    textArea_xpath = (By.XPATH,"//div[@class='wrapper']/div[@class='editor']")
    save_btn_css = (By.CSS_SELECTOR,"button[class='btn d-flex justify-content-center align-items-center w-100 h-100 btn-primary']")
    keywords_xpath = (By.XPATH,"//input-field[@formcontrolname='keywords']/label-value/div/div/input")
    search_result_xpath = (By.XPATH,"//div[@class='card-text']")
    searched_element = "Lion"

    def click_my_advertisements(self):
        self.click(self.advertisements_xpath)

    def add_new_advertisements(self):
        self.click(self.add_new_xpath)

    def fill_advertisement(self):
        self.send_keys(self.title_xpath,"Orange")
        self.click(self.category_xpath)
        self.click(self.item_xpath)
        self.send_keys(self.price_css,"200")
        self.send_keys(self.textArea_xpath,"It;s very Delicious")

    def click_save_button(self):
        self.click(self.save_btn_css)

    def search_functionality(self):
        self.click(self.keywords_xpath)
        self.send_keys(self.keywords_xpath,self.searched_element)
        time.sleep(3)

    def verify_result(self):
        store = self.find(self.search_result_xpath).text
        assert store == self.searched_element
