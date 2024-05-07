import os
from bs4 import BeautifulSoup

# Define the parent directory containing the "Data" folder
parent_directory = "Data"

# Define the companies for conversion
companies = ['KO', 'PEP', 'NKE']

for company in companies:
    company_path = os.path.join(parent_directory, "sec-edgar-filings", company, "10-K")
    for root, dirs, files in os.walk(company_path):
        for filename in files:
            if filename.endswith(".html"):  # Check for HTML files
                html_file = os.path.join(root, filename)
                txt_file = os.path.splitext(html_file)[0] + ".txt"
                with open(html_file, 'r', encoding='utf-8') as html_content_file:
                    html_content = html_content_file.read()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    text_content = soup.get_text()  # Extract text content from HTML
                    with open(txt_file, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(text_content)
                os.remove(html_file)  # Remove the original HTML file after conversion
