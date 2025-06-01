import sqlite3
import requests
from bs4 import BeautifulSoup

# Open database connection
con = sqlite3.connect('syndicates.db')
cur = con.cursor()

def delete_all_tables():

    # Get a list of all tables in the database
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Drop each table
    for table in tables:
        table_name = table[0]
        cur.execute(f'DROP TABLE "{table_name}";')

    # Commit the changes and close the connection
    con.commit()
    #con.close()
    
    
def create_new_item_table(item_name):
    create = '''CREATE TABLE IF NOT EXISTS "{item_name}" ( 
                mission_name varchar(255),
                rotation varchar(255),
                stage varchar(255),
                drop_rate double)'''.format(item_name=item_name)
    cur.execute(create)

def insert_current_item(item_name, drop_rate, mission_name, rotation, stage):
    
    # formatd roprate
    indx_start = drop_rate.index('(')
    indx_end = drop_rate.index(')')
    drop_rate = float(drop_rate[indx_start+1:indx_end-1])
    
    insert = '''INSERT INTO "{item_name}"(mission_name, rotation, stage, drop_rate) 
                VALUES (?, ?, ?, ?)'''.format(item_name=item_name)
    
    cur.execute(insert, (mission_name, rotation, stage, drop_rate))
    
    
    
def update_syndicate_DB(url, content_table_names):
    
    delete_all_tables()
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    
    
    # Find correct tables
    content_table_ids = {}

    content = soup.find_all('h3')

    for i,heading in enumerate(content):
        
        if heading.text in content_table_names:
            table_name = heading.text.replace(" Rewards:", "")
            content_table_ids[table_name] = i-2;
            

    all_tables = soup.find_all('table')
    content_tables = {}


    for table_name, table_id in content_table_ids.items():
        content_tables[table_name] = all_tables[table_id]
    
    
    
    
    # Table for each item
    
    # each syndicate
    for syndicate_bounty in content_tables:
        
        current_mission = ""
        currernt_rotation = "A"
        current_stage = ""

        # All rows
        rows = content_tables[syndicate_bounty].find_all('tr')
        
        for row in rows:
            
            header = row.find('th')

            # Mission / Rotation / Stage
            if header is not None:
                # Rotation
                if header.text.strip() == 'Rotation A':
                    currernt_rotation = 'A'
                elif header.text.strip() == 'Rotation B':
                    currernt_rotation = 'B'
                elif header.text.strip() == 'Rotation C':
                    currernt_rotation = 'C'
                else:
                    colspan = header.get("colspan")
                    
                    # Mission
                    if colspan == '3':
                        current_mission = header.text.strip()
                    # Stage
                    elif colspan == '2':
                        current_stage = header.text.strip()
                    else:
                        print("Something I didn't thought off")
            else:
                body = row.find_all('td')
                if len(body) > 1:
                    # Item name
                    item_name = body[1].text.strip()
                    # Drop chance
                    drop_chance = body[2].text.strip()
                    
                    
                    #print(current_mission, currernt_rotation, current_stage, item_name, drop_chance)
                    
                    # Create table if not exists
                    create_new_item_table(item_name)
                    # Insert current item
                    insert_current_item(item_name, drop_chance, current_mission, currernt_rotation, current_stage)
                    
                    
                else:
                    current_mission = ''
                    currernt_rotation = 'A'
                    current_stage = ""
                    
    # Commit and close database connection
    con.commit()
    con.close()