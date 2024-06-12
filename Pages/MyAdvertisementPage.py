import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
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

    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.driver = driver

    def click_my_advertisements(self):
        '''click my advertisements button on home page'''
        try:
            self.click(self.advertisements_xpath)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def add_new_advertisements(self):
        '''click add new advertisements icon'''
        try:
            self.click(self.add_new_xpath)
        except ElementNotInteractableException as e:
            print(f"Element not interactable: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def fill_advertisement(self):
        '''fill the details in advertisements form'''
        try:
            self.send_keys(self.title_xpath, "Orange")
            self.click(self.category_xpath)
            self.click(self.item_xpath)
            self.send_keys(self.price_css, "200")
            self.send_keys(self.textArea_xpath, "It's very Delicious")
        except Exception as e:
            print(f"Error: {e}")

    def click_save_button(self):
        '''click save button on advertisements form'''
        try:
            self.click(self.save_btn_css)
        except ElementNotInteractableException as e:
            print(f"Element not interactable: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def search_functionality(self):
        '''click the search button and send keys to search'''
        try:
            self.click(self.keywords_xpath)
            self.send_keys(self.keywords_xpath, self.searched_element)
            time.sleep(3)  # Assuming you need this wait
        except TimeoutException as e:
            print(f"Timeout Exception occurred: {e}")
        except Exception as e:
            print(f"Error occurred: {e}")

    def verify_result(self):
        '''verify the result on search functionality'''
        try:
            store = self.find(self.search_result_xpath).text
            assert store == self.searched_element
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Error: {e}")
