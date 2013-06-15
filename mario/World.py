#coding: utf-8

class World:
    def __init__(self, models=[], objects=[], sphereObjectDictionary={}):
        self.models = models #lista wszystkich modeli
        self.objects = objects #lista instancji klasy MyObject 
        self.sphereObjectDictionary = sphereObjectDictionary #słownik w którym kluczami są nazwy sfer otaczających a wartościami instancje MyObject
        # wymagane do odwzorowań pomiędzy sferą kolidującą a obiektem w nią wpisanym
    
    def getModels(self):
        return self.models
    
    def setModels(self, models):
        self.models = models
        
    def getObjects(self):
        return self.objects
    
    def setObjects(self, objects):
        self.objects = objects
        
    def getSphereObjectDictionary(self):
        return self.sphereObjectDictionary
    
    def setSphereObjectDictionary(self, sphereObjectDictionary):
        self.sphereObjectDictionary = sphereObjectDictionary
        
    def addToSphereObjectDictionary(self, key, value):
        self.sphereObjectDictionary[key] = value
        
    def addToModels(self, value):
        self.models.append(value)
        
    def adToObjects(self, value):
        self.objects.append(value)
        
    def getObjectsFromCollisionEntry(self, collisionEntry):
        return (self.sphereObjectDictionary[str(collisionEntry.getFromNodePath().node()).split(" ")[1]], self.sphereObjectDictionary[str(collisionEntry.getIntoNodePath().node()).split(" ")[1]] )
    
    