import json
animals_web_generator.py

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_animal_html(animal):
    """Generates HTML for an animal."""
    name = animal['name']
    diet = animal['characteristics'].get('diet', 'Unknown')
    location = ', '.join(animal.get('locations', []))
    animal_type = animal['characteristics'].get('type', 'Unknown')
    skin_type = animal['characteristics'].get('skin_type', 'Unknown')  # Added skin_type

    html = f"""
    <li class="cards__item">
        <div class="animal-info">
            <h2 class="card__title">{name}</h2>
            <p class="card__text"><strong>Diet:</strong> {diet}</p>
            <p class="card__text"><strong>Location:</strong> {location}</p>
            <p class="card__text"><strong>Type:</strong> {animal_type}</p>
            <p class="card__text"><strong>Skin Type:</strong> {skin_type}</p>  <!-- Display skin_type -->
        </div>
    </li>
    """
    return html


def get_unique_skin_types(animals_data):
    """Extracts unique skin types from the data."""
    skin_types = set(animal['characteristics'].get('skin_type', 'Unknown') for animal in animals_data)
    return sorted(skin_types)


def main():
    # Load the JSON data
    animals_data = load_data("animals_data.json")

    # Get and display the unique skin types
    skin_types = get_unique_skin_types(animals_data)
    print("Available skin types:")
    for i, skin_type in enumerate(skin_types, 1):
        print(f"{i}. {skin_type}")

    # Prompt user to select a skin type
    while True:
        try:
            choice = int(input(f"Enter the number corresponding to your chosen skin type (1-{len(skin_types)}): "))
            if 1 <= choice <= len(skin_types):
                selected_skin_type = skin_types[choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Filter animals by the selected skin type
    filtered_animals = [animal for animal in animals_data if
                        animal['characteristics'].get('skin_type') == selected_skin_type]

    # Generate the HTML for the filtered animals
    all_animals_html = "".join(generate_animal_html(animal) for animal in filtered_animals)

    # HTML template
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

    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", all_animals_html)

    # Save the resulting HTML to a file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)


if __name__ == "__main__":
    main()
