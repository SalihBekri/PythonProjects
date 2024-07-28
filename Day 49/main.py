from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

# Credentials
load_dotenv(".env")
User = os.getenv("USER")
Pass = os.getenv("PASS")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_webdriver_path = "c:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_webdriver_path), options=options)
driver.get(
    "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")

# SIGNING IN
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(User)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(Pass)

submit_button = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
submit_button.click()
#############################

# SEARCHING
job_adv_btn = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]")
job_adv_btn.click()

search_input = driver.find_element(By.ID, "jobs-search-box-keyword-id-ember183")
search_input.send_keys("python")
time.sleep(1)
search_input.send_keys(Keys.ENTER)
time.sleep(1)
country = driver.find_element(By.XPATH,"/html/body/div[5]/header/div/div/div/div[2]/div[3]")
country.click()
# FILTERS
experience_filter = driver.find_element(By.ID, "searchFilter_experience")
experience_filter.click()
experty = driver.find_element(By.XPATH,
                              "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[2]/label/p/span[1]")
experty.click()
# time.sleep(0.5)
# submit_1 = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span")
# submit_1.click()
# time.sleep(1)
# job_type = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[6]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[1]")
# job_type.click()
