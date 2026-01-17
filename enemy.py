from PyQt6.QtCore import Qt, QObject, QPointF, QTimer, QLineF
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
import math

class Enemy(QObject, QGraphicsPixmapItem):
    def __init__(self, parent = None):
        super().__init__(parent)

        # set graphics
        self.setPixmap(QPixmap(":/images/images/enemy_cut_out.png"))

        # set points
        self.points = [QPointF(), QPointF(), QPointF()]

        for point in self.points:
            self.mapToScene(point)

        self.points[0].setPointPos(50, 50)
        self.points[1].setPointPos(100, 70)
        self.points[2].setPointPos(150, 450)
        
        self.point_index = 0

        self.dest = self.points[self.point_index]

        # connect timer to move_forward
        self.timer = QTimer()

        self.timer.timeout.connect(self.move_forward)
        self.timer.start(150)
        
    # move enemy forward at current angle
    def move_forward(self):
        step_size = 30
        angle = self.rotation() # degrees
        radians = math.radians(angle)
        dx = step_size * math.cos(radians)
        dy = step_size * math.sin(radians)

        self.setPos(self.pos().x() + dx, self.pos().y() + dy)

    def rotateToPoint(self, point):
        line = QLineF(self.pos(), point)
        angle = -1 * line.angle()

        self.setRotation(angle)

    def setPointPos(self, x, y):
        self.setX(x)
        self.setY(y)

        return self