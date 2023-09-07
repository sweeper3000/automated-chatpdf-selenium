
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

### MODIFY THESE ###
file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Case1.pdf')
questions = ["Who are the parties involved in the case?", "What is the case about?", "What was the verdict?", "What is the name of the accused person and what charges are they facing?", "Where does the accused live and work?", "What is their occupation and level of education?", "Are there any prior criminal charges against them?", "Do they have any mental health issues or disabilities?", "What is their marital status and do they have any children?", "Are they currently on probation or parole for another offense?", "Are there any witnesses or victims that can attest to the accused's behavior?", "Are there any mitigating or aggravating circumstances that should be considered?", "Has the accused confessed to the crime or shown remorse?"]

# Setup Firefox options
options = webdriver.FirefoxOptions()

# Initialize the driver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

# Open the website
url = 'https://www.chatpdf.com/'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Get the file path

# Find the file input element and upload the file
file_input = driver.find_element_by_css_selector('input[type="file"]')
file_input.send_keys(file_path)

time.sleep(5)

# Find the chat input element
chat_input = driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div[3]/div/textarea')

# Find the submit button
submit_button = driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div[3]/div/button')

# List of questions

# Ask the questions
for question in questions:
    chat_input.send_keys(question)
    # Wait until the submit button becomes clickable
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[5]/div/div[3]/div/button')))
    submit_button.click()
    time.sleep(5)
