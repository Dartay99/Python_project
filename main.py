#from actors.enemy import Enemy
#from actors.player import Player
#from events.fight import Fight

#from items.storage import Storage

from utils.game_exceptions import ExitGame
from utils.location_movement import location_movement, read_location_from_json

def runGame(map):
    current=map
    while True:
        current=location_movement(map,current)

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

map=read_location_from_json()

try:
    runGame(map)
except ExitGame:
    print("Goodbye!")



    
