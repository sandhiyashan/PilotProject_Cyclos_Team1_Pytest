import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Pages.BasePage import BasePage


class Advertisement(BasePage):

    advertisment_xpath = (By.XPATH , "//div[text()='Advertisements']")
    keyword_xpath = (By.XPATH , "(//div[@class='d-flex label-value-value']//input)[1]")
    keyword_based_xpath = (By.XPATH, "//div[text()=' Orange ']")
    invalid_msg_xpath = (By.XPATH, "//div[text()='Invalid keywords']")
    price_xpath = (By.XPATH, "//div[@class='card-title']")
    show_advertisement_xpath = (By.XPATH , "//span[text()='Show advertisements']")
    order_By = (By.XPATH, "//div[@class='w-100 mw-100 text-truncate pr-3']")
    relevance = (By.XPATH, "//a[@class='select-option mt-1']")
    last_published = (By.XPATH, "//div[@class='dropdown-menu show']//a[2]")
    verify_last = (By.XPATH, "(//div[text()=' Orange '])[1]")
    lowest_price = (By.XPATH , "//div[@class='dropdown-menu show']//a[3]")
    highest_price = (By.XPATH, "//div[@class='dropdown-menu show']//a[4]")
    favourite = (By.XPATH, "//label[@class='custom-control-label']")
    like_button = (By.XPATH,"//div[text()='Add to favorites']")
    remove_fav = (By.XPATH, "//div[text()='Remove from favorites']")

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
  
    def click_show_advertisement(self):
        self.click(self.show_advertisement_xpath)
    
    def click_orderBy(self):
        self._wait.until(ec.visibility_of_element_located((self.order_By)))
        self.click(self.order_By)
        time.sleep(3)
    
    def click_relevance(self):
        self.click(self.relevance)

    def click_last_Published(self):
        self.click(self.last_published)

    def verify_last_published(self):
        element = self._wait.until(ec.visibility_of_element_located((self.verify_last)))
        assert element.text == "Orange"
    
    def click_highest_price(self):
        self.click(self.highest_price)
    
    def click_lowest_price(self):
        self.click(self.lowest_price)
       
    def verify_lowest_price(self):
        prices = []
        time.sleep(5)
        elements = self.find_Elements(self.price_xpath)
        for element in elements:
            text = element.text
            price = text.split()[0]  # Assuming the price is the first part of the text
            price = price.replace(',', '')  # Remove commas from the price
            prices.append(int(price))
        # Assert that the prices are sorted in ascending order
        assert prices == prices , "prices are not in sorted order"

    def click_Favourite_checkbox(self):
        self.click(self.favourite)
    
    def add_to_favourite(self):

        self._wait.until(ec.visibility_of_element_located((self.verify_last)))
        self.click(self.verify_last)
        self._wait.until(ec.visibility_of_element_located((self.like_button)))
        self.click(self.like_button)

    def verify_product_added_to_favourite(self):
        element = self._wait.until(ec.visibility_of_element_located((self.verify_last)))
        assert element.text == "Orange"
    
    def remove_From_Favourite(self):
        self._wait.until(ec.visibility_of_element_located((self.verify_last)))
        self.click(self.verify_last)
        self._wait.until(ec.visibility_of_element_located((self.remove_fav)))
        self.click(self.remove_fav)

    def verify_product_removed_favuorite(self):
        element = self.find(self.like_button).text
        assert element == "Add to favorites"