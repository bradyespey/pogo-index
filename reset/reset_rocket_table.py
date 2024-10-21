import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def drop_table():
    """Drop the 'rocket' table if it exists."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS rocket;")
    conn.commit()
    conn.close()
    print("Table 'rocket' dropped.")

def create_table():
    """Create the 'rocket' table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'rocket' table with the correct schema
    cursor.execute('''
        CREATE TABLE rocket (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dex_number INTEGER NOT NULL,
            name TEXT NOT NULL,
            method TEXT  -- Make sure the method column is here
        );
    ''')

    conn.commit()
    conn.close()
    print("Table 'rocket' created.")

def main():
    drop_table()  # Optionally drop the table if you want to reset it
    create_table()

if __name__ == "__main__":
    main()
