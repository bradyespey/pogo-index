import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def drop_table():
    """Drop the 'forms' table if it exists."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS forms;")
    conn.commit()
    conn.close()
    print("Table 'forms' dropped.")

def create_table():
    """Create the 'forms' table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE forms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dex_number INTEGER NOT NULL,
            name TEXT NOT NULL,
            form TEXT
        );
    ''')

    conn.commit()
    conn.close()
    print("Table 'forms' created.")

def main():
    drop_table()
    create_table()

if __name__ == "__main__":
    main()