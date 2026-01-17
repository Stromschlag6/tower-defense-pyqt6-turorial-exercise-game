from PyQt6.QtCore import Qt, QObject, QPointF
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class Enemy(QObject, QGraphicsPixmapItem):
    def __init__(self, parent = None):
        super().__init__(parent)

        # set graphics
        self.setPixmap(QPixmap(":/images/images/enemy_cut_out.png"))

        # set points
        self.points = []
        self.points.append(self.mapToScene(self.setPointPos(QPointF(), 50, 50)))
        self.points.append(self.mapToScene(self.setPointPos(QPointF(), 100, 70)))
        self.points.append(self.mapToScene(self.setPointPos(QPointF(), 100, 70)))
        self.dest = QPointF()
        self.point_index = None

    def move_forward(self):
        pass

    def rotateToPoint(self, point):
        pass

    def setPointPos(self, point, x, y):
        point.setX(x)
        point.setY(y)

        return point