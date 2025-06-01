import sqlite3


default_config = [
    
    ("Capture", "A", 2, 1, 0, 0),
    ("Exterminate", "A", 3, 1, 0, 0),
    ("Mobile Defense", "A", 5, 1, 0, 0),
    ("Sabotage", "A", 5, 1, 0, 0),      # Void
    ("Assassination", "A", 3, 1, 0, 0),
    ("Skirmish", "A", 5, 1, 0, 0), 
    ("Pursuit", "A", 5, 1, 0, 0),
    
        
    ("Disruption", "A", 3.5, 1, 0, 0),
    ("Disruption", "B", 3.5, 0, 1, 0),
    ("Disruption", "C", 30, 0, 1, 7),
    
    ("Survival", "A", 5, 1, 0, 0),
    ("Survival", "B", 15, 2, 1, 0),
    ("Survival", "C", 20, 2, 1, 1),
    
    ("Defense", "A", 5, 1, 0, 0),
    ("Defense", "B", 15, 2, 1, 0),
    ("Defense", "C", 20, 2, 1, 1),
    
    ("Interception", "A", 5, 1, 0, 0),
    ("Interception", "B", 15, 2, 1, 0),
    ("Interception", "C", 20, 2, 1, 1),
    
    ("Excavation", "A", 1.5, 1, 0, 0),
    ("Excavation", "B", 4.5, 2, 1, 0),
    ("Excavation", "C", 6, 2, 1, 1),
    
    ("Sanctuary Onslaught", "A", 5, 1, 0, 0),
    ("Sanctuary Onslaught", "B", 15, 2, 1, 0),
    ("Sanctuary Onslaught", "C", 20, 2, 1, 1),
    
    
    ("Alchemy", "A", 4, 1, 0, 0),
    ("Alchemy", "B", 10, 2, 1, 0),
    ("Alchemy", "C", 15, 2, 1, 1),
        
    ("Defection", "A", 5, 2, 0, 0),
    ("Defection", "B", 15, 4, 2, 0),
    ("Defection", "C", 20, 4, 2, 2),
    
    ("Rescue", "A", 3, 1, 1, 1),
    ("Rescue", "B", 3, 1, 1, 1),
    ("Rescue", "C", 3, 1, 1, 1),
    
    ("Caches", "A", 4, 1, 0, 0),        # Both Sabotage / Railjack
    ("Caches", "B", 5, 1, 1, 0),        # Both Sabotage / Railjack
    ("Caches", "C", 6, 1, 1, 1),        # Only Sabotage
    
    ("Spy", "A", 4, 1, 1, 1),
    ("Spy", "B", 4, 1, 1, 1),
    ("Spy", "C", 4, 1, 1, 1),
    
    ("Rush", "A", 4, 1, 1, 1),
    ("Rush", "B", 4, 1, 1, 1),
    ("Rush", "C", 4, 1, 1, 1),
    
    ("Mirror Defense", "A", 6, 1, 0, 0),
    ("Mirror Defense", "B", 18, 2, 1, 0),
    ("Mirror Defense", "C", 24, 2, 1, 1),
    
    ("Infested Salvage", "A", 4, 1, 0, 0),
    ("Infested Salvage", "B", 12, 2, 1, 0),
    ("Infested Salvage", "C", 16, 2, 1, 1),
    
    ("Void Armageddon", "A", 6, 1, 0, 0),
    ("Void Armageddon", "B", 18, 2, 1, 0),
    ("Void Armageddon", "C", 24, 2, 1, 1),
    
    ("Void Cascade", "A", 5, 1, 0, 0),
    ("Void Cascade", "B", 15, 2, 1, 0),
    ("Void Cascade", "C", 20, 2, 1, 1),
    
    ("Void Flood", "A", 5, 2, 0, 0),
    ("Void Flood", "B", 15, 4, 2, 0),
    ("Void Flood", "C", 20, 4, 2, 2),
    
    ("Low Risk", "A", 5, 1, 0, 0),      # Index
    ("Low Risk", "B", 15, 2, 1, 0),     # Index
    ("Low Risk", "C", 20, 2, 1, 1),     # Index
    
    ("Medium Risk", "A", 5, 1, 0, 0),     # Index
    ("Medium Risk", "B", 15, 2, 1, 0),    # Index
    ("Medium Risk", "C", 20, 2, 1, 1),    # Index
        
    ("High Risk", "A", 5, 1, 0, 0),     # Index
    ("High Risk", "B", 15, 2, 1, 0),    # Index
    ("High Risk", "C", 20, 2, 1, 1),    # Index
    
    ("Arena", "A", 5, 1, 0, 0),      # Sedna
    ("Arena", "B", 15, 2, 1, 0),     # Index
    ("Arena", "C", 20, 2, 1, 1),     # Index
    
    ("Variant", "A", 5, 1, 0, 0),      # Conclave
    ("Variant", "B", 15, 2, 1, 0),     # Conclave
    ("Variant", "C", 20, 2, 1, 1),     # Conclave
    
    ("Conclave", "A", 10, 1, 0, 0),      # Conclave
    ("Conclave", "B", 10, 1, 1, 0),     # Conclave
    
    ("Normal", "A", 30, 1, 0, 0),       # Duviri
    ("Hard", "A", 30, 1, 0, 0),       # Duviri
    
    ("Special", "A", 10, 1, 1, 1),
    ("Special", "B", 10, 1, 1, 1),
    ("Special", "C", 10, 1, 1, 1),
    
    ("Shrine Defense", "A", 3, 1, 0, 0),
    
    ("Legacyte Harvest", "A", "3", 1, 0, 0),
    ("Legacyte Harvest", "B", "9", 2, 1, 0),
    ("Legacyte Harvest", "C", "12", 2, 1, 1),
    
    ]

def mission_config_db():
    
    con = sqlite3.connect('config.db')
    cur = con.cursor()
    
    delete = '''DROP TABLE IF EXISTS mission_config'''
    cur.execute(delete)
    
    create = '''CREATE TABLE mission_config ( 
                mission_type varchar(255),
                rotation varchar(255),
                time double,
                A double,
                B double, 
                C double)'''
    
    cur.execute(create)
    
    for mission in default_config:
        insert = '''INSERT INTO "mission_config"(mission_type, rotation, time, A, B, C) 
                    VALUES (?, ?, ?, ?, ?, ?)'''
        cur.execute(insert, (mission[0], mission[1], mission[2], mission[3], mission[4], mission[5]))
        
    con.commit()
    con.close()
