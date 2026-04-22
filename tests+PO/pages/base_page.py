from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    events_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator)

    def click_sign_in(self):
        self.get_sign_in_button().click()

    def get_events_link(self):
        return self.driver.find_element(*self.events_link_locator)

    def navigate_to_events(self):
        self.get_events_link().click()