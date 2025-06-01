import sqlite3

def print_items():
    
    con = sqlite3.connect('mission.db')
    cur = con.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Drop each table
    for table in tables:
        table_name = table[0]
    
        print(table_name)
        
        
    con.commit()
    con.close()
    
    
def print_unique_mission_types():
    
    unique_mission_types = set()
    
    con = sqlite3.connect('mission.db')
    cur = con.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    
    for table in tables:
        cur.execute(f'SELECT DISTINCT mission_type FROM "{table[0]}"')
        mission_types = cur.fetchall()
        unique_mission_types.update(mission_types)

        
    con.commit()
    con.close()
    
    print(unique_mission_types)
    

def get_related_items(items):
    
    related_items = []
    
    con = sqlite3.connect('mission.db')
    cur = con.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    table_names = [table[0] for table in tables]
    
    for table_name in table_names:
        for item in items:
            if item.lower() in table_name.lower():
                related_items.append(table_name)
                
    return related_items


def display_report(report, num_items=5):
    report.sort(key=lambda x: x.total_drop)
    # Display only the top 5 missions
    for mission in report[-num_items:]:
        print(mission)
    
    