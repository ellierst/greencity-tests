from selenium.webdriver.common.by import By
from driver_factory import create_driver
from pages.events_page import EventsPage


if __name__ == "__main__":
    driver = create_driver()
    try:
        events_page = EventsPage(driver)
        events_page.open()

        list_view_btn = events_page.click_list_view()
        events_page.wait_for_list_view_active(list_view_btn)
        assert list_view_btn.get_attribute("aria-pressed") == "true", \
            "List view is not activated"
        print(f"List view attribute aria-pressed is {list_view_btn.get_attribute('aria-pressed')}")

        posts = events_page.get_event_cards()
        for post in posts:
            card = post.find_element(By.CSS_SELECTOR, ".card-wrapper")
            assert "list-view" in card.get_attribute("class"), \
                "Post is not displayed in list view"
        print("Posts are displayed in list view.")

        events_page.click_table_view()
        events_page.wait_for_list_view_inactive(list_view_btn)
        assert list_view_btn.get_attribute("aria-pressed") == "false", \
            "List view is still activated"
        print(f"List view attribute aria-pressed is {list_view_btn.get_attribute('aria-pressed')}")

        print("TC_02 PASSED: View toggle works correctly")
    finally:
        driver.quit()