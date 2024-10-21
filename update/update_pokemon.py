# update_pokemon.py

import os
import sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# Add the project root directory (where app.py and models.py are located) to the system path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Importing db and Pokemon model from models.py
from models import db, Pokemon

# Define specific forms to skip (with spaces to ensure exact matches)
FORMS_TO_SKIP = [" Mega ", " Alolan ", " Galarian ", " Hisuian "]

def fetch_pokemon_data(app_context):
    with app_context:
        print("Starting to fetch and update Pokémon data...")

        # Scrape Pokémon data from the Pokémon DB website
        url = "https://pokemondb.net/go/pokedex"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse the HTML table containing the Pokémon data
        table = soup.find("table", {"id": "pokedex"})
        rows = table.find_all("tr")[1:]  # Skip the header row

        image_dir = os.path.join('C:/Projects/GitHub/PoGO/static/images', 'mons')

        count_updated = 0
        count_inserted = 0
        count_with_images = 0
        total_pokemon = len(rows)

        # Loop through the Pokémon from the website
        for row in rows:
            cols = row.find_all("td")
            dex_number = int(cols[0].text.strip())  # Dex number as integer
            name = cols[1].text.strip().replace("♀", "-f").replace("♂", "-m")
            type_ = " ".join([t.text for t in cols[2].find_all("a")])

            # Filter out Pokémon names with specific forms (Mega, Alolan, Galarian, Hisuian)
            if any(form in name for form in FORMS_TO_SKIP):
                continue

            # Construct image filename based on Pokémon name and check if it exists
            image_filename = f"{name.lower().replace(' ', '-').replace(':', '')}.png"
            image_path = os.path.join(image_dir, image_filename)

            local_image_url = f"/static/images/mons/{image_filename}" if os.path.exists(image_path) else None

            if local_image_url:
                count_with_images += 1

            # Check if Pokémon already exists in the database
            pokemon = Pokemon.query.filter_by(id=dex_number).first()

            # Update the existing Pokémon entry or insert a new one
            if pokemon:
                pokemon.image_url = local_image_url  # Update the image URL or None
                db.session.commit()
                count_updated += 1
            else:
                new_pokemon = Pokemon(
                    id=dex_number,
                    name=name,
                    type=type_,
                    image_url=local_image_url,
                )
                db.session.add(new_pokemon)
                db.session.commit()
                count_inserted += 1

        print(f"Finished fetching and saving Pokémon data.")
        print(f"Total Pokémon processed: {total_pokemon}")
        print(f"Total Pokémon added: {count_inserted}")
        print(f"Total Pokémon updated: {count_updated}")
        print(f"Total Pokémon with images added: {count_with_images}")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        fetch_pokemon_data(app.app_context())