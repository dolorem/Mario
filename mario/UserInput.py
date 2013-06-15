#coding: utf-8
import sys
from panda3d.core import VBase3, Point3
from math import sin, cos, pi
from World import World

class UserInput:
    def __init__(self, game, world):
        self.game = game
        self.world = world
        self.jumping = False 
        self.jumpHeight = 0
        self.keys = {";" : False, "," : False, "." : False, "a" : False, "o" : False, "e" : False}
        game.disableMouse()
        game.accept(";", self.keyHandler, [";", True])
        game.accept(";-up", self.keyHandler, [";", False])
        game.accept(",", self.keyHandler, [",", True])
        game.accept(",-up", self.keyHandler, [",", False])
        game.accept(".", self.keyHandler, [".", True])
        game.accept(".-up", self.keyHandler, [".", False])
        game.accept("a", self.keyHandler, ["a", True])
        game.accept("a-up", self.keyHandler, ["a", False])
        game.accept("o", self.keyHandler, ["o", True])
        game.accept("o-up", self.keyHandler, ["o", False])
        game.accept("e", self.keyHandler, ["e", True])
        game.accept("e-up", self.keyHandler, ["e", False])
        game.accept("q", sys.exit)
        self.angle = 0
        taskMgr.add(self.userInput, "User Input")
        
    '''Wywoływane gdy klawisz jest naciśnięty bądź puszczony, rejestruje to w słowniku klawiszy.'''
    def keyHandler(self, key, value):
        self.keys[key] = value    
        
    '''Zadanie reagujące na zdarzenia klawiatury.'''
    def userInput(self, task):
        if self.keys[";"]:
            self.move(pi * 1.5)
        if self.keys[","]:
            self.move(0.0)
        if self.keys["."]:
            self.move(pi * 0.5)
        if self.keys["a"]:
            self.rotate(-pi / 180.0)
        if self.keys["o"]:
            self.move(pi)
        if self.keys["e"]:
            self.rotate(pi / 180.0)
        return task.cont

    def jump(self):
        self.lastTime = 0
        self.jumpHeight = 0
        if self.jumping:
            return
        self.jumping = True        
        taskMgr.add(self.jumpTask, "Jump Task")

    def checkCollision(self):
        if self.jumpHeight >= 2.0:
            return True
        return False
#TODO: zamienić move() na skakanie i poruszanie się do gory, skakanie powoduje TypeError() - za dużo argumentów jest przekazywanych do move() 
    def jumpTask(self, task):
        if not self.checkCollision():
            dh = task.time - self.lastTime
            dh *= 2
            self.lastTime = task.time
            self.jumpHeight += dh
            if self.jumpHeight >= 1.0:
                self.move(0.0, 0.0, -dh)
            else:
                self.move(0.0, 0.0, dh)
            return task.cont
        self.jumping = False
        return task.done

    '''Obraca kamerę.'''
    def rotate(self, dangle):
        self.angle += dangle
        camera = self.game.camera
        camera.lookAt(sin(self.angle) + camera.getX(), cos(self.angle) + camera.getY(), 0)
    
    '''Przesuwa kamerę.'''
    #TODO: detekcja kolizji kamery z otoczeniem
    def move(self, deltaAngle):
        self.game.camera.setX(self.game.camera.getX() + 0.2 * sin(self.angle + deltaAngle))
        self.game.camera.setY(self.game.camera.getY() + 0.2 * cos(self.angle + deltaAngle))
        self.world.getSphereObjectDictionary()["CollisionHull1_"].setLastPosition(Point3(self.game.pb.getPos().getX(), self.game.pb.getPos().getY(), self.game.pb.getPos().getZ()))
        self.game.pb.setX(self.game.pb.getX() - 0.2)
        