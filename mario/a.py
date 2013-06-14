from CollisionDetection import CollisionDetection
from UserInput import UserInput
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3

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
        #collisionDetection.foobar(self.pa, self.camera, self)
        self.pb = loader.loadModel("./model.x")
        self.pb.reparentTo(root)
        self.pb.setPos(7, 5, 0)
        #self.pb.posInterval(3.0, Point3(5, 5, 0)).start()
        #self.pb.posInterval(3.0, Point3(0, 5, 0))
        collisionDetection.foobar(self.pa, self.pb, self)
        print self.pa
        print "###############"
        for i in self.pa.getChildren():
            print i
        print "###############"
        for i in self.pa.findAllVertexColumns():
            print i
        print "###############"
        geomNodeCollection = self.pa.findAllMatches('**/+GeomNode')
        for nodePath in geomNodeCollection:
            geomNode = nodePath.node()
            for j in range(geomNode.getNumGeoms()):
                print geomNode.getGeom(j).getBounds()
        
app = MyApp()
app.run()