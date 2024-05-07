import os

# Define the parent directory containing the "Data" folder
parent_directory = "Data"

# Define the companies for conversion
companies = ['KO', 'PEP', 'NKE']

for company in companies:
    company_path = os.path.join(parent_directory, "sec-edgar-filings", company, "10-K")
    for root, dirs, files in os.walk(company_path):
        for filename in files:
            if filename.endswith(".txt"):
                txt_file = os.path.join(root, filename)
                html_file = os.path.splitext(txt_file)[0] + ".html"
                if not os.path.exists(html_file):  # Check if HTML file doesn't exist
                    os.rename(txt_file, html_file)
