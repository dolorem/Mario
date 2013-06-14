from panda3d.core import CollisionNode, CollisionTraverser, CollisionSphere, \
	CollisionHandlerPusher

class CollisionDetection:
    def __init__(self, game):
        taskMgr.add(self.collisionDetection, "collision detection")
        fromObject = base.camera.attachNewNode(CollisionNode('colNode'))
        fromObject.node().addSolid(CollisionSphere(0, 0, 0, 1))
        pusher = CollisionHandlerPusher()
        #pusher.addCollider(fromObject, game.camera, game.camera.drive.node())

    def collisionDetection(self, task):
        
        return task.cont