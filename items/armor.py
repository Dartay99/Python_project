from dataclasses import dataclass

from items.item import Item

@dataclass
class Armor(Item):
    defense:int 
    #durability:int