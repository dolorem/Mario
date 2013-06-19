#coding: utf-8
from Player import Player
import time
import sys

class World:
    def __init__(self, models = [], objects = [], sphereObjectDictionary = {}, player = None, camera = None):
        self.models = models #lista wszystkich modeli
        self.objects = objects #lista instancji klasy MyObject 
        self.sphereObjectDictionary = sphereObjectDictionary #słownik w którym kluczami są nazwy sfer otaczających a wartościami instancje MyObject
        # wymagane do odwzorowań pomiędzy sferą kolidującą a obiektem w nią wpisanym
        self.player = player
        self.camera= camera
 
    def end(self):
        f = open("results", "a")
        f.write(self.username + " " + str(self.getTime()) + " " + str(self.getPlayer().deaths) + "\n")
        print self.username + " " + str(self.getTime()) + " " + str(self.getPlayer().deaths) + "\n"
        f.close()
        sys.exit()
        
    def getTime(self):
        return time.time() - self.time            
        
    def addAnimated(self, value):
        self.animated.append(value)
        
    def getCamera(self):
        return self.camera
    
    def setCamera(self, camera):
        self.camera = camera
    
    def getPlayer(self):
        return self.getSphereObjectDictionary()['CollisionHull0_camera']
    
    def setPlayer(self, player):
        self.player = player
    
    def getModels(self):
        return self.models
    
    def setModels(self, models):
        self.models = models
        
    def getObjects(self):
        obj = []
        for key in self.sphereObjectDictionary:
            obj.append(self.sphereObjectDictionary[key])
        return obj
    
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
    
    
