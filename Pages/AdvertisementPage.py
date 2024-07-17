import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
        '''Click the Advertisement button in Advertisment page'''
        try:
            self.wait_for_element(self.advertisment_xpath)
            self.click(self.advertisment_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def enter_keyword(self,data):
        '''Enter the keyword into the keyword field'''
        try:
            self.wait_for_element(self.keyword_xpath)
            time.sleep(3)
            self.send_keys(self.keyword_xpath, data)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def verify_keyword_based_element(self):
        '''Verify the keyword based elements are displayed'''
        try:
            self.wait_for_element(self.keyword_based_xpath)
            time.sleep(3)
            elements = self.find_Elements(self.keyword_based_xpath)
            for element in elements:
                assert element.text == "Orange"
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def verify_invalid_keyword_error_msg(self):
        '''Verify the invalid keyword error message is displayed'''
        try:
            error_msg = self.wait_for_element(self.invalid_msg_xpath).text
            assert error_msg == "Invalid keywords"
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"Error Message: {e}")
  
    def click_show_advertisement(self):
        '''Click the show Advertisment button in Advertisement page'''
        try:
            self.click(self.show_advertisement_xpath)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")
    
    def click_orderBy(self):
        '''Click the dropdown button order by '''
        try:
            self.wait_for_element(self.order_By)
            self.click(self.order_By)
            time.sleep(3)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_relevance(self):
        '''Click the dropdown list Relevance'''
        try:
            self.click(self.relevance)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_last_Published(self):
        '''Click the dropdown list last published'''
        try:
            self.click(self.last_published)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def verify_last_published(self):
        '''Verify the last published'''
        try:
            element = self.wait_for_element(self.verify_last)
            assert element.text == "Orange"
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    
    def click_highest_price(self):
        '''Click the dropdown list highest price'''
        try:
            self.click(self.highest_price)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_lowest_price(self):
        '''Click the dropdown list lowest price'''
        try:
            self.click(self.lowest_price)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

       
    def verify_lowest_price(self):
        '''Verify the lowest price product are displayed first'''
        try:
            prices = []
            time.sleep(5)
            elements = self.find_Elements(self.price_xpath)
            for element in elements:
                text = element.text
                price = text.split()[0]  # price is the first part of the text
                price = price.replace(',', '')  # Remove commas from the price
                prices.append(int(price))
            # Assert that the prices are in ascending order
            assert prices == prices , "prices are not in sorted order"
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def click_Favourite_checkbox(self):
        '''click the Favourite checkbox'''
        try:
            self.click(self.favourite)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    
    def add_to_favourite(self):
        '''Add product to the Favourite list'''
        try:
            self.wait_for_element(self.verify_last)
            self.click(self.verify_last)
            self.wait_for_element(self.like_button)
            self.click(self.like_button)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def verify_product_added_to_favourite(self):
        '''Verify product added to the Favourite list'''
        try:
            element = self.wait_for_element(self.verify_last)
            assert element.text == "Orange"
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def remove_From_Favourite(self):
        '''Remove product from the favourite list'''
        try:
            self.wait_for_element(self.verify_last)
            self.click(self.verify_last)
            self.wait_for_element(self.remove_fav)
            self.click(self.remove_fav)
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")

    def verify_product_removed_favuorite(self):
        '''Verify that the product removed from the Favourite list'''
        try:
            element = self.wait_for_element(self.like_button).text
            assert element == "Add to favorites"
        except NoSuchElementException as e:
            print(f"Element cannot be located: {e}")
        except Exception as e:
            print(f"Error Message: {e}")
