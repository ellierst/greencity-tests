from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")
    wait = WebDriverWait(driver, 10)
    
    data_button_xpath = "//div[@class='mat-mdc-select-arrow']"
    data_button = wait.until(EC.element_to_be_clickable((By.XPATH, data_button_xpath)))
    assert data_button.is_displayed(), "Data button is not displayed"
    data_button.click()

    button_date_xpath = "//span[@class='mdc-button__label']"
    change_year_xpath = "//span[contains(text(), '2020')]"
    change_month_xpath = "//span[contains(text(), 'ЖОВТ.')]"
    change_start_day_xpath = "//button//span[contains(text(), '23')]"
    change_end_day_xpath = "//span[contains(text(), '29')]"

    change_year_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_date_xpath)))
    assert change_year_button.is_displayed(), "Change year button is not displayed"
    change_year_button.click()

    change_year_option = wait.until(EC.element_to_be_clickable((By.XPATH, change_year_xpath)))
    assert change_year_option.is_displayed(), "Change year option is not displayed"
    change_year_option.click()

    change_month_option = wait.until(EC.element_to_be_clickable((By.XPATH, change_month_xpath)))
    assert change_month_option.is_displayed(), "Change month option is not displayed"
    change_month_option.click()

    change_start_day_option = wait.until(EC.element_to_be_clickable((By.XPATH, change_start_day_xpath)))
    assert change_start_day_option.is_displayed(), "Change start day option is not displayed"
    change_start_day_option.click()

    change_end_day_option = wait.until(EC.element_to_be_clickable((By.XPATH, change_end_day_xpath)))
    assert change_end_day_option.is_displayed(), "Change end day option is not displayed"
    change_end_day_option.click()

    not_found_message_xpath = "//p[@class='end-page-txt ng-star-inserted']"
    wait.until(EC.visibility_of_element_located((By.XPATH, not_found_message_xpath)))
    not_found_message = driver.find_element(By.XPATH, not_found_message_xpath)
    assert not_found_message.is_displayed(), "Not found message is not displayed"
    print(f"Not found message displayed: {not_found_message.text.strip()}")

    close_button_xpath = "//div[@class='cross-container']"
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
    assert close_button.is_displayed(), "Close button is not displayed"
    close_button.click()

    driver.quit()