import random

class EntityManager:
    def __init__(self, entities):
        self.entities = entities
    
    def selectRandom(self):
        return random.choice(self.entities)
    
    def filterByType(self, entity_type):
        return [e for e in self.entities if isinstance(e, entity_type)]
    
    def getNearby(self, position, radius=10):
        return [e for e in self.entities 
                if sum((a - b)**2 for a, b in zip(e.getPos, position)) <= radius**2]