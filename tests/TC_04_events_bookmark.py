from dotenv import load_dotenv
from testing import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

load_dotenv()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.greencity.cx.ua/#/greenCity")
    wait = WebDriverWait(driver, 30)
    
    sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sign_in_selector)))
    sign_in_button.click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button_xpath = "//button[@class='greenStyle']"
    sign_in_button = driver.find_element(By.XPATH, sign_in_button_xpath)
    assert sign_in_button.is_displayed(), "Sign in button is not displayed"
    email_input.send_keys(os.getenv("TEST_EMAIL"))
    password_input.send_keys(os.getenv("TEST_PASSWORD"))
    sign_in_button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "header_user-wrp")))
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    favorites_flag_xpath = "//span[@class='flag']"
    favorites_flag = wait.until(EC.visibility_of_element_located((By.XPATH, favorites_flag_xpath)))
    assert favorites_flag.is_displayed(), "Favorites flag is not displayed"

    event_details = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-card[.//span[@class='flag']]")))
    event_title = event_details.find_element(By.CSS_SELECTOR, ".event-title").text
    
    print(f"Saved event: {event_title}")

    favorites_flag.click()
    assert "flag-active" in favorites_flag.get_attribute("class"), \
        "Favorites flag did not become active"
    print("Favorites flag is active")

    driver.get("https://www.greencity.cx.ua/#/greenCity/events?isBookmark=true&section=events")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".event-list-item")))

    events_with_favorites = driver.find_elements(By.XPATH, "//mat-card")

    saved_titles = [
        event.find_element(By.CSS_SELECTOR, ".event-title").text
        for event in events_with_favorites
    ]

    print(f"Found {len(saved_titles)} saved events in bookmarks:")
    print(saved_titles)

    assert event_title in saved_titles, \
        f"Event '{event_title}' not found in saved events. Found: {saved_titles}"
    print(f"✓ Event '{event_title}' successfully saved to bookmarks")
    
    
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    event_card = wait.until(EC.presence_of_element_located((By.XPATH, f"//mat-card[.//p[contains(text(), '{event_title}')]]")))
    flag = event_card.find_element(By.CSS_SELECTOR, ".flag-active")
    assert flag.is_displayed(), "Favorites flag is not displayed on the event card"
    flag.click()
    wait.until(lambda d: "flag-active" not in flag.get_attribute("class"))
    assert "flag-active" not in flag.get_attribute("class"), \
        "Favorites flag did not become inactive"
    
    driver.get("https://www.greencity.cx.ua/#/greenCity/events?isBookmark=true&section=events")

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".event-list-item")))

    events_with_favorites = driver.find_elements(By.XPATH, "//mat-card")

    saved_titles_after = [
        event.find_element(By.CSS_SELECTOR, ".event-title").text
        for event in events_with_favorites
    ]

    print(f"Found {len(saved_titles_after)} saved events in bookmarks:")
    print(saved_titles_after)

    assert event_title not in saved_titles_after, \
        f"Event '{event_title}' found in saved events."
    print(f"✓ Event '{event_title}' successfully deleted from bookmarks")

    driver.quit()