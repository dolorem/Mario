from CollisionDetection import CollisionDetection
from UserInput import UserInput
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3
from MyObject import MyObject
from World import World
from Player import Player

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
        self.pb = loader.loadModel("./infinity.x")
        self.pb.reparentTo(root)
        self.pb.setPos(7, 5, 2)
        text = loader.loadTexture("./Bg_Texture___wood_by_nortago.jpg")
        self.pb.setTexture(text)
        self.pbObject = MyObject(model=self.pb)
        self.pc = loader.loadModel("./model.x")
        self.pc.reparentTo(root)
        self.pc.setPos(0, 0, -2)
        gameObjects = [MyObject(model=self.pa, lastPosition=self.pa.getPos()), MyObject(model=self.pb, lastPosition=self.pb.getPos()), Player(model=self.camera, lastPosition=self.camera.getPos()), MyObject(model=self.pc, lastPosition=self.pc.getPos())]
        self.collisionDetection.prepareCollisionSpheres(gameObjects, self)
        
        
app = MyApp()
app.run()