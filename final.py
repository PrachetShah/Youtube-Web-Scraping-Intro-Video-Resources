# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Step 1: Make a Request to the Website
url = 'https://www.timeanddate.com/weather/'  # Replace with the URL of the website you want to scrape
response = requests.get(url)
print(response.text)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(f"Successfully connected to {url}")
else:
    print(f"Failed to connect to {url}. Status code: {response.status_code}")
    exit()


# Step 2: Create a BeautifulSoup Object
soup = BeautifulSoup(response.text, 'html.parser')


# Step 3: Explore HTML Structure and Find Elements
# Example 1: Extracting and printing the title of the webpage
title_element = soup.title
print(f'Title of the webpage: {title_element.text}')


# Example 2: Extracting and printing all the links on the webpage
all_links = soup.find_all('a')
print('\nAll links on the webpage:')
for link in all_links:
    print(link.get('href'))


# Example 3: Extracting and printing all text from paragraphs
all_paragraphs = soup.find_all('p')
print('\nAll text from paragraphs:')
for paragraph in all_paragraphs:
    print(paragraph.text)


# Example 4: Extracting data using CSS selectors
css_selector_example = soup.select_one('.my-city__temp')  # Selects the first element with class 'my-city__temp'
if css_selector_example:
    print(f'\nData from CSS selector example: {css_selector_example.text}')
else:
    print('\nCSS selector example not found.')


# Step 4: Extracting Specific Data
# Example 5: Scraping data from a specific element with an ID
example_with_id = soup.find('ul', id='site-nav')
if example_with_id:
    print(f'\nData from the example with ID: {example_with_id.text}')
else:
    print('\nExample with ID not found.')


# Example 6: Extracting data using regular expressions
import re
pattern = re.compile(r'my-city__temp')
regex_example = soup.find_all('span', class_=pattern)
print('\nData from elements matching the regular expression:')
for element in regex_example:
    print(element.text)



# Step 4: Handling Dynamic Content (We can set project to scrape every 10 minutes or so)
# Note: For dynamic content, you may need to use tools like Selenium.

# Step 6: Best Practices and Ethics
# Emphasize ethical scraping practices, respect website terms of service, etc.

# Step 7: Save Scraped Data (Optional)
# You can save the scraped data to a file or database.

# Conclusion
print('\nWeb scraping with BeautifulSoup tutorial completed.')

# Additional Resources
# Provide links to documentation, tutorials, and further learning resources.