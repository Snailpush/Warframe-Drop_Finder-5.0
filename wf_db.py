from bs4 import BeautifulSoup
import requests
import sqlite3

import wf_mission_config


class Mission:
    def __init__(self, text):
        
        name, planet, mission_type = self.format_missions(text)
        
        self.name = name
        self.planet = planet
        self.mission_type = mission_type
        
        
        pass
    
    def format_missions(self, mission_info):
        ''' "Planet/Name (Type)" -> [Name, Planet, Type] '''
        
        name = ''
        mission_type = ''
        if "/" in mission_info:
            planet, mission = mission_info.split('/')
        

            indx_start = mission.index('(')
            indx_end = mission.index(')')
            mission_type = mission[indx_start+1:indx_end] 
            
            name = mission[:indx_start-1] + mission[indx_end+1:]
            
        else:
            name = mission_info
            planet = ""
            mission_type = "Special"
        return name.strip(), planet.strip(), mission_type.strip()
    

    
# Open database connection
con = sqlite3.connect('mission.db')
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
                mission_type varchar(255),
                planet varchar(255),
                rotation varchar(255),
                drop_rate double)'''.format(item_name=item_name)
    cur.execute(create)

def insert_current_item(item_name, drop_rate, mission, rotation):
    insert = '''INSERT INTO "{item_name}"(mission_name, mission_type, planet, rotation, drop_rate) 
                VALUES (?, ?, ?, ?, ?)'''.format(item_name=item_name)
    cur.execute(insert, (mission.name, mission.mission_type, mission.planet, rotation, drop_rate))

def create_new_db(url):

    print("Delete old DB")
    delete_all_tables()
    
    print("Create New Mission Config")
    wf_mission_config.mission_config_db()
    
    print("Load URL")
    # Load page content
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    print("Create new DB")
    # Main mission table
    content = soup.find('table')

    # All rows
    rows = content.find_all('tr')

    current_mission = ''
    currernt_rotation = 'A'

    # Iterate rows
    for row in rows:
        # Check for Mission name or Rotation name
        header = row.find('th')

        # Mission or Rotation
        if header is not None:
            if header.text.strip() == 'Rotation A':
                currernt_rotation = 'A'
            elif header.text.strip() == 'Rotation B':
                currernt_rotation = 'B'
            elif header.text.strip() == 'Rotation C':
                currernt_rotation = 'C'
            else:
                current_mission = Mission(header.text.strip())
        else:
            body = row.find_all('td')
            if len(body) > 1:
                # Item name
                item_name = body[0].text.strip()
                # Drop chance
                drop_chance = body[1].text.strip()
                
                # Create table if not exists
                create_new_item_table(item_name)
                # Insert current item
                insert_current_item(item_name, drop_chance, current_mission, currernt_rotation)
            else:
                current_mission = ''
                currernt_rotation = 'A'

        

    # Commit and close database connection
    con.commit()
    con.close()