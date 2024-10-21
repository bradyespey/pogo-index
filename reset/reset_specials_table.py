import os
import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def drop_table():
    """Drop the 'specials' table if it exists."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS specials;")
    conn.commit()
    conn.close()
    print("Table 'specials' dropped.")

def create_table():
    """Create the 'specials' table with dex_number as an integer."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE specials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dex_number INTEGER NOT NULL,
            name TEXT NOT NULL,
            type TEXT
        );
    ''')

    conn.commit()
    conn.close()
    print("Table 'specials' created with dex_number as an integer.")

def main():
    drop_table()
    create_table()

if __name__ == "__main__":
    main()
