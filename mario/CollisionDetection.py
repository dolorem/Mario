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
	def __init__(self, world):
		self.world = world #Instancja klasy World
		self.taskEvents = set() #zbiór zawierający krotki obiektów zakwalifikowanych jako możliwie kolidujące przez sfery otaczające
		self.collCount = 0 #liczba utworzonych sfer otaczających, istotna dla zachowania unikatowej nazwy
		taskMgr.add(self.collisionDetection, "collision detection")
		
	'''Usuwa ze zbioru możliwych kolizji krotkę zawierającą dwa obiekty, których sfery otaczające kolidują ze sobą.'''
	def addCollidingObjects(self, obj1, obj2):
		self.taskEvents.add((obj1, obj2))
		
	'''Dodaje do zbioru możliwych kolizji krotkę zawierającą dwa obiekty, których sfery otaczające kolidują ze sobą.'''
	def removeCollidingObjects(self, obj1, obj2):
		self.taskEvents.remove((obj1, obj2))
	
	'''Zadanie przeglądające wszystkie pary obiektów zakwalifikowane do sprawdzenia za pomocą prostopadłościanów przez sfery.'''
	def collisionDetection(self, task):
		for event in self.taskEvents:
			self.verifyCollision(event)
		return task.cont
	
	'''Inicjuje sferę otaczającą dla obiektu.'''
	def initCollisionSphere(self, obj, show=False):
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
		
	'''Tworzy sfery otaczające dla każdego obiektu z zadanej tablicy gameObjects. I ustawie je w odpowiednim miejscu grafu. Dodaje relację sfera-obiekt w słowniku.'''	
	def prepareCollisionSpheres(self, gameObjects, game):
		self.gameObjects = gameObjects
		base.cTrav = CollisionTraverser()
		self.collHandEvent = CollisionHandlerEvent()
		self.collHandEvent.addInPattern('into-%in')
		self.collHandEvent.addOutPattern('outof-%in')
		self.collCount = 0
		for myObject in gameObjects:
			sColl = self.initCollisionSphere(myObject.getModel(), True)
			self.world.getSphereObjectDictionary()[sColl[1]] = myObject
			base.cTrav.addCollider(sColl[0], self.collHandEvent)
			game.accept('into-' + sColl[1], self.collideIn)
			game.accept('outof-' + sColl[1], self.collideOut)
		
	'''Wywoływane przez Pandę gdy obiekty zaczną kolidować, dodaje je do listy obiektów do sprawdzenia i ewentualnego przywrócenia.'''
	def collideIn(self, collEntry):
		first, second = self.world.getObjectsFromCollisionEntry(collEntry)
		self.addCollidingObjects(first, second)

	'''Wywoływane przez Pandę gdy obiekty przestaną kolidować, usuwa je z listy obiektów do sprawdzenia i ewentualnego przywrócenia.'''
	def collideOut(self, collEntry):
		first, second = self.world.getObjectsFromCollisionEntry(collEntry)
		self.removeCollidingObjects(first, second)
			
	'''Cofa obiekt do poprzedniego położenia.'''
	def revertPosition(self, foo):
		model = foo.getModel()
		model.setX(foo.getLastPosition().getX())
		model.setY(foo.getLastPosition().getY())
		model.setZ(foo.getLastPosition().getZ())
		
	'''Sprawdza czy kolizja rzeczywiście nastąpiła, jeśli tak, cofa obiekty do poprzedniego położenia.'''
	def verifyCollision(self, collisionEvent):
		obj1, obj2 = collisionEvent[0], collisionEvent[1]
		if obj1.isColliding(obj2):
			self.revertPosition(obj1)
			self.revertPosition(obj2)
				
	def initCollisionPolygons(self, obj, show=False):
		'''Poniższy kod tworzy CollisionPolygony dla obiektu. Szkoda, że wykrywanie kolizji w ten sposób nie jest zaimplementowane w silniku...'''
		geomNodeCollection = obj.findAllMatches('**/+GeomNode')
		for nodePath in geomNodeCollection:
			geomNode = nodePath.node()
			collisionString = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
			self.collCount += 1
			cNode = CollisionNode(collisionString)
			for i in range(geomNode.getNumGeoms()):
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