from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
# renseigner le chemin de votre msedgedriver dans executable_path
service = Service(executable_path='C:\edgedriver\msedgedriver.exe')
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

driver.get("https://www.linkedin.com/pulse/selenium-un-guide-exhaustif-pour-lautomatisation-des-tests-barta/")

# ...
sleep(10)
driver.quit()