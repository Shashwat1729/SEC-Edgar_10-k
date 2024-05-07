


# SEC-Edgar_10-k

## Project Overview

This repository encompasses the code and resources for the Financial Services Innovation Lab's Summer Research Programming Task. The project integrates a website app developed using HTML, CSS, and JavaScript, data collection from SEC-EDGAR for Coca-Cola, PepsiCo, and Nike using the sec-edgar-downloader, text analysis utilizing the Gemini API, and insight generation focusing on Return on Common Equity (ROE).


## Data Collection

The script download_filings.py automates the download of 10-K filings from SEC-EDGAR for Coca-Cola (KO), PepsiCo (PEP), and Nike (NKE) for the last 29 years. During this process, several measures were taken to ensure data accuracy and reliability:

- Error Handling: While reading HTML files into text, occasional errors were encountered. Robust error handling mechanisms were implemented to address these issues and ensure smooth data processing.
Data Cleaning: Irregularities were observed in the formatting of data across different companies but within the same year. To maintain consistency, data was transformed into a standardized format, enhancing the quality and uniformity of the dataset.
- Selective Data Extraction: To focus on relevant information, keywords were strategically used to selectively extract data pertinent to the analysis. This approach streamlined the dataset and facilitated subsequent analysis steps.

```python
from sec_edgar_downloader import Downloader

dl = Downloader("TEST", "email@example.com", "./Data/")

def download_latest_10k_filings(companies, num_filings=29):
    # Download latest 10-K filings for specified companies
    for company in companies:
        try:
            dl.get("10-K", company, limit=num_filings, download_details=False)
            print(f"Downloaded {num_filings} latest 10-K filings for {company}")
        except Exception as e:
            print(f"Error downloading {company} filings: {str(e)}")

# Usage
companies = ["KO", "PEP", "NKE"]
download_latest_10k_filings(companies)
```

## Text Analysis

Text analysis using Gemini API focused on generating insights on Return on Common Equity (ROE) for the selected companies. Gemini API was chosen due to token constraints with other LLMs like Mistral. ROE was selected for analysis as it provides valuable information about a company's profitability and efficiency, making it a key metric for financial analysis.

- API Approach: In addition to analyzing overall ROE trends, specific items such as Item 7 of the 10-K filings were considered using the SEC API. This allowed for a deeper exploration of key financial indicators beyond ROE. This was used and code was written but this was not used in the end
- Insight Interpretation: Generated insights were meticulously interpreted to provide meaningful and actionable information for financial analysis and decision-making. (Mainly Mistral part app.ipynb file)

```python
import google.generativeai as genai

genai.configure(api_key="API_KEY")

model = genai.GenerativeModel('gemini-1.0-pro-001')

prompt = """
Based on the following data on What individual Insight can you give for each company- Return on Common Equity
Year Pepsi Coca Cola Nike
1996 0.72 0.69 0.24
1997 1.36 0.82 0.2
...
2022 5.49 2.19 3.75
2023 6.5 2.47 3.23"""

response = model.generate_content(prompt)
```

## App Development

A basic web app was developed using HTML, CSS, and JavaScript to visualize insights generated from the ROE analysis. React was considered for future enhancements.
This web app shows the plot and finacial insight given by the LLM on these companies

## Additional Notes

- **Deployment:** You can view current outputs on this website - https://shashwat1729.github.io/SEC-Edgar_10-k/backend/templates/ticker_data.html , can also execute the HTML file locally to view results.
- **Insight Focus:** ROE was chosen for analysis due to its significance in evaluating a company's profitability and efficiency. (Du Pont was considered but due to variable mismatch across years ROE was selected in the end)
- **Gemini Models:** Various Gemini models were explored for text generation and insights and finally 'gemini-1.0-pro-001' was considered. Mistral and other models were also considered and there code is also there but for the time being Gemini seemed more feasible
```
