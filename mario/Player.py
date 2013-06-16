#coding: utf-8
from panda3d.core import Point3
from MyObject import MyObject
    
class Player(MyObject):
    def __init__(self, lifes = 0, position = Point3(0, 0, 0), lastPosition = Point3(0, 0, 0), velocity = 1, jumpVelocity = 1, jumpHeight = 1, points = 0, model = None):
        MyObject.__init__(self, lastPosition = lastPosition, model = model)
        self.lifes = lifes
        self.position = position
        self.lastPosition = lastPosition
        self.velocity = velocity
        self.jumpVelocity = jumpVelocity
        self.jumpHeight = jumpHeight
        self.points = points
        
    '''Zwraca długość, szerokość, wysokość i środek obiektu jako krotkę.'''
    def calculateDimension(self):
        return (4, 4, 4, self.model.getPos()) 
        
    '''Dodaje punkty graczowi.'''
    def addPoints(self, amount):
        self.points += amount
        
    '''Usuwa punkty.'''
    def removePoints(self, amount):
        self.points -= amount 
        
    '''Dodaje życia.'''
    def addLifes(self, amount):
        self.lifes += amount
    
    '''Usuwa życia.'''
    def removeLifes(self, amount):
        self.lifes -= 1
    
    def getPoints(self):
        return self.points
    
    def setPoints(self, points):
        self.points = points

    def getLifes(self):
        return self.lifes

    def getPosition(self):
        return self.position

    def getLastPosition(self):
        return self.lastPosition

    def getVelocity(self):
        return self.velocity

    def getJumpVelocity(self):
        return self.jumpVelocity

    def getJumpHeight(self):
        return self.jumpHeight

    def setLifes(self, value):
        self.lifes = value

    def setPosition(self, value):
        self.position = value

    def setLastPosition(self, value):
        self.lastPosition = value

    def setVelocity(self, value):
        self.velocity = value

    def setJumpVelocity(self, value):
        self.jumpVelocity = value

    def setJumpHeight(self, value):
        self.jumpHeight = value   