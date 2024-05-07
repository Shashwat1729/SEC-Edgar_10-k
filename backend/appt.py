import os
import re

# Function to clean the data
def clean_data(input_data):
    # Remove unwanted characters, tags, etc.
    cleaned_data = re.sub('<.*?>', '', input_data)  # Remove HTML tags
    cleaned_data = re.sub('[^\w\s.]', '', cleaned_data)  # Remove non-alphanumeric characters except spaces and periods
    cleaned_data = re.sub('\s+', ' ', cleaned_data).strip()  # Remove extra spaces and strip whitespace
    return cleaned_data

# Define the parent directory containing the "Data1" folder
parent_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output folder
output_folder = os.path.join(parent_directory, "F2")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the companies and variables needed for analysis
companies = {'KO': ['Year', 'Return on Common Equity'],
             'PEP': ['Year', 'Return on Common Equity'],
             'NKE': ['Year', 'Return on Common Equity']}

def process_company_folder(company_path):
    print(f"Company Path: {company_path}")  # Debugging statement

    data_list = []
    for file_name in os.listdir(company_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(company_path, file_name)
            print(f"File Path: {file_path}")  # Debugging statement
            with open(file_path, 'r') as file:
                data = file.read()
                data_list.append(data)

    return data_list

    # Your code to process the company folder goes here
    # This function should return a list of data to be cleaned and processed

    # For example:
    data_list = []
    for file_name in os.listdir(company_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(company_path, file_name)
            with open(file_path, 'r') as file:
                data = file.read()
                data_list.append(data)

    return data_list

# Process each company folder in the "Data1" directory
for company, variables in companies.items():
    company_path = os.path.join(parent_directory, "Data1", "sec-edgar-filings", company, "10-K")
    data_list = process_company_folder(company_path)  # Assuming you have a function to process the company folder

    # Clean the data
    cleaned_data_list = [clean_data(data) for data in data_list]

    # Generate HTML table for the company
    html_table = generate_html_table(cleaned_data_list, variables)  # Assuming you have a function to generate HTML tables

    # Save the HTML table to a file in the output folder
    html_filename = os.path.join(output_folder, f"{company}_data.html")
    with open(html_filename, "w") as html_file:
        html_file.write(html_table)
