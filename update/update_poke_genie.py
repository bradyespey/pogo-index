import os
import csv
import sqlite3

# Database path
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def get_latest_poke_genie_csv(directory):
    """Get the latest CSV file from the specified directory."""
    try:
        csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
        if not csv_files:
            print("No CSV files found.")
            return None

        latest_file = max([os.path.join(directory, f) for f in csv_files], key=os.path.getctime)
        print(f"Latest CSV file found: {latest_file}")
        return latest_file
    except Exception as e:
        print(f"Error finding latest CSV: {e}")
        return None

def insert_data_to_db(data):
    """Insert the CSV data into the SQLite poke_genie table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Delete all existing data in the poke_genie table
        cursor.execute("DELETE FROM poke_genie")

        # Insert statement for the PokeGenieEntry table
        insert_query = '''
            INSERT INTO poke_genie (
                `index`, `name`, `form`, `pokemon_number`, `gender`, `cp`, `hp`,
                `atk_iv`, `def_iv`, `sta_iv`, `iv_avg`, `level_min`, `level_max`,
                `quick_move`, `charge_move`, `charge_move_2`, `scan_date`, `original_scan_date`,
                `catch_date`, `weight`, `height`, `lucky`, `shadow_purified`, `favorite`,
                `dust`, `rank_g_pct`, `rank_g_num`, `stat_prod_g`, `dust_cost_g`, `candy_cost_g`,
                `name_g`, `form_g`, `sha_pur_g`, `rank_u_pct`, `rank_u_num`, `stat_prod_u`, 
                `dust_cost_u`, `candy_cost_u`, `name_u`, `form_u`, `sha_pur_u`, `rank_l_pct`, 
                `rank_l_num`, `stat_prod_l`, `dust_cost_l`, `candy_cost_l`, `name_l`, 
                `form_l`, `sha_pur_l`, `marked_for_pvp`
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        cursor.executemany(insert_query, data)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error inserting data into the database: {e}")

def sanitize_value(value, data_type=str):
    """Safely convert values to the specified data type, returning None if conversion fails."""
    try:
        return data_type(value) if value else None
    except (ValueError, TypeError):
        return None

def import_poke_genie_data():
    print("Starting to import Poke Genie data...")

    directory = r'G:\My Drive\Games\Pokémon Go'
    csv_file_path = get_latest_poke_genie_csv(directory)
    if not csv_file_path:
        print("No CSV file found. Exiting.")
        return

    data_to_insert = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        print(f"Headers: {headers}")

        row_count = 0

        for row in reader:
            try:
                # Prepare the data row for insertion without transformations
                sanitized_row = (
                    sanitize_value(row[0], int),      # Index
                    sanitize_value(row[1], str),      # Name
                    sanitize_value(row[2], str),      # Form
                    sanitize_value(row[3], int),      # Pokemon Number
                    sanitize_value(row[4], str),      # Gender
                    sanitize_value(row[5], int),      # CP
                    sanitize_value(row[6], int),      # HP
                    sanitize_value(row[7], int),      # Atk IV
                    sanitize_value(row[8], int),      # Def IV
                    sanitize_value(row[9], int),      # Sta IV
                    sanitize_value(row[10], float),   # IV Avg
                    sanitize_value(row[11], float),   # Level Min
                    sanitize_value(row[12], float),   # Level Max
                    sanitize_value(row[13], str),     # Quick Move
                    sanitize_value(row[14], str),     # Charge Move
                    sanitize_value(row[15], str),     # Charge Move 2
                    sanitize_value(row[16], str),     # Scan Date
                    sanitize_value(row[17], str),     # Original Scan Date
                    sanitize_value(row[18], str),     # Catch Date
                    sanitize_value(row[19], float),   # Weight
                    sanitize_value(row[20], float),   # Height
                    sanitize_value(row[21], int),     # Lucky
                    sanitize_value(row[22], int),     # Shadow/Purified
                    sanitize_value(row[23], int),     # Favorite
                    sanitize_value(row[24], int),
                    sanitize_value(row[25], float),
                    sanitize_value(row[26], int),
                    sanitize_value(row[27], float),
                    sanitize_value(row[28], int),
                    sanitize_value(row[29], int),
                    sanitize_value(row[30], str),
                    sanitize_value(row[31], str),
                    sanitize_value(row[32], int),     # Sha/Pur (G) as integer
                    sanitize_value(row[33], float),
                    sanitize_value(row[34], int),
                    sanitize_value(row[35], float),
                    sanitize_value(row[36], int),
                    sanitize_value(row[37], int),
                    sanitize_value(row[38], str),
                    sanitize_value(row[39], str),
                    sanitize_value(row[40], int),     # Sha/Pur (U) as integer
                    sanitize_value(row[41], float),
                    sanitize_value(row[42], int),
                    sanitize_value(row[43], float),
                    sanitize_value(row[44], int),
                    sanitize_value(row[45], int),
                    sanitize_value(row[46], str),
                    sanitize_value(row[47], str),
                    sanitize_value(row[48], int),     # Sha/Pur (L) as integer
                    sanitize_value(row[49], int),     # Marked for PvP Use
                )
                data_to_insert.append(sanitized_row)
                row_count += 1

            except Exception as e:
                print(f"Error processing row {row}: {e}")

        # Insert the sanitized data into the database
        insert_data_to_db(data_to_insert)

        print(f"Finished importing Poke Genie data. Total rows processed: {row_count}")

if __name__ == "__main__":
    import_poke_genie_data()
    