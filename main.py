from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options



s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://gb.ru/login')

login = driver.find_element(By.ID, "user_email")
login.send_keys("study.ai_172@mail.ru")

pwd = driver.find_element(By.ID, "user_password")
pwd.send_keys("Password172!")
pwd.send_keys(Keys.ENTER)

profile_link = driver.find_element(By.XPATH, "//a[contains(@href,'/users/')]").get_attribute('href')
driver.get(profile_link)

edit_profile = driver.find_element(By.CLASS_NAME, "text-sm").get_attribute('href')
driver.get(edit_profile)

timezone = driver.find_element(By.NAME, "user[time_zone]")
select = Select(timezone)
select.select_by_value('Vladivostok')
timezone.submit()


print()

