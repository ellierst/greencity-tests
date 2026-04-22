from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")
    wait = WebDriverWait(driver, 10)
    
    type_button_id = "mat-select-6"
    type_of_events = wait.until(EC.element_to_be_clickable((By.ID, type_button_id)))
    assert type_of_events.is_displayed(), "Type of events dropdown is not displayed"
    type_of_events.click()
    
    type_of_events_social_xpath = "//*[@id='mat-option-11']/span"
    social_option = wait.until(EC.element_to_be_clickable((By.XPATH, type_of_events_social_xpath)))
    assert social_option.is_displayed(), "Social option is not displayed"
    social_option.click()

    posts_container_selector = "mat-card.event-list-item"
    posts = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, posts_container_selector)))
    assert len(posts) > 0, "No posts found"
    for post in posts:
        tags = post.find_elements(By.CSS_SELECTOR, "span.tag-active")
        
        assert len(tags) > 0, "No tags in post"

        assert any(tag.text.strip() in {"Social", "СОЦІАЛЬНИЙ"} for tag in tags), \
            f"No Social tag in post. Found: {[t.text for t in tags]}"
        
        print(f"Post with Social tag found: {[t.text for t in tags]}")
    
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
    close_button_xpath = "//div[@class='cross-container']"
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
    assert close_button.is_displayed(), "Close button is not displayed"
    close_button.click()

    driver.quit()