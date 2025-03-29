# cp-search-result-item li 
# title-content span
# author-link a
# cp-format-info div
# display-info-primary span

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
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    results_list = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
    results = []
    for element in results_list:
        book_dict = {}
        book_title = element.find_element(By.CSS_SELECTOR,'span.title-content')
        if (book_title):
            book_dict['Title'] = book_title.text
        else:
            book_dict['Title'] = 'title not found'
        book_authors = element.find_elements(By.CSS_SELECTOR,'a.author-link')
        if len(book_authors) == 0:
            book_dict['Author'] = 'author not found'
        else:
            author_list=[]
            for author in book_authors:
                author_list.append(author.text)
            book_dict['Author'] = ';'.join(author_list)
        book_dict['Format-Year'] = 'no format-year found'
        book_info_div = element.find_element(By.CSS_SELECTOR,'div.cp-format-info')
        if book_info_div:
            format_year = book_info_div.find_element(By.CSS_SELECTOR,'span.display-info-primary')
            if format_year:
                book_dict['Format-Year'] = format_year.text
        results.append(book_dict)
    df = pd.DataFrame(results)
    print(df)
    df.to_csv('./get_books.csv', sep='|')
    with open('./get_books.json', 'w') as file:
        json.dump(results, file, indent=4)
    
except Exception as e:
    print(f"An exception occurred getting the page: {type(e).__name__} {e}")

finally:
    driver.quit()