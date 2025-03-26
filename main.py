import requests
import pandas as pd

# 1. Fetch data from MuseScore API (assuming a public API endpoint for fetching scores)
def fetch_musescore_data():
    url = "https://api.musescore.org/v1/scores"  # Modify this with the actual API URL if necessary
    
    # Send GET request to fetch data
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # This will convert the response to a Python dictionary
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# 2. Process and clean the data (for example, extracting relevant score details)
def process_musescore_data(data):
    # Convert the data into a pandas DataFrame (assuming data is a list of scores)
    df = pd.DataFrame(data)
    
    # Extract relevant columns (example: title, author, genre)
    # You can modify these fields based on the API response format
    cleaned_data = df[['title', 'author', 'genre']]  # Adjust these based on actual available fields
    
    # Clean up text (e.g., remove extra spaces from titles)
    cleaned_data['title'] = cleaned_data['title'].str.strip()
    cleaned_data['author'] = cleaned_data['author'].str.strip()
    
    return cleaned_data

# 3. Save the cleaned data to a CSV file
def save_data_to_csv(data, filename):
    data.to_csv(filename, index=False)
    print(f"Cleaned data saved to {filename}")

# Example usage
if __name__ == "__main__":
    # Fetch data from MuseScore API
    musescore_data = fetch_musescore_data()
    
    if musescore_data:
        # Process the data
        cleaned_data = process_musescore_data(musescore_data)
        
        # Save to CSV
        save_data_to_csv(cleaned_data, 'musescore_scores.csv')
