import random

class Entity:
    def __init__(self):
        self._pos = (
            random.randint(-1000, 1000),
            random.randint(-1000, 1000),
            random.randint(-1000, 1000)
        )
        self._rotation = (0, 0, 0)
    
    @property
    def getPos(self):
        return self._pos
    
    def setPos(self, pos):
        self._pos = pos
    
    @property
    def getRotation(self):
        return self._rotation
    
    def setRotation(self, rotation):
        self._rotation = rotation