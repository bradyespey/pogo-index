import os
import sys
from pathlib import Path

# Add the parent directory to the system path, so it can find app.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app, db
from models import Pokemon, PokeGenieEntry, ShinyPokemon, SpecialsPokemon, Costume, Form, Rocket, Note

def check_table_entries():
    with app.app_context():
        # Pokémon table
        print("Checking Pokémon table entries:")
        pokemon_entries = db.session.query(Pokemon.id, Pokemon.name, Pokemon.type, Pokemon.image_url).limit(5).all()
        for p in pokemon_entries:
            print(f"id: {p.id}, name: {p.name}, type: {p.type}, image_url: {p.image_url}")

        # Poke Genie table
        print("\nChecking Poke Genie table entries:")
        poke_genie_entries = db.session.query(
            PokeGenieEntry.index, PokeGenieEntry.name, PokeGenieEntry.form, PokeGenieEntry.pokemon_number, 
            PokeGenieEntry.gender, PokeGenieEntry.cp, PokeGenieEntry.hp, PokeGenieEntry.atk_iv, 
            PokeGenieEntry.def_iv, PokeGenieEntry.sta_iv, PokeGenieEntry.iv_avg, PokeGenieEntry.level_min, 
            PokeGenieEntry.level_max, PokeGenieEntry.quick_move, PokeGenieEntry.charge_move, 
            PokeGenieEntry.charge_move_2, PokeGenieEntry.scan_date, PokeGenieEntry.original_scan_date, 
            PokeGenieEntry.catch_date, PokeGenieEntry.weight, PokeGenieEntry.height, PokeGenieEntry.lucky, 
            PokeGenieEntry.shadow_purified, PokeGenieEntry.favorite, PokeGenieEntry.dust, 
            PokeGenieEntry.rank_g_pct, PokeGenieEntry.rank_g_num, PokeGenieEntry.stat_prod_g, 
            PokeGenieEntry.dust_cost_g, PokeGenieEntry.candy_cost_g, PokeGenieEntry.name_g, 
            PokeGenieEntry.form_g, PokeGenieEntry.sha_pur_g, PokeGenieEntry.rank_u_pct, PokeGenieEntry.rank_u_num,
            PokeGenieEntry.stat_prod_u, PokeGenieEntry.dust_cost_u, PokeGenieEntry.candy_cost_u, 
            PokeGenieEntry.name_u, PokeGenieEntry.form_u, PokeGenieEntry.sha_pur_u, PokeGenieEntry.rank_l_pct, 
            PokeGenieEntry.rank_l_num, PokeGenieEntry.stat_prod_l, PokeGenieEntry.dust_cost_l, 
            PokeGenieEntry.candy_cost_l, PokeGenieEntry.name_l, PokeGenieEntry.form_l, 
            PokeGenieEntry.marked_for_pvp).limit(5).all()
        for pg in poke_genie_entries:
            print(pg)

        # Shiny Pokémon table
        print("\nChecking Shiny Pokémon table entries:")
        shiny_entries = db.session.query(ShinyPokemon.id, ShinyPokemon.dex_number, ShinyPokemon.name, ShinyPokemon.method).limit(5).all()
        for s in shiny_entries:
            print(f"id: {s.id}, dex_number: {s.dex_number}, name: {s.name}, method: {s.method}")

        # Specials Pokémon table
        print("\nChecking Specials Pokémon table entries:")
        specials_entries = db.session.query(SpecialsPokemon.id, SpecialsPokemon.dex_number, SpecialsPokemon.name, SpecialsPokemon.type).limit(5).all()
        for sp in specials_entries:
            print(f"id: {sp.id}, dex_number: {sp.dex_number}, name: {sp.name}, type: {sp.type}")

        # Costume Pokémon table
        print("\nChecking Costume Pokémon table entries:")
        costume_entries = db.session.query(Costume.id, Costume.dex_number, Costume.name, Costume.costume).limit(5).all()
        for c in costume_entries:
            print(f"id: {c.id}, dex_number: {c.dex_number}, name: {c.name}, costume: {c.costume}")

        # Forms table
        print("\nChecking Forms table entries:")
        form_entries = db.session.query(Form.id, Form.dex_number, Form.name, Form.form).limit(5).all()
        for f in form_entries:
            print(f"id: {f.id}, dex_number: {f.dex_number}, name: {f.name}, form: {f.form}")

        # Rocket Pokémon table
        print("\nChecking Rocket Pokémon table entries:")
        rocket_entries = db.session.query(Rocket.id, Rocket.dex_number, Rocket.name, Rocket.method).limit(5).all()
        for r in rocket_entries:
            print(f"id: {r.id}, dex_number: {r.dex_number}, name: {r.name}, method: {r.method}")

        # Notes table
        print("\nChecking Notes table entries:")
        note_entries = db.session.query(Note.id, Note.pokemon_id, Note.note_text).limit(5).all()
        for n in note_entries:
            print(f"id: {n.id}, pokemon_id: {n.pokemon_id}, note_text: {n.note_text}")

if __name__ == "__main__":
    check_table_entries()