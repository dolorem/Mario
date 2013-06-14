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
		taskMgr.add(self.collisionDetection, "collision detection")
		#fromObject = base.camera.attachNewNode(CollisionNode('colNode'))
		#fromObject.node().addSolid(CollisionSphere(0, 0, 0, 1))
		self.pusher = CollisionHandlerPusher()
		
		
	
	def collisionDetection(self, task):
		return task.cont
	   
	def initCollisionSphere(self, obj, show=False, camera=False):
		'''if camera:
			center = obj.getPos()
			radius = 2
		else:
			 bounds = obj.getChild(0).getBounds()
			 center = bounds.getCenter()
			 radius = bounds.getRadius()
		collSphereStr = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
		self.collCount += 1
		cNode = CollisionNode(collSphereStr)
		cNode.addSolid(CollisionBox(center, radius, radius, radius))
		cNodepath = obj.attachNewNode(cNode)
		if show:
			cNodepath.show()
		#return (cNodepath, collSphereStr)'''
		if camera:
			center = obj.getPos()
			radius = 2
		else:
			 bounds = obj.getChild(0).getBounds()
			 center = bounds.getCenter()
			 radius = bounds.getRadius()
		collSphereStr = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
		self.collCount += 1
		cNode = CollisionNode(collSphereStr)
		cNode.addSolid(CollisionSphere(center, radius))
		cNodepath = obj.attachNewNode(cNode)
		if show:
			cNodepath.show()
		return (cNodepath, collSphereStr)
		'''Poniższy kod tworzy CollisionPolygony dla obiektu. Szkoda, że wykrywanie kolizji w ten sposób nie jest zaimplementowane w silniku...'''
		'''geomNodeCollection = obj.findAllMatches('**/+GeomNode')
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
			return (cNodepath, collisionString)'''
			  
	def foobar(self, s, t, game):
	   base.cTrav = CollisionTraverser()
	   self.collHandEvent = CollisionHandlerPusher()
	   self.collHandEvent.addInPattern('into-%in')
	   self.collHandEvent.addOutPattern('outof-%in')
	   self.collCount = 0
	   sColl = self.initCollisionSphere(s, True)
	   base.cTrav.addCollider(sColl[0], self.collHandEvent)
	   game.accept('into-' + sColl[1], self.collide3)
	   game.accept('outof-' + sColl[1], self.collide4)
	   print(sColl[1])
	   tColl = self.initCollisionSphere(t, True)
	   base.cTrav.addCollider(tColl[0], self.collHandEvent)
	   game.accept('into-' + tColl[1], self.collide)
	   game.accept('outof-' + tColl[1], self.collide2)
	   print(tColl[1])
	   print("WERT")
	   pusher = self.pusher
	   pusher.addCollider(sColl[0], s, base.drive.node())
	   self.collHandEvent.addCollider(sColl[0], s, base.drive.node())
	   self.collHandEvent.addCollider(tColl[0], t, base.drive.node())		
		
	def collide(self, collEntry):
		print("WERT: object has collided into another object")
		Sequence(Func(collEntry.getFromNodePath().getParent().setColor,
					  VBase4(1, 0, 0, 1)),
				 Wait(0.2),
				 Func(collEntry.getFromNodePath().getParent().setColor,
					  VBase4(0, 1, 0, 1)),
				 Wait(0.2),
				 Func(collEntry.getFromNodePath().getParent().setColor,
					  VBase4(1, 1, 1, 1))).start()
 
 
	def collide2(self, collEntry):
		print("WERT.: object is no longer colliding with another object")
 
	def collide3(self, collEntry):
		print("WERT2: object has collided into another object")
 
	def collide4(self, collEntry):
		print("WERT2: object is no longer colliding with another object")