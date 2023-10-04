# importing required packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

if __name__ == '__main__':
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
    
    try:
        # Wait for the email input field to become visible
        email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        
        # Enter the email address
        email_input.send_keys("rishabhps@lambdatest.com")
        
        # Find and click the password input field
        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        
        # Enter the password
        password_input.send_keys("password")
        
        # Find and click the login button
        login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
        login_button.click()
        
        # Sleep for 10 seconds (you might want to use WebDriverWait for elements after login)
        sleep(10)
        
    except TimeoutException:
        print("No element found")
    
    # Close the browser
    browser.quit()