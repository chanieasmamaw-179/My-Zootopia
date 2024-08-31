import json
from data_fetcher import fetch_animal_data

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def generate_animal_html(animal):
    """Generates HTML for an animal."""
    name = animal.get('name', 'Unknown')
    diet = animal.get('characteristics', {}).get('diet', 'Unknown')
    location = ', '.join(animal.get('locations', []))
    animal_type = animal.get('characteristics', {}).get('type', 'Unknown')

    html = f"""
    <li class="cards__item">
        <div class="animal-info">
            <h2 class="card__title">{name}</h2>
            <p class="card__text"><strong>Diet:</strong> {diet}</p>
            <p class="card__text"><strong>Location:</strong> {location}</p>
            <p class="card__text"><strong>Type:</strong> {animal_type}</p>
        </div>
    </li>
    """
    return html

def main():
    # Request animal name from user
    animal_name = input("Enter the name of an animal (or leave blank to get all animals): ").strip()

    # Fetch animal data from the API using the function from data_fetcher.py
    animals_data = fetch_animal_data(animal_name)

    # If API data fetching failed, load data from the local file as a fallback
    if animals_data is None:
        animals_data = load_data("animals_data.json")

    # Generate the HTML for all animals
    all_animals_html = "".join(generate_animal_html(animal) for animal in animals_data)

    # HTML template with placeholder for animal information
    html_template = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
            /* Define color variables */
            :root {
                --gray-darker: #444444;
                --gray-dark: #696969;
                --gray: #999999;
                --gray-light: #cccccc;
                --gray-lighter: #ececec;
                --gray-lightest: #f2f2f2;
            }

            html {
                background-color: #ffe9e9;
            }

            h1 {
                text-align: center;
                font-size: 40pt;
                font-weight: normal;
            }

            body {
                font-family: 'Roboto', 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-style: normal;
                font-weight: 400;
                letter-spacing: 0;
                padding: 1rem;
                text-rendering: optimizeLegibility;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
                -moz-font-feature-settings: "liga" on;
                width: 900px;
                margin: auto;
            }

            .cards {
                list-style: none;
                margin: 0;
                padding: 0;
            }

            .cards__item {
                background-color: white;
                border-radius: 0.25rem;
                box-shadow: 0 20px 40px -14px rgba(0, 0, 0, 0.25);
                overflow: hidden;
                padding: 1rem;
                margin: 50px;
            }

            .card__title {
                color: var(--gray-dark);
                font-size: 1.25rem;
                font-weight: 300;
                letter-spacing: 2px;
                text-transform: uppercase;
            }

            .card__text {
                flex: 1 1 auto;
                font-size: 0.95rem;
                line-height: 2;
                margin-bottom: 1.25rem;
            }
            </style>
        </head>
        <body>
            <h1>My Animal Repository</h1>
            <ul class="cards">
                __REPLACE_ANIMALS_INFO__
            </ul>
        </body>
    </html>
    """

    # Replace the placeholder with the generated HTML for all animals
    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", all_animals_html)

    # Save the resulting HTML to a file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)

if __name__ == '__main__':
    main()
