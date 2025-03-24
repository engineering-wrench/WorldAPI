from .entities.player import Player
from .managers.entity_manager import EntityManager
import random

class World:
    def __init__(self):
        self.me = Player()
        self.entities = [Player() if i % 5 == 0 else Entity() for i in range(20)]
        self.entity = EntityManager(self.entities)

# Global world instance
world = World()