class World:
    def __init__(self, models=[], objects=[], sphereObjectDictionary={}):
        self.models = models
        self.objects = objects
        self.sphereObjectDictionary = sphereObjectDictionary
    
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
    
    