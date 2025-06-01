import wf_db
import wf_debug
import wf_query
import wf_user_friendly
import wf_syndicate

def main():
    
    if update:
        wf_db.create_new_db(URL)
        
        if check_syndicates:
            wf_syndicate.update_syndicate_DB(URL)
    
    #wf_debug.print_items()
    
    #wf_debug.print_unique_mission_types()
    
    
    related_items = wf_debug.get_related_items(items)
    if show_related:
        print()
        print("Related Items:")
        print(related_items)
        print()
        
        if check_syndicates:
            syndicate_related_items = wf_syndicate.get_related_items(items)
            if len(syndicate_related_items) == 0:
                print("No Related Items in Syndicates")
            else:
                print("Related Items in Syndicates:")
                print(syndicate_related_items)
                print()
                print("Syndicate Drops")
                wf_syndicate.query_items(syndicate_related_items, syndicate_minimum_drop_rate)
                
                
                
                
    
    print("-------------------------\n")
    print("Best Farming Locations:")
    report = wf_query.search_best_expected_return(related_items, time_scale=time_scale)
    
    wf_debug.display_report(report, report_length)
    pass




if __name__ == '__main__':
    
    URL = 'https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html'
    
    manual_input = False
    
    if manual_input:
        user_input = wf_user_friendly.user_input()
        
        update = user_input["update"]
        items = user_input["items"]
        show_related = user_input["show_related"]
        time_scale = user_input["time_scale"]
        report_length = user_input["report_length"]
    
    
    else:
    
        update = False
        items = ["Neo D10"]
        show_related = True
        time_scale = 20
        report_length = 5
        
        check_syndicates = True
        syndicate_minimum_drop_rate = 5

    
    main()