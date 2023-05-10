from dataclasses import dataclass
from items.effect import Effect

from items.item import Item

@dataclass
class Potion(Item): #title не нужен, потому что potion наследуется от item
    duration:int
    effects: list[Effect]
    