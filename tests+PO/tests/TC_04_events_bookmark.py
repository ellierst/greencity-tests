import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from driver_factory import create_driver
from pages.events_page import EventsPage
from pages.sign_in_page import SignInPage
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


if __name__ == "__main__":
    driver = create_driver()
    try:
        driver.get("https://www.greencity.cx.ua/#/greenCity")
        sign_in_page = SignInPage(driver)
        sign_in_page.wait.until(EC.element_to_be_clickable(SignInPage.sign_in_button_locator))
        sign_in_page.login(os.getenv("TEST_EMAIL"), os.getenv("TEST_PASSWORD"))

        events_page = EventsPage(driver)
        events_page.open()

        flag = events_page.get_first_favorites_flag()
        _, event_title = events_page.get_event_with_flag()
        print(f"Saving event: {event_title}")

        flag.click()
        assert "flag-active" in flag.get_attribute("class"), \
            "Favorites flag did not become active"
        print("Favorites flag is active")

        events_page.open_bookmarks()
        saved_titles = events_page.get_saved_event_titles()
        print(f"Found {len(saved_titles)} saved events in bookmarks: {saved_titles}")

        assert event_title in saved_titles, \
            f"Event '{event_title}' not found in saved events. Found: {saved_titles}"
        print(f"✓ Event '{event_title}' successfully saved to bookmarks")

        events_page.open()
        event_card = events_page.get_event_card_by_title(event_title)
        active_flag = event_card.find_element(By.CSS_SELECTOR, ".flag-active")
        assert active_flag.is_displayed(), "Active flag is not displayed on the event card"
        active_flag.click()
        events_page.wait.until(lambda d: "flag-active" not in active_flag.get_attribute("class"))
        assert "flag-active" not in active_flag.get_attribute("class"), \
            "Favorites flag did not become inactive"

        events_page.open_bookmarks()
        saved_titles_after = events_page.get_saved_event_titles()
        print(f"Found {len(saved_titles_after)} saved events after removal: {saved_titles_after}")

        assert event_title not in saved_titles_after, \
            f"Event '{event_title}' still found in saved events."
        print(f"✓ Event '{event_title}' successfully deleted from bookmarks")

        print("TC_04 PASSED: Bookmark add/remove works correctly")
    finally:
        driver.quit()