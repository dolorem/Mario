from CollisionDetection import CollisionDetection
from UserInput import UserInput
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase

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
        print self.pa.node()
        print self.camera.node()
        userInput = UserInput(self)
        collisionDetection = CollisionDetection()
        #collisionDetection.initCollisionSphere(self.pa, True)
        #collisionDetection.initCollisionSphere(self.camera, True, True)
        collisionDetection.foobar(self.pa, self.camera, self)
        
app = MyApp()
app.run()