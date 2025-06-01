import sqlite3

def search_best_expected_return(items, time_scale=1):
    
    con = sqlite3.connect('mission.db')
    cur = con.cursor()
    
    config_con = sqlite3.connect('config.db')
    config_cur = config_con.cursor()
    
    # get Unique Drop locations
    unique_locations = set()
    for item in items:
        get = f'''SELECT DISTINCT mission_name, planet, mission_type FROM "{item}"'''   
        cur.execute(get)
        missions = cur.fetchall()
        
        unique_locations.update(missions)
     
    unique_locations = list(unique_locations)
    
    
    
    missions_for_items = []
        
    for location in unique_locations:
        # mission Info
        mission_name = location[0]
        planet = location[1]
        mission_type = location[2]
        

        
        item_drop_rate = {}
        
        total_drop_rate = {
            'A': 0,
            'B': 0,
            'C': 0
            }
        
        # all related items
        for item in items:
            
            item_drop_rate[item] = {
                'A': 0,
                'B': 0,
                'C': 0
                }
            
            get = f'''SELECT rotation, drop_rate FROM "{item}"
            WHERE mission_name LIKE "{mission_name}" AND planet LIKE "{planet}" AND mission_type LIKE "{mission_type}"''' 
            cur.execute(get)
            drops = cur.fetchall() 
            
            # different Rotations + potential dublications in a rotation
            for drop in drops:
                
                rot = drop[0]
                
                drop_chance = drop[1]
                drop_start = drop_chance.index('(')
                drop_end = drop_chance.index('%')
                drop_chance = drop_chance[drop_start+1:drop_end]
                drop_chance = float(drop_chance)/100
                
                
                item_drop_rate[item][rot] += drop_chance
                
                total_drop_rate[rot] += drop_chance
                   
               
        #print()
        #print(mission_name + "/" + planet + ": " + mission_type)
        #print("Per Item Drop Rate:", item_drop_rate)
        #print("Total Drop Rate:", total_drop_rate)
        #print()
        
        
        farm_strategy = ['A','B','C']
        for strategy in farm_strategy:
            
            get_config = f'''SELECT * FROM mission_config 
            WHERE mission_type LIKE "{mission_type}" AND rotation LIKE "%{strategy}%"'''
            
            config_cur.execute(get_config)
            type_config = config_cur.fetchall()
            
            if len(type_config) > 0:
                
                type_config = type_config[0]
                        
                type_config = {
                    'type_name': type_config[0],
                    'farm strat': type_config[1],
                    'time': type_config[2],
                    'A': type_config[3],
                    'B': type_config[4],
                    'C': type_config[5]
                    }
                
                # Total expected drop
                expected_drop_total = 0
                expected_drop_total += total_drop_rate['A'] * type_config['A']
                expected_drop_total += total_drop_rate['B'] * type_config['B']
                expected_drop_total += total_drop_rate['C'] * type_config['C']
                expected_drop_total /= type_config['time']
                expected_drop_total *= time_scale
                
               
                    
                    
                # Per Item expected drop
                expected_drop_item = {}
                for item_name in item_drop_rate.keys():
                    expected_drop_item[item_name] = 0
                    expected_drop_item[item_name] += item_drop_rate[item_name]['A'] * type_config['A']
                    expected_drop_item[item_name] += item_drop_rate[item_name]['B'] * type_config['B']
                    expected_drop_item[item_name] += item_drop_rate[item_name]['C'] * type_config['C']
                    expected_drop_item[item_name] /= type_config['time']
                    expected_drop_item[item_name] *= time_scale
                    
                
                if expected_drop_total > 0:
                    
                    mission = Mission(mission_name, planet, mission_type, strategy,expected_drop_total, expected_drop_item)
                    missions_for_items.append(mission)
                    
    con.commit()
    con.close()
    
    config_con.commit()
    config_con.close()
    
    return missions_for_items

        
    
    pass

class Mission:
    def __init__(self, mission_name, planet, mission_type, strategy, expected_drop_total, expected_drop_item):
        
        self.mission_name = mission_name
        self.planet = planet
        self.mission_type = mission_type
        
        self.strategy = strategy
        
        self.total_drop = expected_drop_total
        self.item_drop_rate = expected_drop_item
        
        
    def __str__(self):
        
        print()
        print(self.mission_name + "/" + self.planet + ": " + self.mission_type)
        print('Strategy: ' + self.strategy)
        print('Expected Return: ', round(self.total_drop,4))
        for item_name in self.item_drop_rate.keys():
            if self.item_drop_rate[item_name] > 0:
                print(' -' + item_name + ": ", round(self.item_drop_rate[item_name],4))
        
        return""
    
    
    