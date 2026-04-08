from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://hikka.io")
    print(driver.title)

    sleep(2)

    search = driver.find_element(By.XPATH, "//button[.//span[contains(text(),'Пошук...')]]")
    search.click()

    sleep(2)

    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Пошук...']")
    search_input.send_keys("Given")

    sleep(2)

    choose = driver.find_element(By.XPATH, "//a[(@href='/anime/given-90c446')]")
    choose.click()

    
    sleep(5)
    driver.quit()