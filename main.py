#from actors.enemy import Enemy
#from actors.player import Player
#from events.fight import Fight

#from items.storage import Storage


#player=Player(first_name="Player", hp=100, inventory=Storage([]), attack_point=10)

#enemies=[Enemy(first_name="Enemy", hp=40, inventory=Storage([]), attack_point=10),
#        Enemy(first_name="Enemy", hp=40, inventory=Storage([]), attack_point=40),
#        Enemy(first_name="Enemy", hp=40, inventory=Storage([]), attack_point=10)]


#while player.is_alive():
    
#    for enemy in enemies:
#        Fight.fight_without_steps(player,enemy)
#        if not player.is_alive():
#            break
        
#if player.is_alive():
#    print("You won")
#else: 
#    print("Wasted!")


from utils.location_movement import location_movement, read_location_from_json, show_current_location
from utils.map_maker import get_location_from_console, map_maker, search_location_in_dict

map=read_location_from_json()
current=map
current=location_movement(map)
current=location_movement(current)
show_current_location(current)

#from utils.map_maker import map_maker


#map_maker()



    
