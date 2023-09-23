import elements
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: WebDriver = webdriver.Chrome()

driver.get('https://gfgpro.com/')

try:

    elements = driver.find_elements(By.CSS_SELECTOR, 'div.not-logged-header.ng-scope')

    print(f"Found {len(elements)} elements with a class 'not-logged-header ng-scope' on the page.")


    for element in elements:
        element_text = element.text
        print(f"Element text: {element_text}")

except Exception as e:
    print("An error occurred while searching for items by class.")
    print(str(e))

finally:

    driver.quit()