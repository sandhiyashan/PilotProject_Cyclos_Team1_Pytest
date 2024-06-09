from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self._driver=driver
        self._wait = WebDriverWait(self._driver,10)
        self._action = ActionChains(self._driver)

    def find(self, locator):
        return self._driver.find_element(*locator)
    
    def click(self, locator):
        element = self.find(locator)
        element.click()

    def send_keys(self, locator,text):
        element = self.find(locator)
        element.send_keys(text)
        
    
    def find_Elements(self, locator):
        return self._driver.find_elements(*locator)

    def wait_for_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))
    
    def switch_to_window(self):
        self._driver.switch_to.window(self._driver.window_handles[1])
        
