import wf_syndicate_db
import sqlite3


content_table_names = ["Cetus Bounty Rewards:", 
                       "Orb Vallis Bounty Rewards:", 
                       "Cambion Drift Bounty Rewards:",
                       "Zariman Bounty Rewards:",
                       "Albrecht's Laboratories Bounty Rewards:",
                       "Hex Bounty Rewards:"
                       ]


def update_syndicate_DB(url):
    
    wf_syndicate_db.update_syndicate_DB(url, content_table_names)
    

def get_related_items(items):
    
    related_items = []
    
    con = sqlite3.connect('syndicates.db')
    cur = con.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    table_names = [table[0] for table in tables]
    
    for table_name in table_names:
        for item in items:
            if item.lower() in table_name.lower():
                related_items.append(table_name)
                
    return related_items


def query_items(items, minimum_drop_rate = 5):
    
    con = sqlite3.connect('syndicates.db')
    cur = con.cursor()
    
    for item in items:
        
        print(item, ":")
        
        get = f'''SELECT * FROM "{item}" WHERE drop_rate > {minimum_drop_rate}'''   
        cur.execute(get)
        missions = cur.fetchall()
        
        for mission in missions:
            print(" -", mission[0], "|", mission[1], "|", mission[2], "|", str(mission[3])+"%")
            
        print()
    
    

if __name__ == '__main__':
     
    url = 'https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html'
    
    
    #update_syndicate_DB(url)
    
    
    related_items = get_related_items(["Axi G14", "Neo Q1", "Axi t12"])
    
    query_items(related_items)
    