from .base_entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.inventory = []
    
    def addToInventory(self, item):
        self.inventory.append(item)
    
    def getInventory(self):
        return self.inventory.copy()