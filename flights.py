
#importing everything we need
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

#creates a service instance to use the webdriber
service = Service()

#creates chrome path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # this keeps the window open post execution/errors/ changing frames (explained later)

prefs = {"download.default_directory": '/Users/justinpaul/Downloads',  # note need to change this
         "directory_upgrade": True}
chrome_options.add_experimental_option("prefs", prefs)

#creates a chrome webdriver 
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

# We use this to create multiple actions and execute them at once
actions = ActionChains(driver)

#gets driver for flight website 
chromeFlights = 'https://www.google.com/travel/flights'
driver.get(chromeFlights)


#asking the user for their phone number 
phone_number = input("Please enter your phone number: ")
max_price = input("What is the max you are willing to pay: ")
nearest_airport = input("Enter your city: ")


# Find the element containing the price (you'll need to inspect the webpage to find the specific element)
# For example, if the price is in a <span> element with a class 'price':
price_element = driver.find_element_by_class_name('price')

# Get the text content of the element
price = price_element.text

# Print or do further processing with the price
print('The price is:', price)
