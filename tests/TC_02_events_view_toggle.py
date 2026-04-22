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
    
    list_view_button_xpath = "//button[@aria-label='list view']"
    list_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, list_view_button_xpath)))
    assert list_view_button.is_displayed(), "List view button is not displayed"
    list_view_button.click()

    wait.until(lambda d: list_view_button.get_attribute("aria-pressed") == "true")
    assert list_view_button.get_attribute("aria-pressed") == "true", \
        "List view is not activated"
    print(f"List view attribute aria-pressed is {list_view_button.get_attribute('aria-pressed')}")

    posts = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "mat-card.event-list-item")
        )
    )
    for post in posts:
        card = post.find_element(By.CSS_SELECTOR, ".card-wrapper")
        assert "list-view" in card.get_attribute("class"), \
            "Post is not displayed in list view"
    print(f"Posts are displayed in list view.")

    table_view_button_xpath = "//button[@aria-label='table view']"
    table_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, table_view_button_xpath)))
    assert table_view_button.is_displayed(), "Table view button is not displayed"
    table_view_button.click()

    wait.until(lambda d: list_view_button.get_attribute("aria-pressed") == "false")
    assert list_view_button.get_attribute("aria-pressed") == "false", \
        "List view is still activated"
    print(f"List view attribute aria-pressed is {list_view_button.get_attribute('aria-pressed')}")

    driver.quit()