import sys
import sqlite3
from pathlib import Path

# Set the correct path to locate app.py and models.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the app and db from app.py, and the Note model from models.py
from app import app, db
from models import Note  # Import the Note model from models.py

def drop_table(db_path, table_name):
    """Drop the specified table from the SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()
    conn.close()
    print(f"Table '{table_name}' dropped.")

def recreate_table():
    """Recreate the notes table using SQLAlchemy."""
    with app.app_context():
        db.create_all()  # This will create all tables defined in the models if they don't exist
    print("Recreated all tables.")

def main():
    """Main function to drop and recreate the notes table."""
    db_path = "C:/Projects/GitHub/PoGO/pogo.db"
    table_name = "notes"

    # Drop the notes table
    drop_table(db_path, table_name)

    # Recreate the notes table
    recreate_table()

if __name__ == "__main__":
    main()