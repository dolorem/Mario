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
        self.keys = {";" : False, "," : False, "." : False, "a" : False, "o" : False, "e" : False, "page_up" : False, "page_down" : False}
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
        game.accept("page_up", self.keyHandler, ["page_up", True])
        game.accept("page_up-up", self.keyHandler, ["page_up", False])
        game.accept("page_down", self.keyHandler, ["page_down", True])
        game.accept("page_down-up", self.keyHandler, ["page_down", False])
        game.accept("q", sys.exit)
        game.accept("space", self.jump)
        self.angle = 0
        self.dangle = 0
        taskMgr.add(self.userInput, "User Input")
        
    '''Wywoływane gdy klawisz jest naciśnięty bądź puszczony, rejestruje to w słowniku klawiszy.'''
    def keyHandler(self, key, value):
        self.keys[key] = value    
        
    '''Zadanie reagujące na zdarzenia klawiatury.'''
    def userInput(self, task):
        self.world.getPlayer().setLastPosition(self.world.getPlayer().getModel().getPos())
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
        if self.keys["page_up"]:
            self.rotateVertically(0.1)
        if self.keys["page_down"]:
            self.rotateVertically(-0.1)
        self.world.getPlayer().getModel().setPos(self.world.getCamera().getPos())
        return task.cont

    def jump(self):
        self.world.getPlayer().jump()

    '''Obraca kamerę.'''
    def rotate(self, dangle):
        self.angle += dangle
        camera = self.game.camera
        camera.lookAt(sin(self.angle) + camera.getX(), cos(self.angle) + camera.getY(), self.world.getPlayer().getModel().getPos().getZ())
        
    #TODO: umożliwić poruszanie kamerą w płaszczyźnie YZ
    def rotateVertically(self, dangle):
        pass
    
    '''Przesuwa kamerę.'''
    def move(self, deltaAngle):
        self.world.getCamera().setX(self.world.getCamera().getX() + 1 * sin(self.angle + deltaAngle))
        self.world.getCamera().setY(self.world.getCamera().getY() + 1 * cos(self.angle + deltaAngle))
        #self.world.getSphereObjectDictionary()["CollisionHull1_"].setLastPosition(Point3(self.game.pb.getPos().getX(), self.game.pb.getPos().getY(), self.game.pb.getPos().getZ()))