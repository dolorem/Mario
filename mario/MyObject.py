#coding: utf-8
from panda3d.core import Point3

class MyObject:
    def __init__(self, lastPosition = Point3(0, 0, 0), animated = False, movementAnimation = None, minX = 0, maxX = 0, minY = 0, maxY = 0, model = None):
        self.lastPosition = lastPosition
        self.animated = animated
        self.movementAnimation = movementAnimation
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.model = model
        
    def getPos(self):
        return self.model.getPos()   
        
    def avg(self, a, b):
        return (a + b) / 2
            
    '''Zwraca długość, szerokość, wysokość i środek obiektu jako krotkę.'''
    def calculateDimension(self):
        p1, p2 = self.model.getTightBounds()
        width = abs(p2.getX() - p1.getX())
        height = abs(p2.getY() - p1.getY())
        depth = abs(p2.getZ() - p1.getZ())
        center = Point3(self.avg(p1.getX(), p2.getX()), self.avg(p1.getY(), p2.getY()), self.avg(p1.getZ(), p2.getZ()))
        return (width, height, depth, center) 
    
    '''Sprawdza kolizję bazując na prostopadłościanach otaczających.'''
    def isColliding(self, obj2, camera = False):
        colliding = True
        dimension1 = self.calculateDimension()
        dimension2 = obj2.calculateDimension()
        center1 = dimension1[3]
        center2 = dimension2[3]
        colliding = colliding and (abs(center1.getX() - center2.getX()) <= (dimension1[0] + dimension2[0]) / 2)
        colliding = colliding and (abs(center1.getY() - center2.getY()) <= (dimension1[1] + dimension2[1]) / 2)
        colliding = colliding and (abs(center1.getZ() - center2.getZ()) <= (dimension1[2] + dimension2[2]) / 2)
        return colliding
        
    def isCollidingWithCamera(self, cameraPosition, width, height, depth):
        colliding = True
        dimension1 = self.calculateDimension()
        center1 = dimension1[3]
        colliding = colliding and (abs(center1.getX() - cameraPosition.getX()) <= (dimension1[0] + width) / 2)
        colliding = colliding and (abs(center1.getY() - cameraPosition.getY()) <= (dimension1[1] + height) / 2)
        colliding = colliding and (abs(center1.getZ() - cameraPosition.getZ()) <= (dimension1[2] + depth) / 2)
        return colliding
        
    def setMinX(self, minX):
        self.minX = minX
        
    def setMaxX(self, maxX):
        self.maxX = maxX
        
    def setMinY(self, minY):
        self.minY = minY
        
    def setMaxY(self, maxY):
        self.maxY = maxY
        
    def setAnimated(self, animated):
        self.animated = animated
        
    def setMovementAnimation(self, movementAnimation):
        self.movementAnimation = movementAnimation
    
    def setLastPosition(self, lastPositiona):
        self.lastPosition = lastPositiona
        
    def setModel(self, model):
        self.model = model
        
    def getMinX(self):
        return self.minX
    
    def getMaxX(self):
        return self.maxX
    
    def getMinY(self):
        return self.minY
    
    def getMaxY(self):
        return self.maxY
    
    def getAnimated(self):
        return self.animated
    
    def getMovementAnimation(self):
        return self.movementAnimation
    
    def getLastPosition(self):
        return self.lastPosition
        
    def getModel(self):
        return self.model 
        
        
