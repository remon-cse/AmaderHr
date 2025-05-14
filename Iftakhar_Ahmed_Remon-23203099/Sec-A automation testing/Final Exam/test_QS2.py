from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dropdown")

    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))

    select = Select(dropdown_element)
    select.select_by_visible_text("Option 2")

    selected_option = select.first_selected_option
    print("Selected option:", selected_option.text)

finally:
    driver.quit()
