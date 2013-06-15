#coding: utf-8
from panda3d.core import Point3

class MyObject:
    def __init__(self, lastPosition=Point3(0,0,0), animated=False, movementAnimation=None,minX=0,maxX=0,minY=0,maxY=0,model=None):
        self.lastPosition = lastPosition
        self.animated = animated
        self.movementAnimation = movementAnimation
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.model = model
        print model        
            
    '''Zwraca długość, szerokość i wysokość obiektu jako krotkę'''
    def calculateDimension(self):
        p1, p2 = self.model.getTightBounds()
        width = p2.getX() - p1.getX()
        height = p2.getY() - p1.getY()
        depth = p2.getZ() - p1.getZ()
        return (width, height, depth)
        
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
        return self.maxX
    
    def getMaxY(self):
        return self.maxY
    
    def getAnimated(self):
        return self.animated
    
    def getMovementAnimation(self):
        return self.movementAnimation
    
    def getLastPosition(self):
        print "LAST POSITION " + str(self.lastPosition)
        print "LP " + str(self.lastPosition.getX()) + " " + str(self.lastPosition.getY()) + " " + str(self.lastPosition.getZ())
        return self.lastPosition
        
    def getModel(self):
        return self.model 
        
        
