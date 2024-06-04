from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support import ui
from selenium.webdriver import ActionChains
from faker import Faker

fake = Faker()

# Initialize the WebDriver (for Edge)
driver = webdriver.Edge()

# Open the webpage
driver.get('https://survey.zohopublic.com/zs/kHCzUh')

# Locate the checkbox using its class name and click it
checkbox = driver.find_element(By.CLASS_NAME, 'zsCheckboxFaux')
checkbox.click()

# Wait for a moment to ensure the checkbox is clicked (optional)
time.sleep(2)

# Locate the button using its class name and click it
button = driver.find_element(By.CLASS_NAME, 'btnFormAction')
button.click()

# Wait between pages
time.sleep(4)

# TODO: randomize radio button selection
# Locate the radio button using its ID and click it
choices = [
    "choiceEffects_972306000000046029",
    "choiceEffects_972306000000046031",
    "choiceEffects_972306000000046033",
    "choiceEffects_972306000000046035",
    "choiceEffects_972306000000046037"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()
time.sleep(5)

# First name
first_name = fake.first_name()
text_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="First Name"]')
text_box.send_keys(first_name)

# Last Name
last_name = fake.last_name()
text_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Last Name"]')
text_box.send_keys(last_name)

# email
email = fake.email()
text_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="question_message_972306000000046071 hintmessage_972306000000046071"]')
text_box.send_keys(email)

# company name
company = fake.company()
text_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="question_message_972306000000046079 hintmessage_972306000000046079"]')
text_box.send_keys(company)

# press next button
next_button = driver.find_element(By.CLASS_NAME, 'btnFormAction.next')
next_button.click()

# Page 3 start
time.sleep(4)

driver.execute_script("window.scrollBy(0, 500);")

time.sleep(4)


section = driver.find_element(By.ID, 'matrix_question_972306000000046125')
column_group_div = section.find_element(By.ID, "matrixradiochoice")

question_5_sub_questions = [
    "matrix_choice_0", 
    "matrix_choice_1", 
    "matrix_choice_2", 
    "matrix_choice_3", 
    "matrix_choice_4", 
    "matrix_choice_5",    
]

options =  ["972306000000046131", "972306000000046133", "972306000000046147", "972306000000046149", "972306000000047089"]
for sub_question in question_5_sub_questions:
    question_div = column_group_div.find_element(By.CSS_SELECTOR, f'div[name="{sub_question}"]')
    # TODO: randomize which radio to select here
    choice = random.choice(options)
    radio_choice_div = question_div.find_element(By.CSS_SELECTOR, f'div[answer_field_id="{choice}"]')
    radio_button = radio_choice_div.find_element(By.CLASS_NAME, 'zsRadioFaux')
    radio_button.click()

# question 6
section = driver.find_element(By.ID, 'matrix_question_972306000000046159')
column_group_div = section.find_element(By.ID, "matrixradiochoice")
question_5_sub_questions = [
    "matrix_choice_0", 
    "matrix_choice_1", 
    "matrix_choice_2", 
    "matrix_choice_3", 
    "matrix_choice_4", 
    "matrix_choice_5",    
]
options =  ["972306000000046173", "972306000000046175", "972306000000046177", "972306000000046179", "972306000000047085"]
for sub_question in question_5_sub_questions:
    question_div = column_group_div.find_element(By.CSS_SELECTOR, f'div[name="{sub_question}"]')
    # TODO: randomize which radio to select here
    choice = random.choice(options)
    radio_choice_div = question_div.find_element(By.CSS_SELECTOR, f'div[answer_field_id="{choice}"]')
    radio_button = radio_choice_div.find_element(By.CLASS_NAME, 'zsRadioFaux')
    radio_button.click()

