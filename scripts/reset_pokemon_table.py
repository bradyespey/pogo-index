import os
import sys
from pathlib import Path
import subprocess

# Add the root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Now we import app and db inside the functions to avoid any circular import issues
def drop_pokemon_table():
    """Drop the Pokémon table from the PostgreSQL database."""
    from app import app, db  # Import app and db locally
    with app.app_context():
        db.drop_all()  # Drop all tables including 'pokemon'
        db.session.commit()
        print("Dropped all tables.")

def recreate_pokemon_table():
    """Recreate the Pokémon table using SQLAlchemy."""
    from app import app, db  # Import app and db locally
    with app.app_context():
        db.create_all()  # Recreate all tables, including the updated 'pokemon' table
        db.session.commit()
        print("Recreated all tables.")

def run_update_script():
    """Run the update script for the Pokémon table."""
    try:
        print("Running update_pokemon.py script...")
        update_script_path = Path(__file__).resolve().parent / 'update_pokemon.py'
        subprocess.run([sys.executable, str(update_script_path)], check=True)
        print("Update script ran successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running the update script: {e}")
        sys.exit(1)

def main():
    # Drop the existing Pokémon table
    drop_pokemon_table()

    # Recreate the Pokémon table with the new fields
    recreate_pokemon_table()

    # Run the update script
    run_update_script()

if __name__ == "__main__":
    main()