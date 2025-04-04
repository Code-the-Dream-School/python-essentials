
# **Lesson 09 — Introduction to Web Scraping**

## **Lesson Overview**
**Learning objective:** In this lesson, students will gain a comprehensive understanding of web scraping, focusing on the fundamentals such as HTML structure, DOM representation, and using Python libraries like `BeautifulSoup` and `Requests` to scrape and extract data from web pages. Additionally, students will explore the ethical aspects of web scraping, including adhering to guidelines provided by `robots.txt` and managing server requests responsibly.

### **Topics:**
1. Basics of HTML and DOM
2. Web Scraping Tools: `Requests` and `BeautifulSoup`
3. Ethical Web Scraping: Understanding `robots.txt` and ethical considerations
4. Scraping Structured Data: Extracting specific data points
5. Managing Requests: Delays, retries, and handling errors
6. Saving Scraped Data to Files
7. Frailty in Scraping Programs

**Why Do Web Scraping?**

There is a lot of information on the Internet, as you know, but it is in web pages that are provided so that humans can read them.  If you want to automate the process of searching or archiving some of this information, you need to extract it into a structured format and store it separately, so that you can then do SQL searches or the like on what you save.

Here are some examples:

- Finding the prices of airline flights to a given destination for multiple airlines.
- Finding all scholarly articles on a particular topic you want to research and saving this information for reference.
- Finding the schedule of public meetings for local government bodies.

---

## **9.1 Basics of HTML and DOM**

### **Overview**
HTML (Hypertext Markup Language) is the backbone of web pages, providing structure and content. The Document Object Model (DOM) is a tree structure that represents the page content. Understanding the structure of web pages and the DOM is essential for locating and extracting data during web scraping.  When you pull up a web page in your browser, a request is sent to a web server and an HTML document is returned.  Your browser then parses that document and presents the page.  When you do web scraping, you'll also parse that page, not for presentation, but to capture information from that page so that it can be stored in a structured way.  You need to understand HTML and the DOM structure to do screen scraping.  Many of you may already be familiar with HTML -- if so, skip ahead.

### Elements of an HTML Document

Each element of the DOM has the following:
- A tag, the name for the type of element.
- Attributes.  These are name-value pairs, and vary with the element type.  For example, a `class` attribute might describe the display style for the element.  For a link element, the `href` attribute describes web address to use for the link.  There are many others.
- Content.  This may be text, or it may be other elements.  As the DOM is a tree, some elements contain others.

### **Key HTML Elements:**
- **`<title>`**: The title of the page.
- **`<p>`**: Paragraphs of text.
- **`<h1>, <h2>, <h3>`**: Headers of varying levels.
- **`<a>`**: Links with `href` attributes pointing to URLs.
- **`<img>`**: Images with `src` attributes indicating the image source.

There are many others.

### For Further Reference

