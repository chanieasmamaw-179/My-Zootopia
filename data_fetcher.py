import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('API_KEY')

print(f"API Key Retrieved: {api_key}")  # For debugging purposes; remove in production

if not api_key:
    print("API key is missing. Please check your .env file.")

def fetch_animal_data(animal_name=''):
    """Fetch animal data from the API."""
    if not api_key:
        return None

    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}' if animal_name else 'https://api.api-ninjas.com/v1/animals'
    headers = {'X-Api-Key': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        print("Error details:", response.json())
        return None
