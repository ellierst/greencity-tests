from selenium.webdriver.common.by import By
from driver_factory import create_driver
from pages.events_page import EventsPage


if __name__ == "__main__":
    driver = create_driver()
    try:
        events_page = EventsPage(driver)
        events_page.open()

        events_page.open_type_dropdown()
        events_page.select_social_type()

        posts = events_page.get_event_cards()
        assert len(posts) > 0, "No posts found"

        for post in posts:
            tags = post.find_elements(By.CSS_SELECTOR, "span.tag-active")
            assert len(tags) > 0, "No tags in post"
            assert any(tag.text.strip() in {"Social", "СОЦІАЛЬНИЙ"} for tag in tags), \
                f"No Social tag in post. Found: {[t.text for t in tags]}"
            print(f"Post with Social tag found: {[t.text for t in tags]}")

        events_page.close_filter()
        print("TC_01 PASSED: All posts contain Social tag")
    finally:
        driver.quit()