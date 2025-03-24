class WorldAPI:
    class WorldSpace:
        def __init__(self):
            self.earth = None  # Инициализируем как None

        def get_earth(self):
            if self.earth is None:
                self.earth = WorldAPI.Earth()  # Создаем экземпляр только при первом обращении
            return self.earth

    class Earth:
        def __init__(self):
            self.entity = WorldAPI.Entity()  # Используем полное имя класса
    
    class Entity:
        def __init__(self):
            self.human = WorldAPI.Human()  # Используем полное имя класса
    
    class Human:
        def __init__(self):
            self.man = WorldAPI.Man()  # Используем полное имя класса
    
    class Man:
        def __init__(self):
            self.person = WorldAPI.Person()  # Используем полное имя класса
    
    class Person:
        def __init__(self):
            self.people = []
        
        def add_person(self, name):
            self.people.append(self.Individual(name))
        
        def findByName(self, name):
            return next((p for p in self.people if p.name == name), None)
        
        class Individual:
            def __init__(self, name):
                self.name = name
                self.age = None
                self.gender = None
            
            def set_age(self, age):
                self.age = age
                return self
            
            def set_gender(self, gender):
                self.gender = gender
                return self

    # Инициализация worldSpace
    worldSpace = WorldSpace()

# Пример использования
if __name__ == "__main__":
    WorldAPI.worldSpace.get_earth().entity.human.man.person.add_person("Дима")
    
    misha = WorldAPI.worldSpace.get_earth().entity.human.man.person.findByName("Дима")
    
    if misha:
        print(f"Найден: {misha.name}")
        misha.set_age(25).set_gender("male")
        print(f"Возраст: {misha.age}, Пол: {misha.gender}")
    else:
        print("Персонаж не найден")