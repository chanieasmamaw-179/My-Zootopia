Zootopia App - Animal Information Repository
1. Introduction

Zootopia is an "Animal Information Repository" that generates a static website displaying animal information. The app automatically creates the website using data retrieved from a JSON file with the help of an API. Specifically, it utilizes the "Animals API" from the API Ninja website. The back-end Python code fetches JSON data from the API and generates the Zootopia app.
2. Features

    Fetches animal data from an external API.
    Provides a fallback to local JSON data if the API request fails.
    Allows users to search for a specific animal by name or view all available animals.
    Generates an HTML file displaying the animal information in a visually appealing format.

3. Usage and Prerequisites
3.1. Usage

    Run the application:

    bash

    python main.py

    Enter the name of an animal:
        You will be prompted to enter the name of an animal. You can leave the input blank to fetch data for all available animals.

    View the generated HTML file:
        After running the script, an animals.html file will be generated in the project directory. Open this file in a web browser to view the information about the animals.

3.2. Prerequisites

Before running this project, ensure you have the following installed:

    Python 3.x
    pip (Python package installer)

4. Project Structure

bash

animal-info-repository/
│
├── data_fetcher.py            # Contains the logic to fetch data from the API
├── animals_data.json          # Local JSON file with fallback animal data
├── main.py                    # Main script that runs the application
├── .env                       # Environment variables file (not included in the repo)
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies file
└── animals.html               # Generated HTML file with animal information

5. Contact

For any questions or inquiries, please contact Asmamaw Yehun at chanieasmamaw@yahoo.com.