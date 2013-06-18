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
        #self.pa = Actor("./animation.x", {"foobar": "./animation.x",})
        '''self.pa = loader.loadModel("./snake.x")
        self.pa.setPos(0, 5, 3)
        self.pa.reparentTo(root)
        #self.pa.loop("foobar");
        self.pb = loader.loadModel("./infinity.x")
        self.pb.reparentTo(root)
        self.pb.setPos(7, 5, 2)
        text = loader.loadTexture("Bg_Texture___wood_by_nortago.jpg")
        text.setWrapU(Texture.WMBorderColor)
        text.setWrapV(Texture.WMBorderColor)
        text.setBorderColor(VBase4(0.4, 0.5, 1, 1))
        print self.pa.getMaterial()
        print self.pa.getColor()
        self.pa.setTexture(text, 1)
        self.pbObject = MyObject(model=self.pb)
        self.pc = loader.loadModel("./model.x")
        self.pc.reparentTo(root)
        self.pc.setPos(0, 0, -2)'''
        #gameObjects = [MyObject(model=self.pa, lastPosition=self.pa.getPos(), animated=True), MyObject(model=self.pb, lastPosition=self.pb.getPos()), Player(model=self.camera, lastPosition=self.camera.getPos()), MyObject(model=self.pc, lastPosition=self.pc.getPos())]
        gameObjects = [Player(model=self.camera, lastPosition=self.camera.getPos())]
        gameObjects.extend(self.loadMap("map"))
        '''p1 = self.pa.posInterval(2, Point3(0, 5, 5), startPos=Point3(0, 5, 3))
        p2 = self.pa.posInterval(2, Point3(0, 5 , 3), startPos=Point3(0, 5, 5))
        pp = Sequence(p1, p2, name="pp")
        pp.loop()'''
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
                print obj.getMaxX()
                print obj.getMinY()
                print obj.getMaxY()
                time = 1
                rotationTime = 2
                print "Z=" + str(obj.getModel().getZ())
                obj.getModel().setPos(Point3(obj.getModel().getX(), obj.getModel().getY(), obj.getModel().getZ()))
                #p0 = Point3(obj.getModel().getX(), obj.getModel().getY(), obj.getModel().getZ())
                p1 = Point3(obj.getMinX(), obj.getMinY(), obj.getModel().getZ())
                p2 = Point3(obj.getMinX(), obj.getMaxY(), obj.getModel().getZ())
                p3 = Point3(obj.getMaxX(), obj.getMaxY(), obj.getModel().getZ())
                p4 = Point3(obj.getMaxX(), obj.getMinY(), obj.getModel().getZ())
                #pp0 = obj.getModel().posInterval(time, p1, startPos=p0)
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