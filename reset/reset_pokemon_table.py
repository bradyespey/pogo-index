import sys
import sqlite3
from pathlib import Path

# Set up the correct path for app.py and models.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app, db  # Import the app and db directly from app.py

def drop_pokemon_table(db_path):
    """Drop the Pokémon table from the SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS pokemon;")
    conn.commit()
    conn.close()
    print("Table 'pokemon' dropped.")

def recreate_pokemon_table():
    """Recreate the Pokémon table in the database using SQLAlchemy."""
    with app.app_context():
        db.create_all()  # Recreate all tables, including the updated 'pokemon' table
    print("Recreated the Pokémon table.")

def main():
    db_path = "C:/Projects/GitHub/PoGO/pogo.db"

    # Drop the existing Pokémon table
    drop_pokemon_table(db_path)

    # Recreate the Pokémon table with the new fields
    recreate_pokemon_table()

if __name__ == "__main__":
    main()
