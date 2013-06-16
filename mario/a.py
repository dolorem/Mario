from CollisionDetection import CollisionDetection
from UserInput import UserInput
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3
from MyObject import MyObject
from World import World
from Player import Player
from CameraObject import CameraObject

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        root = render.attachNewNode("Root")
        root.setPos(0.0, 0.0, 0.0)
        self.root = root
        self.pa = Actor("./animation.x", {"foobar": "./animation.x",})
        self.pa.setPos(0, 5, 0)
        self.pa.reparentTo(root)
        self.pa.loop("foobar");
        world = World(player = Player(), camera = self.camera)        
        userInput = UserInput(self, world)
        self.collisionDetection = CollisionDetection(world)
        self.pb = loader.loadModel("./model.x")
        self.pb.reparentTo(root)
        self.pb.setPos(7, 5, 0)
        self.pbObject = MyObject(model=self.pb)
        gameObjects = [MyObject(model=self.pa, lastPosition=self.pa.getPos()), MyObject(model=self.pb, lastPosition=self.pb.getPos()), Player(model=self.camera, lastPosition=self.camera.getPos())]
        self.collisionDetection.prepareCollisionSpheres(gameObjects, self)
        
        
app = MyApp()
app.run()