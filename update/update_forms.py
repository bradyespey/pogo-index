import requests
from bs4 import BeautifulSoup
import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def sanitize_string(value):
    """Remove or replace special characters that cause encoding issues."""
    if value:
        return value.encode('ascii', 'ignore').decode()  # Remove non-ASCII characters
    return None

def fetch_forms_data():
    """Fetch Forms data and update the SQLite database."""
    url = "https://pokemongo.fandom.com/wiki/List_of_Pok%C3%A9mon_with_different_forms"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse data appropriately (you'll need to adjust the logic based on the HTML structure)
    forms_data = []  # List to hold parsed data (dex_number, name, form)

    # Replace the logic below with actual parsing based on the HTML structure of the page
    # forms_data.append((dex_number, name, form))

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for form_entry in forms_data:
        dex_number, name, form = form_entry

        # Check if the form entry already exists
        cursor.execute("SELECT * FROM forms WHERE dex_number = ? AND name = ?", (dex_number, name))
        existing_entry = cursor.fetchone()

        if existing_entry:
            # Update the existing entry
            cursor.execute('''
                UPDATE forms
                SET form = ?
                WHERE dex_number = ? AND name = ?
            ''', (form, dex_number, name))
            print(f"Updated {name} in the database.")
        else:
            # Insert a new entry
            cursor.execute('''
                INSERT INTO forms (dex_number, name, form)
                VALUES (?, ?, ?)
            ''', (dex_number, name, form))
            print(f"Added {name} to the database.")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Finished fetching and saving Forms data.")

if __name__ == "__main__":
    fetch_forms_data()