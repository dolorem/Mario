#coding: utf-8
from panda3d.core import CollisionNode, CollisionTraverser, CollisionSphere, \
	CollisionHandlerPusher, CollisionHandlerEvent, CollisionPolygon, CollisionBox, CollisionTube
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from panda3d.core import CollisionTraverser, CollisionHandlerEvent
from panda3d.core import CollisionNode, CollisionSphere
from panda3d.core import VBase4
from panda3d.core import SocketStream, GeomVertexReader
from sys import stdout

class CollisionDetection():
	def __init__(self):
		self.collCount = 0
		self.dict = {}
		#taskMgr.add(self.collisionDetection, "collision detection")
	
	#def collisionDetection(self, task):
	#	return task.cont
	
	def initCollisionSphere(self, obj, show=False, camera=False):
		if camera:
			center = obj.getPos()
			radius = 2
		else:
			 bounds = obj.getChild(0).getBounds()
			 center = bounds.getCenter()
			 radius = bounds.getRadius()
		collSphereStr = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
		print collSphereStr
		self.collCount += 1
		cNode = CollisionNode(collSphereStr)
		cNode.addSolid(CollisionSphere(center, radius))
		cNodepath = obj.attachNewNode(cNode)
		if show:
			cNodepath.show()
		return (cNodepath, collSphereStr)
		
			  
	def prepareCollisionSpheres(self, gameObjects, game):
		self.gameObjects = gameObjects
		base.cTrav = CollisionTraverser()
		self.collHandEvent = CollisionHandlerEvent()
		self.collHandEvent.addInPattern('into-%in')
		self.collHandEvent.addOutPattern('outof-%in')
		self.collCount = 0
		for myObject in gameObjects:
			sColl = self.initCollisionSphere(myObject.getModel(), True)
			self.dict[sColl[1]] = myObject
			base.cTrav.addCollider(sColl[0], self.collHandEvent)
			game.accept('into-' + sColl[1], self.collideIn)
			game.accept('outof-' + sColl[1], self.collideOut)
			
		
	def collideIn(self, collEntry):
		print("Object has collided into another object")
		self.verifyCollision(collEntry)
 
	def collideOut(self, collEntry):
		pass
	#	print("Object is no longer colliding with another object")
	#	self.verifyCollision(collEntry)
		
	def baz(self, foo):
		model = foo.getModel()
		model.setX(foo.getLastPosition().getX())
		model.setY(foo.getLastPosition().getY())
		print "(" + str(model.getY()) + " -> " + str(foo.getLastPosition().getY()) + ")"
		model.setZ(foo.getLastPosition().getZ())
		
	def verifyCollision(self, collEntry):
		#print "From " + str(collEntry.getFromNodePath().node()) + " to " + str(collEntry.getIntoNodePath().node())
		#print str(self.dict[str(collEntry.getFromNodePath().node()).split(" ")[1]])
		print collEntry	
		second = self.dict[str(collEntry.getFromNodePath().node()).split(" ")[1]]
		first = self.dict[str(collEntry.getIntoNodePath().node()).split(" ")[1]]
		#second.getModel().setPos(second.getLastPosition())
		#first.getModel().setPos(first.getLastPosition())
		#second.getModel().setX(3.6)
		self.baz(first)
		self.baz(second)
		print "NEW POSITIONS - " + str(first.getModel().getPos()) + " " + str(second.getModel().getPos())
		#print "MOVING TO " + str(first.getLastPosition())
		#print second.getModel()
		print "FIRST - " + str(first.getModel()) + " SECOND " + str(second.getModel())
		
		
	def initCollisionPolygons(self, obj, show=False):
		'''Poniższy kod tworzy CollisionPolygony dla obiektu. Szkoda, że wykrywanie kolizji w ten sposób nie jest zaimplementowane w silniku...'''
		geomNodeCollection = obj.findAllMatches('**/+GeomNode')
		for nodePath in geomNodeCollection:
			geomNode = nodePath.node()
			collisionString = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
			self.collCount += 1
			cNode = CollisionNode(collisionString)
			for i in range(geomNode.getNumGeoms()):
				#cNode.addSolid(geomNode.getGeom(j).getBounds())
				geom = geomNode.getGeom(i)
				state = geomNode.getGeomState(i)
				print geom
				print state
				print "//"
				vdata = geom.getVertexData()
				print vdata #TU JEST GIT
				forPolygons = []
				for j in range(geom.getNumPrimitives()):
					prim = geom.getPrimitive(j)
					print "prim - " + str(prim)
					vertex = GeomVertexReader(vdata, 'vertex')
					prim = prim.decompose()
					for p in range(prim.getNumPrimitives()):
						s = prim.getPrimitiveStart(p)
						e = prim.getPrimitiveEnd(p)
						forPolygon = []
						for k in range(s, e):
							vi = prim.getVertex(k)
							vertex.setRow(vi)
							v = vertex.getData3f()
							print "prim %s has vertex %s: %s" % (p, vi, repr(v))
							forPolygon.append(v)
						forPolygons.append(forPolygon)
						#print "forPolygon - " + str(forPolygon)	
						#print "AAA"
						#if len(forPolygon) == 4:
						#	collisionPolygon = CollisionPolygon(forPolygon[0], forPolygon[1], forPolygon[2], forPolygon[3]) 
						#	cNode.addSolid(collisionPolygon)	
						#	print "AAA"	
			print "OVERALL - " + str(len(forPolygons))
			for p in forPolygons:
				if len(p) == 3:
								print "PROCESSING"
								collisionPolygon = CollisionPolygon(forPolygon[0], forPolygon[1], forPolygon[2]) 
								cNode.addSolid(collisionPolygon)
								print "PROCESSED"
				else:
					print "DAMMIT " + str(len(p))
			cNodepath = obj.attachNewNode(cNode)
			if show:
				cNodepath.show()
			return (cNodepath, collisionString)