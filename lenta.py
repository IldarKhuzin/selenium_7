from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

s = Service('./chromedriver')

chromeOptions = Options()
chromeOptions.add_argument('start-maximized')

driver = webdriver.Chrome(service=s, options=chromeOptions)
driver.implicitly_wait(10)
driver.get('https://aliexpress.ru/')

for i in range(5):
    goods = driver.find_elements(By.XPATH, "//div[@data-product-id]")
    actions = ActionChains(driver)
    actions.move_to_element(goods[-1])
    actions.perform()

i = 0
while i < 2:
    wait = WebDriverWait(driver, 10)
    next_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    next_button.click()
    i += 1
    # next_button = driver.find_element(By.TAG_NAME, "button")
    # next_button.click()

    # time.sleep(1)

goods = driver.find_elements(By.XPATH, "//div[@data-product-id]")

for good in goods:
    name = good.find_element(By.XPATH, ".//div[@class='product-snippet_ProductSnippet__name__lido9p']").text
    price = good.find_element(By.XPATH, ".//div[@class='snow-price_SnowPrice__mainM__18x8np']").text
    print(name, price)
