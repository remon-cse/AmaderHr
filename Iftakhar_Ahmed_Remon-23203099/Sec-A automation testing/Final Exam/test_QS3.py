from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure to have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()  # Or webdriver.Firefox() if using Firefox

try:
    # 1. Open the browser and navigate to the site
    driver.get("https://www.saucedemo.com/")

    # 2. Locate username and password fields and enter credentials
    username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # 3. Click the login button
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click()

    # 4. Wait for the page to load (basic wait)
    time.sleep(3)

    # 5. Take screenshot
    driver.save_screenshot("results.png")
    print("Screenshot saved as results.png")

finally:
    # Close the browser
    driver.quit()
