


# SEC-Edgar_10-k

## Project Overview

This repository contains code and resources for the Financial Services Innovation Lab's Summer Research Programming Task. The project includes a website app developed using HTML, CSS, and JavaScript, data collection from SEC-EDGAR for Coca-Cola, PepsiCo, and Nike using sec-edgar-downloader, text analysis using Gemini API, and insight generation on Return on Common Equity (ROE).

## Tech Stack

- Website making
- Python (sec-edgar-downloader)
- Gemini API
- Google Generative AI (Gemini models)

## Data Collection

The script `download_filings.py` automates the download of 10-K filings from SEC-EDGAR for Coca-Cola (KO), PepsiCo (PEP), and Nike (NKE) for the last 29 years.

```python
from sec_edgar_downloader import Downloader

dl = Downloader("TEST", "email@example.com", "./Data1/")

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

## Additional Notes

- **Deployment:** No deployed version; execute the HTML file locally to view results.
- **Insight Focus:** ROE was chosen for analysis due to its significance in evaluating a company's profitability and efficiency. (Du Pont was considered but due to variable mismatch across years ROE was selected in the end)
- **Gemini Models:** Various Gemini models were explored for text generation and insights and finally 'gemini-1.0-pro-001' was considered. Mistral and other models were also considered and there code is also there but for the time being Gemini seemed more feasible
```
