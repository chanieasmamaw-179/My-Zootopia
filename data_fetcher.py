import requests

API_KEY = 'VvdZk/eLNcUMI2W/Zp5sZg==txiiFyuEGIse97vq'  # Replace with your actual API key

def fetch_animal_data(animal_name=''):
    """Fetches animal data from the API."""
    if animal_name:
        url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    else:
        url = 'https://api.api-ninjas.com/v1/animals'

    headers = {
        'X-Api-Key': API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        print("Error details:", response.json())
        return None

    data = response.json()
    if animal_name and not data:  # Check if data is empty for a specific animal name
        return {'error': f'The animal "{animal_name}" doesn\'t exist.'}

    return data
