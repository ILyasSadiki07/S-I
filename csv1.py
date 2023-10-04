import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def run_test(email, password):
    try:
        # Set the path to the Microsoft Edge WebDriver executable
        edge_driver_path = 'C:\\edgedriver\\msedgedriver.exe'
        
        # Create Edge WebDriver instance with specified options
        options = webdriver.EdgeOptions()
        
        # Create a WebDriver service with the executable path
        service = webdriver.EdgeService(executable_path=edge_driver_path)
        
        # Initialize the Edge browser
        browser = webdriver.Edge(service=service, options=options)
        
        # Maximize the browser window
        browser.maximize_window()
        
        # Navigate to the LambdaTest login page
        browser.get('https://accounts.lambdatest.com/login?_gl=1*kscq4z*_gcl_au*MTA2ODc1OTI4Ny4xNjk1NzMyOTM3')
        
        # Wait for the email input field to become visible
        email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        
        # Enter the email address from the CSV
        email_input.send_keys(email)
        
        # Find and click the password input field
        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        
        # Enter the password from the CSV
        password_input.send_keys(password)
        
        # Find and click the login button
        login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
        login_button.click()
        
        # Sleep for 10 seconds (you might want to use WebDriverWait for elements after login)
        time.sleep(10)
        
        # Perform your test assertions here
        
        # Close the browser
        browser.quit()
        
        return "OK"  # Test was successful
        
    except TimeoutException:
        print("No element found")
        return "KO"  # Test failed

if __name__ == '__main__':
    # Open the CSV file for reading
    with open('Classeur1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row['mail']
            password = row['pwd']
            
            result = run_test(email, password)
            
            if result == "OK":
                print("Test for email:", email, "PASSED")
            else:
                print("Test for email:", email, "FAILED")