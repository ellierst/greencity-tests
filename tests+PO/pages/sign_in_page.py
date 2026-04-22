from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignInPage(BasePage):
    email_input_locator = (By.ID, "email")
    password_input_locator = (By.ID, "password")
    submit_button_locator = (By.XPATH, "//button[@class='greenStyle']")
    user_header_locator = (By.ID, "header_user-wrp")

    def login(self, email, password):
        self.click_sign_in()
        self.driver.find_element(*self.email_input_locator).send_keys(email)
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        submit_button = self.driver.find_element(*self.submit_button_locator)
        assert submit_button.is_displayed(), "Sign in button is not displayed"
        submit_button.click()
        self.wait.until(EC.visibility_of_element_located(self.user_header_locator))