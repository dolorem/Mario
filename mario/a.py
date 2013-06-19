#coding:utf-8
from CollisionDetection import CollisionDetection
from UserInput import UserInput
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, Texture, VBase4
from MyObject import MyObject
from World import World
from Player import Player
from direct.interval.IntervalGlobal import Sequence
import time

class MyApp(ShowBase):
    def __init__(self, username, time):
        ShowBase.__init__(self)
        self.intervals = 0
        root = render.attachNewNode("Root")
        root.setPos(0.0, 0.0, 0.0)
        self.root = root
        world = World(player = Player(), camera = self.camera)
        userInput = UserInput(self, world)
        self.collisionDetection = CollisionDetection(world)
        gameObjects = [Player(model=self.camera, lastPosition=self.camera.getPos())]
        gameObjects.extend(self.loadMap("map"))
        self.collisionDetection.prepareCollisionSpheres(gameObjects, self)
        world.theme = loader.loadSfx("./sounds/theme.mp3")
        world.theme.play()
        world.theme.setLoop(True)
        world.death = loader.loadSfx("./sounds/death.mp3")
        world.username = username
        world.time = time
        
    def loadMap(self, mapName):
        objects = []
        f = open(mapName, 'r')
        for line in f:
            arr = line.split(" ")
            print arr
            obj = MyObject()
            pos = Point3(0, 0, 0)
            obj.setModel(loader.loadModel("./" + arr[0] + ".x"))
            obj.getModel().reparentTo(self.root)
            pos.setX(float(arr[2]))
            pos.setY(float(arr[3]))
            pos.setZ(float(arr[4])) 
            obj.setLastPosition(pos)
            obj.getModel().setPos(pos)
            if arr[1] == "0":
                obj.setAnimated(False)
            else:
                obj.setAnimated(True)
                arr[5], arr[6] = float(arr[5]), float(arr[6])
                obj.setMinX(obj.getPos().getX() - (arr[5] / 2))
                obj.setMaxX(obj.getPos().getX() + (arr[5] / 2))
                obj.setMinY(obj.getPos().getY() - (arr[6] / 2))
                obj.setMaxY(obj.getPos().getY() + (arr[6] / 2))
                obj.getMinX()
                time = 1
                rotationTime = 2
                obj.getModel().setPos(Point3(obj.getModel().getX(), obj.getModel().getY(), obj.getModel().getZ()))
                p1 = Point3(obj.getMinX(), obj.getMinY(), obj.getModel().getZ())
                p2 = Point3(obj.getMinX(), obj.getMaxY(), obj.getModel().getZ())
                p3 = Point3(obj.getMaxX(), obj.getMaxY(), obj.getModel().getZ())
                p4 = Point3(obj.getMaxX(), obj.getMinY(), obj.getModel().getZ())
                pp1 = obj.getModel().posInterval(time, p2, startPos=p1)
                pp2 = obj.getModel().posInterval(time, p3, startPos=p2)
                pp3 = obj.getModel().posInterval(time, p4, startPos=p3)
                pp4 = obj.getModel().posInterval(time, p1, startPos=p4)
                ph1 = obj.getModel().hprInterval(rotationTime, Point3(-90, 0, 0), startHpr=Point3(0, 0, 0))
                ph2 = obj.getModel().hprInterval(rotationTime, Point3(-180, 0, 0), startHpr=Point3(-90, 0, 0))
                ph3 = obj.getModel().hprInterval(rotationTime, Point3(-270, 0, 0), startHpr=Point3(-180, 0, 0))
                ph5 = obj.getModel().hprInterval(0, Point3(90, 0, 0), startHpr=Point3(-270, 0, 0))
                ph4 = obj.getModel().hprInterval(rotationTime, Point3(0, 0, 0), startHpr=Point3(90, 0, 0))
                pp = Sequence(pp1, ph1, pp2, ph2, pp3, ph3, pp4, ph4, name="movement" + str(self.intervals))
                pp.loop()
                self.intervals += 1
            objects.append(obj)
        return objects
        
time = time.time()
username = raw_input("Podaj nazwę użytkownika.\n") 
app = MyApp(username, time)
app.run()
