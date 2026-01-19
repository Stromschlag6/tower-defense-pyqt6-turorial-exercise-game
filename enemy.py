from PyQt6.QtCore import Qt, QObject, QPointF, QTimer, QLineF
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
import math

class Enemy(QGraphicsPixmapItem, QObject): # wrong order endes in weird bug, why does QGraphicsPixmapItem have to be first?
    def __init__(self, points_to_follow,  parent = None):
        super().__init__(parent)

        # set graphics
        self.setPixmap(QPixmap(":/images/images/enemy.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))

        # set health
        self.health = 2

        # set points
        self.points = points_to_follow
        self.point_index = 0
        self.dest = self.points[self.point_index]

        # connect timer to move_forward
        self.timer = QTimer()

        self.timer.timeout.connect(self.move_forward)
        self.timer.start(150)
        
    # move enemy forward at current angle
    def move_forward(self):
        # if close enough to dest, go to next dest
        line = QLineF(self.pos(), QPointF(self.dest.x() - self.boundingRect().width() / 2, self.dest.y() - self.boundingRect().height() / 2))
        if line.length() < 5:
            self.point_index += 1
            if self.point_index < len(self.points):
                self.dest = self.points[self.point_index]
            else:
                self.timer.disconnect()

        step_size = 5
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