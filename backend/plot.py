import pandas as pd
import matplotlib.pyplot as plt

# Read data from the HTML file
df = pd.read_html('F1/Merged.html')[0]  # Assuming the data is in the first table of the HTML file

# Plotting and saving HTML files for each company
companies = ['Pepsi', 'Coca Cola', 'Nike']

for company in companies:
    plt.figure(figsize=(8, 6))
    plt.plot(df['Year'], df[company], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Return on Equity')
    plt.title(f'{company} Return on Equity')
    plt.grid(True)
    
    # Save the plot as HTML in the Display folder
    html_file_path = f'backend/Display/{company}_plot.jpeg'
    plt.savefig(html_file_path)
    plt.close()

print(f'Plots saved as HTML files in the Display folder.')
