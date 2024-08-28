import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


# Load the JSON data
animals_data = load_data('animals_data.json')

# Print each animal's details
for animal in animals_data:
    name = animal['name']
    diet = animal['characteristics'].get('diet', 'Unknown')
    location = ', '.join(animal.get('locations', []))
    animal_type = animal['characteristics'].get('type', 'Unknown')
    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Location: {location}")
    print(f"Type: {animal_type}")
