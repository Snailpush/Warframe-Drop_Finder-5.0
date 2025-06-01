

def user_input():
    
    ret = {}
    
    update_input = input("Update Database (Y/n) \n")
    if update_input.lower() == "y":
        update = True
    elif update_input.lower() == "n":
        update = False
    else:
        raise Exception("Unknown Input")
        
    ret["update"] = update
    
    
    more_items = True
    items = []
    
    while(more_items):
        item = input("Add Item: \n")
        items.append(item)
        
        more_items_input = input("More items? (Y/n) \n")
        if more_items_input.lower() == "y":
            more_items = True
        elif more_items_input.lower() == "n":
            more_items = False
        else:
            raise Exception("Unknown Input")
            
    ret["items"] = items
    
    
        
    related_input = input("Show related Items (Y/n) \n")
    if related_input.lower() == "y":
        related = True
    elif related_input.lower() == "n":
        related = False
    else:
        raise Exception("Unknown Input")
        
    ret["show_related"] = related
    
    
    
    time_scale_input = input("Time Scale \n")
    time_scale = int(time_scale_input)
    
    ret["time_scale"] = time_scale
    
    
    report_length_input = input("Show how many Droplocations? \n")
    report_length = int(report_length_input)
    
    ret["report_length"] = report_length
    
    print("\n ------------ \n")
    
    
    return ret