from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #self.pa = loader.loadModel("/home/mateusz/Pulpit/PANDA/working.egg")
        #self.pa = loader.loadModel("/home/mateusz/Pulpit/untitled.x")
        #self.pa.setScale(1000, 1000, 1000)
        self.pa = Actor("./animation.x", {"foobar": "./animation.x",})
        self.pa.setPos(0, 5, 0)
        self.pa.reparentTo(self.render)
        #self.pa.show()
        self.pa.loop("foobar")
        print self.pa.getPos()
        self.accept("a", self.keyFunction)
        
    def keyFunction(self):
        print "a"
        self.pa.stop()
        print self.pa.node()
        self.pa.lookAt(5, 5, 0)
        self.pa.loop("foobar")
        
        
app = MyApp()
app.run()