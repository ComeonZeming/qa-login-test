from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 👇 Replace this with the path to your actual chromedriver.exe
chrome_driver_path = r"C:\QAProject\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

# Launch the Chrome browser
driver = webdriver.Chrome(service=service)

# Open the test login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Locate and fill in the username field
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("student")

# Locate and fill in the password field
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Password123")

# Locate and click the login button
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Wait for page transition
time.sleep(2)

# Check if login was successful by looking for confirmation text
if "Logged In Successfully" in driver.page_source:
    print("✅ Test Passed: Login successful.")
else:
    print("❌ Test Failed: Login unsuccessful.")

# Wait a bit and then close the browser
time.sleep(2)
driver.quit()
