from driver_factory import create_driver
from pages.events_page import EventsPage


if __name__ == "__main__":
    driver = create_driver()
    try:
        events_page = EventsPage(driver)
        events_page.open()

        events_page.open_date_dropdown()
        events_page.select_date_range_oct_2020()

        no_results_msg = events_page.get_no_results_message()
        print(f"Not found message displayed: {no_results_msg.text.strip()}")

        events_page.close_date_filter()
        print("TC_03 PASSED: No results message is displayed for empty date range")
    finally:
        driver.quit()