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
        game.disableMouse()
        game.accept(".-repeat", self.move, [pi * 0.5])
        game.accept(";-repeat", self.move, [pi * 1.5])
        game.accept(",-repeat", self.move, [0.0])
        game.accept("o-repeat", self.move, [pi])
        game.accept(".", self.move, [pi * 0.5])
        game.accept(";", self.move, [pi * 1.5])
        game.accept(",", self.move, [0.0])
        game.accept("o", self.move, [pi])
        game.accept("a", self.rotate, [-pi / 180.0])
        game.accept("e", self.rotate, [pi / 180.0])
        game.accept("a-repeat", self.rotate, [-pi / 180.0])
        game.accept("e-repeat", self.rotate, [pi / 180.0])
        game.accept("escape", sys.exit)
        game.accept("q", sys.exit)
        game.accept("space", self.jump)
        self.angle = 0

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
#TODO: zamienic move() na skakanie i poruszanie sie do gory, skakanie powoduje TypeError() - za duzo argumentow jest przekazywanych do move() 
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

    def rotate(self, dangle):
        self.angle += dangle
        camera = self.game.camera
        camera.lookAt(sin(self.angle) + camera.getX(), cos(self.angle) + camera.getY(), 0)
    
    def move(self, deltaAngle):
        self.game.camera.setX(self.game.camera.getX() + 0.2 * sin(self.angle + deltaAngle))
        self.game.camera.setY(self.game.camera.getY() + 0.2 * cos(self.angle + deltaAngle))
        self.world.getSphereObjectDictionary()["CollisionHull1_"].setLastPosition(Point3(self.game.pb.getPos().getX(), self.game.pb.getPos().getY(), self.game.pb.getPos().getZ()))
        self.game.pb.setX(self.game.pb.getX() - 0.2)
        