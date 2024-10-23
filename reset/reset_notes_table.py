import os
import sys
from pathlib import Path
import subprocess

# Add the root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Now we import app and db inside the functions to avoid any circular import issues
def drop_notes_table():
    """Drop the 'notes' table from the PostgreSQL database."""
    from app import app, db  # Import app and db locally
    with app.app_context():
        db.drop_all()  # Drop all tables including 'notes'
        db.session.commit()
        print("Dropped all tables.")

def recreate_notes_table():
    """Recreate the 'notes' table using SQLAlchemy."""
    from app import app, db  # Import app and db locally
    with app.app_context():
        db.create_all()  # Recreate all tables, including the updated 'notes' table
        db.session.commit()
        print("Recreated all tables.")

def run_flask_migrations():
    """Run the Flask migration commands."""
    try:
        project_root = Path(__file__).resolve().parent.parent  # Set project root directory
        os.chdir(project_root)  # Change to the project directory

        # Ensure FLASK_APP environment variable is set
        os.environ['FLASK_APP'] = "app.py"

        print("Running flask db migrate...")
        subprocess.run(["flask", "db", "migrate"], check=True)
        print("Running flask db upgrade...")
        subprocess.run(["flask", "db", "upgrade"], check=True)
        print("Flask migrations applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during migrations: {e}")
        sys.exit(1)

def main():
    # Drop the existing 'notes' table
    drop_notes_table()

    # Recreate the 'notes' table with the new fields
    recreate_notes_table()

    # Run Flask migration commands
    run_flask_migrations()

if __name__ == "__main__":
    main()
