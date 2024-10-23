import os
import sys
from pathlib import Path
import subprocess

# Add the root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Now we import app and db inside the functions to avoid any circular import issues
def drop_shinies_table():
    """Drop the 'shinies' table from the PostgreSQL database."""
    from app import app, db  # Import app and db locally
    with app.app_context():
        db.drop_all()  # Drop all tables including 'shinies'
        db.session.commit()
        print("Dropped all tables.")

def recreate_shinies_table():
    """Recreate the 'shinies' table using SQLAlchemy."""
    from app import app, db  # Import app and db locally
    with app.app_context():
        db.create_all()  # Recreate all tables, including the updated 'shinies' table
        db.session.commit()
        print("Recreated all tables.")

def run_update_script():
    """Run the update script for the 'shinies' table."""
    try:
        print("Running update_shinies.py script...")
        update_script_path = Path(__file__).resolve().parent / 'update_shinies.py'
        subprocess.run([sys.executable, str(update_script_path)], check=True)
        print("Update script ran successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running the update script: {e}")
        sys.exit(1)

def main():
    # Drop the existing 'shinies' table
    drop_shinies_table()

    # Recreate the 'shinies' table with the new fields
    recreate_shinies_table()

    # Run the update script
    run_update_script()

if __name__ == "__main__":
    main()