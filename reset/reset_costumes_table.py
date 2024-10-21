import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def drop_table():
    """Drop the 'costumes' table if it exists."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS costumes;")
    conn.commit()
    conn.close()
    print("Table 'costumes' dropped.")

def create_table():
    """Create the 'costumes' table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE costumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dex_number INTEGER,
            name TEXT NOT NULL,
            costume TEXT,
            first_appearance TEXT
        );
    ''')

    conn.commit()
    conn.close()
    print("Table 'costumes' created.")

def main():
    drop_table()
    create_table()

if __name__ == "__main__":
    main()
