import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def extract_return_on_equity_with_inspect(html_file, inspect_addresses, keyword="Return on Equity", delay=15):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Load the HTML file in the browser
    driver.get(html_file)

    # Wait for the content to load (adjust wait time as needed)
    time.sleep(delay)

    # Click on the first inspect address and wait
    first_address = inspect_addresses[0]
    driver.find_element_by_xpath(first_address).click()
    time.sleep(5)  # Wait for 5 seconds after clicking the first element

    # Click on the second inspect address and wait
    second_address = inspect_addresses[1]
    driver.find_element_by_xpath(second_address).click()
    time.sleep(1)  # Wait for 1 second after clicking the second element

    # Start searching for the keyword from the visible screen
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'f')
    time.sleep(1)  # Wait for the Find dialog to open
    driver.switch_to.active_element.send_keys(keyword)
    time.sleep(1)  # Wait for the search to complete

    # Get the text of the found element
    roe_element = driver.find_element_by_xpath('//body')
    roe_value = roe_element.text.strip()

    # Close the browser
    driver.quit()

    return roe_value

# Example usage with specified file address and inspect addresses
html_file_address = "file:///D:/Downloads/BITS/Georgia%20Tech/Data/sec-edgar-filings/NKE/10-K/0000320187-14-000097/full-submission.html"
inspect_addresses = [
    "/html/body/sec-document/document[1]/type/sequence/filename/description/text/div[1]/div/a/font",
    "/html/body/sec-document/document[1]/type/sequence/filename/description/text/div[29]/div/table/tbody/tr[29]/td[2]/div/a/font"
]
roe_value = extract_return_on_equity_with_inspect(html_file_address, inspect_addresses)
if roe_value:
    print("Return on Equity value:", roe_value)
else:
    print("Return on Equity value not found or data extraction failed.")
