from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

if __name__ == '__main__':
    # Set the path to the Microsoft Edge WebDriver executable
    edge_driver_path = 'C:\edgedriver\msedgedriver.exe'

    # Create Edge WebDriver instance with specified options
    options = webdriver.EdgeOptions()

    # Create a WebDriver service with the executable path
    service = webdriver.EdgeService(executable_path=edge_driver_path)

    # Initialize the Edge browser
    browser = webdriver.Edge(service=service, options=options)

    browser.maximize_window()
    browser.get('https://lambdatest.github.io/sample-todo-app/')

    try:
        # Click on the first todo item
        li1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "li1")))
        li1.click()

        # Click on the second todo item
        li2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'li2')))
        li2.click()

        # Verify the title of the page
        expected_title = "Sample page - lambdatest.com"
        assert expected_title == browser.title

        # Enter text in the text field
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, 'sampletodotext')))
        email_text_field.send_keys(sample_text)

        # Click the Add button
        add_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "addbutton")))
        add_button.click()

        sleep(60)  # Give some time to see the changes

    except TimeoutException:
        print("Element not found")

    finally:
        browser.close()
