import pandas as pd
import glob

# Get all CSV files in the directory
csv_files = glob.glob("/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv.csv")

# Loop through each CSV file and convert encoding
for file in csv_files:
    # Read the CSV file with the original encoding
    df = pd.read_csv(file, encoding='ISO-8859-1')  # Replace with the correct encoding if different
    
    # Save the CSV file with UTF-8 encoding
    df.to_csv(file, encoding='utf-8', index=False)
    
    print(f"Converted {file} to UTF-8")
