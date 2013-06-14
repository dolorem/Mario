import sys

class UserInput:
    def __init__(self, game):
        self.game = game
        self.jumping = False
        self.jumpHeight = 0
        game.disableMouse()
        game.accept(".-repeat", self.move, [1.0, 0.0, 0.0])
        game.accept(";-repeat", self.move, [-1.0, 0.0, 0.0])
        game.accept(",-repeat", self.move, [0.0, 1.0, 0.0])
        game.accept("o-repeat", self.move, [0.0, -1.0, 0.0])
        game.accept(".", self.move, [1.0, 0.0, 0.0])
        game.accept(";", self.move, [-1.0, 0.0, 0.0])
        game.accept(",", self.move, [0.0, 1.0, 0.0])
        game.accept("o", self.move, [0.0, -1.0, 0.0])
        game.accept("a", self.rotate, [1])
        game.accept("e", self.rotate, [-1])
        game.accept("a-repeat", self.rotate, [1])
        game.accept("e-repeat", self.rotate, [-1])
        game.accept("escape", sys.exit)
        game.accept("q", sys.exit)
        game.accept("space", self.jump)
        self.angle = 0

    def jump(self):
        self.lastTime = 0
        self.jumpHeight = 0
        if self.jumping:
            return
        self.jumping = True        
        taskMgr.add(self.jumpTask, "Jump Task")

    def checkCollision(self):
        if self.jumpHeight >= 2.0:
            return True
        return False

    def jumpTask(self, task):
        if not self.checkCollision():
            dh = task.time - self.lastTime
            dh *= 2
            self.lastTime = task.time
            self.jumpHeight += dh
            if self.jumpHeight >= 1.0:
                self.move(0.0, 0.0, -dh)
            else:
                self.move(0.0, 0.0, dh)
            return task.cont
        self.jumping = False
        return task.done

    def rotate(self, dangle):
        self.angle += dangle
        self.game.camera.setHpr(self.angle, 0, 0)

    def move(self, x, y, z):
        self.game.camera.setX(self.game.camera.getX() + x)
        self.game.camera.setY(self.game.camera.getY() + y)
        self.game.camera.setZ(self.game.camera.getZ() + z)
