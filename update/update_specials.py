import os
import requests
import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def fetch_and_update_specials():
    """Fetch special Pokémon data from the URL and update the SQLite database."""
    url = "https://gist.githubusercontent.com/Lusamine/a8604135b89dcfa840c61900c43df569/raw/7cdd446d7d13c9ea8cd385d630b29ceb550a1009/SV%25203.0.1%2520Legendary,%2520Mythical,%2520Sublegendary,%2520Ultra%2520Beast,%2520Paradox%2520Lists"
    response = requests.get(url)
    raw_data = response.text

    # Split the raw data into different categories
    categories = raw_data.split("\n\n")

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear the existing records in the specials table
    cursor.execute("DELETE FROM specials;")
    conn.commit()

    row_count = 0

    for category in categories:
        lines = category.strip().split("\n")
        if not lines:
            continue

        # The first line is the type (e.g., Legendary, Mythical, etc.)
        type_ = lines[0].strip()

        # Rename 'Sublegend' to 'Legendary'
        if type_ == "Sublegend":
            type_ = "Legendary"

        for line in lines[1:]:
            if not line or ":" not in line:
                continue

            # Split the line to get the Pokémon's dex number and name
            number, pokemon_name = line.split(":", 1)
            pokemon_name = pokemon_name.split("--")[0].strip()  # Remove extra details

            # Insert into the specials table
            dex_number = int(number.strip().replace("#", ""))  # Remove '#' and convert to int
            cursor.execute('''
                INSERT INTO specials (dex_number, name, type)
                VALUES (?, ?, ?)
            ''', (dex_number, pokemon_name, type_))

            row_count += 1

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Specials table updated with {row_count} entries, categorized by type.")

if __name__ == "__main__":
    fetch_and_update_specials()
