from sec_edgar_downloader import Downloader

# Initialize a downloader instance with company name, email, and download location
dl = Downloader("TEST", "shashwatbajpai1729@gmail.com", "./Data1/")

def download_latest_10k_filings(companies, num_filings=29):
    """
    Download the latest 10-K filings for specified companies from SEC website.
    
    Parameters:
    companies (list): List of company tickers (e.g., ["KO", "PEP", "NKE"])
    num_filings (int): Number of latest filings to download (default is 29)
    """
    for company in companies:
        try:
            dl.get("10-K", company, limit=num_filings, download_details=False)
            print(f"Downloaded {num_filings} latest 10-K filings for {company}")
        except Exception as e:
            print(f"Error downloading {company} filings: {str(e)}")

# Usage with Coca-Cola - KO, PepsiCo - PEP, and Nike - NKE as companies
companies = ["KO", "PEP", "NKE"]
download_latest_10k_filings(companies)
