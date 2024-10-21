import sqlite3

# Path to your SQLite database
db_path = "C:/Projects/GitHub/PoGO/pogo.db"

def drop_table():
    """Drop the poke_genie table if it exists."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS poke_genie;")
    conn.commit()
    conn.close()
    print("Table 'poke_genie' dropped.")

def recreate_table():
    """Recreate the poke_genie table with all necessary fields."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the poke_genie table with all the fields from the CSV
    cursor.execute('''
        CREATE TABLE poke_genie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            `index` INTEGER,
            `name` TEXT,
            `form` TEXT,
            `pokemon_number` INTEGER,
            `gender` TEXT,
            `cp` INTEGER,
            `hp` INTEGER,
            `atk_iv` INTEGER,
            `def_iv` INTEGER,
            `sta_iv` INTEGER,
            `iv_avg` REAL,
            `level_min` REAL,
            `level_max` REAL,
            `quick_move` TEXT,
            `charge_move` TEXT,
            `charge_move_2` TEXT,
            `scan_date` TEXT,
            `original_scan_date` TEXT,
            `catch_date` TEXT,
            `weight` REAL,
            `height` REAL,
            `lucky` BOOLEAN,
            `shadow_purified` TEXT,
            `favorite` INTEGER,
            `dust` INTEGER,
            `rank_g_pct` REAL,
            `rank_g_num` INTEGER,
            `stat_prod_g` REAL,
            `dust_cost_g` INTEGER,
            `candy_cost_g` INTEGER,
            `name_g` TEXT,
            `form_g` TEXT,
            `sha_pur_g` TEXT,
            `rank_u_pct` REAL,
            `rank_u_num` INTEGER,
            `stat_prod_u` REAL,
            `dust_cost_u` INTEGER,
            `candy_cost_u` INTEGER,
            `name_u` TEXT,
            `form_u` TEXT,
            `sha_pur_u` TEXT,
            `rank_l_pct` REAL,
            `rank_l_num` INTEGER,
            `stat_prod_l` REAL,
            `dust_cost_l` INTEGER,
            `candy_cost_l` INTEGER,
            `name_l` TEXT,
            `form_l` TEXT,
            `sha_pur_l` TEXT,
            `marked_for_pvp` BOOLEAN
        );
    ''')
    
    conn.commit()
    conn.close()
    print("Recreated the 'poke_genie' table with the necessary columns.")

def main():
    drop_table()
    recreate_table()

if __name__ == "__main__":
    main()
