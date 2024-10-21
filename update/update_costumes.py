import requests
from bs4 import BeautifulSoup
import re
import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def sanitize_string(value):
    """Remove or replace special characters that cause encoding issues."""
    if value:
        return value.encode('ascii', 'ignore').decode()  # Remove non-ASCII characters
    return None

def decode_html(html):
    """Helper function to decode HTML entities like &eacute;."""
    return (html.replace('&amp;', '&')
                .replace('&lt;', '<')
                .replace('&gt;', '>')
                .replace('&quot;', '"')
                .replace('&#39;', "'")
                .replace('&eacute;', 'é')
                .replace('&uacute;', 'ú')
                .replace('&Eacute;', 'É')
                .replace('&Uacute;', 'Ú'))

def extract_costume_data(html):
    """Parse the HTML and extract costume Pokémon data."""
    soup = BeautifulSoup(html, 'html.parser')

    # Find all tables that might contain costume Pokémon data
    tables = soup.find_all('table')

    # Placeholder list for the parsed data (dex_number, name, costume, first appearance)
    costumes_data = []

    # Loop through each table (assuming that costume data is within table rows)
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the first row (header)
            columns = row.find_all('td')

            # Ensure the row has enough columns to be valid
            if len(columns) >= 2:
                name = decode_html(columns[0].get_text(strip=True))
                first_appearance = decode_html(columns[1].get_text(strip=True))

                # Using placeholder dex_number since Eurogamer page doesn’t seem to have dex numbers
                dex_number = None  # You'll need a lookup mechanism to map name -> dex number

                # Match the name with the costume if possible
                costume_type = "Unknown"
                if 'costume' in name.lower():
                    costume_type = 'Costume'
                elif 'flower crown' in name.lower():
                    costume_type = 'Flower Crown'
                elif 'party hat' in name.lower():
                    costume_type = 'Party Hat'

                # Append the parsed data
                costumes_data.append((dex_number, name, costume_type, first_appearance))

    return costumes_data

def fetch_costume_data():
    """Fetch Costume Pokémon data and update the SQLite database."""
    url = "https://www.eurogamer.net/pokemon-go-event-costume-pokemon-party-hat-flower-crown-7002"
    response = requests.get(url)
    html = response.text

    # Extract costume data from the HTML
    costumes_data = extract_costume_data(html)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Counters for summary output
    total_pokemon = 0
    count_inserted = 0
    count_updated = 0

    # Loop through the extracted costume data and insert/update it in the database
    for costume_entry in costumes_data:
        dex_number, name, costume, first_appearance = costume_entry
        total_pokemon += 1

        # Check if the costume Pokémon entry already exists
        cursor.execute("SELECT * FROM costumes WHERE name = ?", (name,))
        existing_entry = cursor.fetchone()

        if existing_entry:
            # Update the existing entry
            cursor.execute('''
                UPDATE costumes
                SET costume = ?, first_appearance = ?
                WHERE name = ?
            ''', (costume, first_appearance, name))
            count_updated += 1
        else:
            # Insert a new entry
            cursor.execute('''
                INSERT INTO costumes (dex_number, name, costume, first_appearance)
                VALUES (?, ?, ?, ?)
            ''', (dex_number, name, costume, first_appearance))
            count_inserted += 1

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Summary output
    print(f"Finished fetching and saving Costume Pokémon data.")
    print(f"Total costume Pokémon processed: {total_pokemon}")
    print(f"Total costume Pokémon added: {count_inserted}")
    print(f"Total costume Pokémon updated: {count_updated}")

if __name__ == "__main__":
    fetch_costume_data()
