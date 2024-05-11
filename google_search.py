# not working yet

from googlesearch import search
import pandas as pd

def extract_redirect_urls(query):
    search_results = search(query, num=10, lang="en")
    
    # Collect URLs in a list
    urls = list(search_results)
    
    # Print URLs
    for url in urls:
        print(url)
    
    # Create a DataFrame from the list of URLs
    df = pd.DataFrame({'URLs': urls})
    return df

if __name__ == "__main__":
    file_path = 'google_search.csv'

    while True:
        search_query = input("Enter search query (or 'quit' to exit): ")
        
        if search_query.lower() == 'quit':
            break
        
        search_results_df = extract_redirect_urls(search_query)
        
        # Save the DataFrame to a CSV file
        search_results_df.to_csv(file_path, mode='a', header=False, index=False)
