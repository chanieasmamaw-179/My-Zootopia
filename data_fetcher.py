import requests

API_KEY = 'VvdZk/eLNcUMI2W/Zp5sZg==txiiFyuEGIse97vq'  # Replace with your actual API key

def fetch_animal_data(animal_name=''):
    """Fetches animal data from the API.

    Args:
        animal_name (str): The name of the animal to fetch. Leave empty to fetch all animals.

    Returns:
        dict or None: The JSON response from the API or None if an error occurred.
    """
    # Construct the URL for the API request
    if animal_name:
        url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    else:
        url = 'https://api.api-ninjas.com/v1/animals'

    # Set up the headers with the API key
    headers = {
        'X-Api-Key': API_KEY
    }

    # Send the GET request to the API with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        print("Error details:", response.json())
        return None

    # Parse and return the JSON response
    return response.json()
