import os
import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def drop_table():
    """Drop the 'shinies' table if it exists."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS shinies;")
    conn.commit()
    conn.close()
    print("Table 'shinies' dropped.")

def create_table():
    """Create the 'shinies' table with dex_number as an integer."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE shinies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dex_number INTEGER NOT NULL,
            name TEXT NOT NULL,
            method TEXT
        );
    ''')

    conn.commit()
    conn.close()
    print("Table 'shinies' created with dex_number as an integer.")

def main():
    drop_table()
    create_table()

if __name__ == "__main__":
    main()
