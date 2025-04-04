# h2 id top-10-web-application-security-risks

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

# Configure Chrome to run in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

try:
    driver.get("https://owasp.org/www-project-top-ten/")
    top_10_header = driver.find_element(By.CSS_SELECTOR, 'h2[id="top-10-web-application-security-risks"]')
    if top_10_header:
        unordered_list = top_10_header.find_element(By.XPATH, "following-sibling::ul")
        if unordered_list:
            top_10=unordered_list.find_elements(By.CSS_SELECTOR,'li')
            results = []
            for risk in top_10:
                risk_link = risk.find_element(By.TAG_NAME, 'a')
                if risk_link:
                    risk_dict = {'Name': risk_link.text, 'URL': risk_link.get_attribute('href')}
                    results.append(risk_dict)
            df = pd.DataFrame(results)
            df.to_csv('./owasp_top_10.csv')

except Exception as e:
    print(f"An exception occurred getting the page: {type(e).__name__} {e}")
finally:
    driver.quit()