A good online refernce to HTML is available at [W3Schools](https://www.w3schools.com/html/).

### **Hands-On Activity:**

1. Open the Wikipedia page for "Web Scraping" ([Wikipedia - Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)).
2. Open the developer tools for your browser.  For Chrome this is `Shift-Ctrl-J`.  Inspect the elements of the page.  In the Chrome developer tools, they are in the `Elements` tab. 
3. Traverse this collection of elements to:
   - Identify the title of the page.
   - Locate the first paragraph and examine its structure.
   - Explore headers (`<h1>, <h2>, <h3>`) and links (`<a>`).

When you are creating a web scraping program, this is often the first step.  Look at the page you want to scrape in the browser developer tools and find where the information you want resides within the DOM, so that you can write code to extract it.

### **How the DOM Is Structured:**
The DOM is a hierarchical tree structure. Here's an example:
```html
<html>
  <head>
    <title>Web Scraping</title>
  </head>
  <body>
    <h1>Introduction</h1>
    <p>This is an example paragraph.</p>
    <a href="https://example.com">Example Link</a>
  </body>
</html>
```

---

## **9.2 Web Scraping Tools: Requests and BeautifulSoup**

### **Overview and Setup**

To scrape data from a web page, two primary libraries are commonly used in Python:
- **`Requests`**: A library for sending HTTP requests and fetching web pages.
- **`BeautifulSoup`**: A library for parsing HTML and extracting elements from the parsed content.

You need to install these into your python_homework directory.  Within your VSCode terminal session for `python_homework` do:

```bash
pip install bs4
pip install requests
```

### **Steps to Web Scraping:**
1. Send an HTTP GET request using `Requests`.
2. Parse the HTML content using `BeautifulSoup`.
3. Extract the desired elements using tags, attributes, or CSS selectors.

BeautifulSoup parses the HTML document into a BeautifulSoup object, which contains a collection of Tag and NavigableString objects in a tree.  You can see a full description at the [documentation page](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and it's a good idea to have a look.  The BeautifulSoup object and the Tag objects it contains can be starting points for a search of the whole tree or the part of the tree that is under that tag.  The NavigableString object and the Tag objects each have `.string` attributes (here meaning attributes of those classes), which is the text content of those HTML elements.  Each may have HTML attributes as well (here meaning the attributes of the HTML element, not the attributes of the NavigableString or Tag classes).  If `tag` is the variable name for a tag, `tag.attrs` is a dictionary of attributes (and the same goes for NavigableString.)  The word `attributes` is overloaded here.

The Tag object has `.contents`, which is a list of what it contains, possibly other Tag or NavigableString objects.  The Tag and BeautifulSoup objects have a `.find_all()` method, that finds the matching elements underneath that point in the tree.  You don't have these for NavigableString objects.  Both Tag and Bea

In extracting information from the parsed tree, you need to find the elements you care about, and get the corresponding data from each.  You do a search.  You can search by the HTML element tag name, the value of an HTML element attribute, a CSS selector, or using a function.  Searching via CSS selectors is complicated, so we won't explain that here, but if you are familiar with CSS, you can reuse the ideas of CSS selectors.

Here are some examples.  You don't need to run these.  Note the shortcuts.

```python
# Assume the BeautifulSoup object is stored in the variable soup'
soup_title_list = soup.find_all('title') # gets all the title elements in the HTML (there will only be one for a typical document)
soup_title = soup.find('title') # gets the first title element (if any)
soup_title = soup.title # a shortcut for soup.find('title') -- can throw an exception!
print(soup_title.get_text()) # the text content of the title.  Just a str object.
print(soup_title.string) # the NavigableString in the title.  Not quite the same as get_text().
soup_main = soup.find(id='main') # find the first HTML element with id="main", which might be, for example, a div.
soup_items = soup_main.find_all('li') # find all li elements within main -- might throw an exception if main wasn't found.
soup_items = soup_main.find_all('li', class_='SalesItem') # a multipart search.  Finds all li elements within main that have this value for the class attribute
# Note that we use class_ instead of class, as the latter is a reserved word in Python
soup_link = soup_main.a # shortcut: finds the first link within main -- can throw an exception!
soup_links = soup_main('a') # shortcut: finds all the links within main
link_target = soup_link['href'] # finds the target of the link, the value of the href attribute for the link
link_classes = soup_link['class'] # because class is a multivalued HTML attribute, finds the list of classes for the link entry

def paragraph_contains_elephant(tag):
    return tag.name=='p' and 'elephant' in tag.get_text()

paragraphs_with_elephant = main.find_all(paragraph_contains_elephant) # here the function above is called for each descendant of main
```
Note that some of the examples above may throw exceptions, typically `AttributeError` exceptions.  So, you should typically do each operation in a try block.

The examples below show how to do the search and how to extract information.  As usual, you should run these within the Python interactive shell in your `python_homework` terminal session.

### **Example Code: Extracting Page Title**
```python
import requests
from bs4 import BeautifulSoup

# Fetch the web page
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract and print the page title
title = soup.title.string
print(f"Page Title: {title}")
```

---

## **9.3 Extracting Specific Data**

### **Task: Extract All Bold Text and Images**
With `BeautifulSoup`, we can use methods like `find_all()` to locate and extract specific HTML elements.

### **Example Code: Extracting Bold Text and Images**
```python
# Extract all bold text
bold_texts = [tag.get_text() for tag in soup.find_all('b')]
print("Bold Texts:", bold_texts)

# Extract all images with their src attributes
images = [(img['src']) for img in soup.find_all('img') if 'src' in img.attrs] 
print("Image Sources:", images)
# hmm, this example uses a list comprehension.  We haven't talked about those.  This is the same as:
image_entries = soup.find_all('img', attrs = {'src': True})
images = []
for img in image_entries:
    images.append(img['src'])

print("Image Sources:", images)
# You can see that list comprehensions are a useful shortcut in Python!
```

---

## **9.4 Ethical Web Scraping**

### **Overview**
While web scraping can be a powerful tool, it is important to follow ethical guidelines and respect website owners’ wishes to avoid excessive server load and legal issues.

### **Key Concepts:**
- **What is `robots.txt`?**
  - A file that specifies which sections of a website can or cannot be accessed by web crawlers.
- **Why is `robots.txt` important?**
  - It helps website owners control the traffic to their site and avoid server overload.
  - Ethical scraping involves reviewing and adhering to the rules set in `robots.txt`.

### **Activity: Explore `robots.txt` for Wikipedia**
1. Access the `robots.txt` file for Wikipedia: [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt).
2. Identify restricted sections of the site.
3. Discuss why these sections are restricted.

### **Example Code: Accessing `robots.txt`**
```python
robots_url = "https://en.wikipedia.org/robots.txt"
robots_response = requests.get(robots_url)
print(robots_response.text)
```

---

## **9.5 Scraping Additional Data**

### **Overview**
After scraping basic data, you can refine your scraping strategy to focus on specific sections of a webpage.

### **Example Task: Scrape the "See also" Section**
```python
# Find the "See also" section
see_also_section = soup.find('span', id="See_also")
if see_also_section:
    see_also_list = see_also_section.find_next('ul')
    links = [a.get_text() for a in see_also_list.find_all('a')]
    print("See Also Links:", links)
else:
    print("No 'See also' section found.")
```

### **Testing on Another Page:**
Test the script on different Wikipedia pages to ensure consistency and robustness.

---

## **9.6 Managing Requests and Handling Errors**

### **Overview**
When scraping large numbers of web pages, managing requests responsibly is essential. Techniques include delaying requests, retrying failed requests, and handling connection errors.

### **Key Techniques:**
1. **Delaying Requests**: Introduce time delays between requests to avoid overloading the server.
   ```python
   import time
   time.sleep(2)  # Delay for 2 seconds
   ```
2. **Retrying Requests**: Use retry logic for handling failed requests.
   ```python
   import requests
   from time import sleep

   def fetch_page(url, retries=3):
       for i in range(retries):
           try:
               response = requests.get(url)
               if response.status_code == 200:
                   return response
           except requests.RequestException as e:
               print(f"Error fetching {url}: {e}")
               sleep(2)  # Wait before retrying
       return None
   ```

### **Handling Errors:**
Use `try-except` blocks to handle potential errors, such as timeouts or missing elements.
```python
try:
    element = soup.find('div', class_='nonexistent')
    print(element.get_text())
except AttributeError:
    print("Element not found!")
```

---

## **9.7 Saving Scraped Data**

### **Overview**
Once you've scraped valuable data, you may want to save it in a structured format, such as CSV or JSON.

### **Saving Data to CSV:**
```python
import csv

# Save extracted data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Link"])
    for link in links:
        writer.writerow([link])
```

### **Saving Data to JSON:**
```python
import json

# Save data to a JSON file
data = {"links": links}
with open('scraped_data.json', 'w') as json_file:
    json.dump(data, json_file)
```

### **Saving Data to an SQL Database**

Suppose you are scraping from multiple sites.  You may want to record different information from each site, and keep track of which site provided which information.  

For example, you may scrape airline sites for destinations, prices, and departure times.  You could create three tables, one for airlines, which would record the airline name and URL, and then three others for destinations, prices, and departure_times.  There would be a many-to-many relationship between airlines and destinations, which might have where_we_fly as a join table.  There would be a one-to-many relationship between where_we_fly entries and prices, and between where_we_fly and departure_times.  This is a little more complicated, to be sure -- but think about your data model when you get ready to store web scraping data!

## **9.8 Frailty in Web Scraping**

Web scraping programs can be frail.  The authors of the websites that you are accessing to scrape data can change the format of the page.  This can break the scraping logic, as the logic you use to traverse the DOM may no longer work.  Sometimes you can make your scraping more robust by finding known strings within the formatted page, and traversing from that point, but sometimes you can only log the error so as to trigger work on a fix.

---

## **Summary**

In this lesson, you learned:
1. How to understand the structure of web pages using HTML and the DOM.
2. How to use Python libraries `Requests` and `BeautifulSoup` for web scraping.
3. Ethical considerations of web scraping, including respecting `robots.txt`.
4. Techniques for extracting specific data, handling errors, and managing requests.
5. How to save scraped data to CSV and JSON formats for future use.

### **Important Notes:**
- Always respect the website’s `robots.txt` file and terms of service.
- Avoid overloading a server with excessive scraping requests.
- Use appropriate delay and retry mechanisms to manage web traffic.

For further learning, explore the [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and the [Requests Library Documentation](https://docs.python-requests.org/).

