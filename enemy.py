from PyQt6.QtCore import Qt, QObject, QPointF, QTimer, QLineF
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
import math

class Enemy(QGraphicsPixmapItem, QObject): # wrong order endes in weird bug, why does QGraphicsPixmapItem have to be first?
    def __init__(self, parent = None):
        super().__init__(parent)

        # set graphics
        self.setPixmap(QPixmap(":/images/images/enemy.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))

        # set points
        self.points = [QPointF(200, 200), QPointF(400, 150), QPointF(500, 300)]
        self.point_index = 0
        self.dest = self.points[self.point_index]

        # connect timer to move_forward
        self.timer = QTimer()

        self.timer.timeout.connect(self.move_forward)
        self.timer.start(150)
        
    # move enemy forward at current angle
    def move_forward(self):
        # if close enough to dest, go to next dest
        line = QLineF(self.pos(), self.dest)
        if line.length() < 5 and len(self.points) > self.point_index:
            self.point_index += 1
            self.dest = self.points[self.point_index]

        step_size = 20
        # angle = self.rotation() # degrees # move enemy forward at current angle
        angle = -1 * line.angle()
        radians = math.radians(angle)
        dx = step_size * math.cos(radians)
        dy = step_size * math.sin(radians)

        self.setPos(self.pos().x() + dx, self.pos().y() + dy)

    # Not used right now
    def rotateToPoint(self):
        line = QLineF(self.pos(), self.dest)
        angle = -1 * line.angle()

        self.setRotation(angle)

    def setPointPos(self, x, y):
        self.setX(x)
        self.setY(y)

        return self