# question 7
choices = [
    "choiceEffects_972306000000047003", 
    "choiceEffects_972306000000047005",
    "choiceEffects_972306000000047007",
    "choiceEffects_972306000000047009",
    "choiceEffects_972306000000047045"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

driver.execute_script("window.scrollBy(0, 500);")


# question 8
pixel_per_point = 6
slider_range = [-5, 80]
move_slider_by = random.randint(-5, 80) * pixel_per_point
slider_handle = driver.find_element(By.CLASS_NAME, "ui-slider-handle")
move = ActionChains(driver)
move.click_and_hold(slider_handle).move_by_offset(move_slider_by, 0).release().perform()
time.sleep(1)

# question 9
choices = [
    "choiceEffects_972306000000047027", 
    "choiceEffects_972306000000047029",
    "choiceEffects_972306000000047031",
    "choiceEffects_972306000000047033",
    "choiceEffects_972306000000047039"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

# question 10
choices = [
    "972306000000047051",
    "972306000000047053",
    "972306000000047055",
    "972306000000047057",
    "972306000000047059"
]
choice = random.choice(choices)
section = driver.find_element(By.CSS_SELECTOR, 'section[aria-labelledby="question_message_972306000000047049 hintmessage_972306000000047049"]')
li = section.find_element(By.CSS_SELECTOR, f'li[answer_field_id="{choice}"]')
li.find_element(By.CLASS_NAME, "zsRadioFaux").click()

# press next button
next_button = driver.find_element(By.CLASS_NAME, 'btnFormAction.next')
next_button.click()

# Wait for a few seconds to observe the result (optional)
time.sleep(5)


# question 11
choices = [
    "choiceEffects_972306000000047095", 
    "choiceEffects_972306000000047097",
    "choiceEffects_972306000000047099",
    "choiceEffects_972306000000047101",
    "choiceEffects_972306000000047103"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()


# question 12
pixel_per_point = 6
slider_range = [-20, 65]
move_slider_by = random.randint(*slider_range) * pixel_per_point
slider_handle = driver.find_element(By.CLASS_NAME, "ui-slider-handle")
move = ActionChains(driver)
move.click_and_hold(slider_handle).move_by_offset(move_slider_by, 0).release().perform()
time.sleep(5)

# question 13
answer_field_id="972306000000047129"
div = driver.find_element(By.CSS_SELECTOR, 'div[answer_field_id="972306000000047129"]')
checkbox = div.find_element(By.CLASS_NAME, "zsCheckboxFaux").click()

# question 14
section = driver.find_element(By.CSS_SELECTOR, 'section[aria-labelledby="question_message_972306000000047145 hintmessage_972306000000047145"]')
choices = [
    "choiceEffects_972306000000047147",
    "choiceEffects_972306000000047149",
    "choiceEffects_972306000000047151",
    "choiceEffects_972306000000047153",
    "choiceEffects_972306000000047155",
    "choiceEffects_972306000000047157"
]
for choice in choices:
    if random.choice([True, False]):
        section.find_element(By.ID, choice).click()

# question 15
choices = [
    "choiceEffects_972306000000047165",
    "choiceEffects_972306000000047167",
    "choiceEffects_972306000000047169"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

# press next button
next_button = driver.find_element(By.CLASS_NAME, 'btnFormAction.next')
next_button.click()

time.sleep(5)

# page 4

# question 16
choices = [
    "choiceEffects_972306000000048153",
    "choiceEffects_972306000000048155",
    "choiceEffects_972306000000048157"
]
choice = random.choice(choices)
# choice = "choiceEffects_972306000000048153" #TODO: remove this
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

time.sleep(2)

# question 16.1, appears only for no and 3rd option
if choice == choices[0]:
    # question 17/18
    new_choices = [
        "choiceEffects_972306000000047223",
        "choiceEffects_972306000000047225",
        "choiceEffects_972306000000047227",
        "choiceEffects_972306000000047229",
    ]
    new_choice = random.choice(new_choices)
    radio_button = driver.find_element(By.ID, new_choice)
    radio_button.click()

# question 17/18 
choices = [
    "choiceEffects_972306000000047253",
    "choiceEffects_972306000000047267",
    "choiceEffects_972306000000047255",
    "choiceEffects_972306000000047257",
    "choiceEffects_972306000000047259",
    "choiceEffects_972306000000047261"
]
for choice in choices:
    if random.choice([True, False]):
        driver.find_element(By.ID, choice).click()

# question 18/19
choices = [
    "choiceEffects_972306000000047273",
    "choiceEffects_972306000000047275",
    "choiceEffects_972306000000047277",
    "choiceEffects_972306000000047279",
    "choiceEffects_972306000000047281"
]
choice = random.choice(choices)
# choice = "choiceEffects_972306000000048153" #TODO: remove this
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

# question  19/20
choices = [
    "choiceEffects_972306000000048005",
    "choiceEffects_972306000000048009",
    "choiceEffects_972306000000048017",
    
    "choiceEffects_972306000000048019",
    "choiceEffects_972306000000048021",
    "choiceEffects_972306000000048023",

    "choiceEffects_972306000000048025",
    "choiceEffects_972306000000048027",
    "choiceEffects_972306000000048029",

    "choiceEffects_972306000000048031",
    "choiceEffects_972306000000048033",
    "choiceEffects_972306000000048035",

    "choiceEffects_972306000000048037",
    "choiceEffects_972306000000048039",
    "choiceEffects_972306000000048041"
]
for choice in choices:
    if random.choice([True, False]):
        driver.find_element(By.ID, choice).click()

# question 19/20
choices = [
    "choiceEffects_972306000000048055",
    "choiceEffects_972306000000048057",
    "choiceEffects_972306000000048059",
    "choiceEffects_972306000000048061"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

# press next button
next_button = driver.find_element(By.CLASS_NAME, 'btnFormAction.next')
next_button.click()

time.sleep(10)

# page 5

# question 21
choices = [
    "choiceEffects_972306000000048109",
    "choiceEffects_972306000000048111",
    "choiceEffects_972306000000048113"
]
choice = random.choice(choices)
radio_button = driver.find_element(By.ID, choice)
radio_button.click()


# question 21.1, appears only for no and 3rd option
if choice == choices[0]:
    time.sleep(1)
    new_choices = [
        "choiceEffects_972306000000048123",
        "choiceEffects_972306000000048125",
        "choiceEffects_972306000000048127",
        "choiceEffects_972306000000048129"
    ]
    new_choice = random.choice(new_choices)
    driver.find_element(By.ID, new_choice).click()

# question 22/23
choices = [
    "choiceEffects_972306000000048177",
    "choiceEffects_972306000000048179",
    "choiceEffects_972306000000048181"
]
# choice = random.choice(choices)
choice = choices[0] #TODO: remove this 
radio_button = driver.find_element(By.ID, choice)
radio_button.click()

# question 22.1/2, appears only for no and 3rd option
if choice == choices[0]:
    time.sleep(1)
    new_choices_1 = [
        "choiceEffects_972306000000048221",
        "choiceEffects_972306000000048223",
        "choiceEffects_972306000000048225",
        "choiceEffects_972306000000048227"
    ]
    new_choice_1 = random.choice(new_choices_1)
    driver.find_element(By.ID, new_choice_1).click()

    new_choices_2 = [
        "choiceEffects_972306000000048195",
        "choiceEffects_972306000000048197",
        "choiceEffects_972306000000048199"
    ]
    new_choice_2 = random.choice(new_choices_2)
    driver.find_element(By.ID, new_choice_2).click()
    
time.sleep(5)
# press next button
next_button = driver.find_element(By.CLASS_NAME, 'submit')
next_button.click()

time.sleep(20)

# Close the browser
driver.quit()
