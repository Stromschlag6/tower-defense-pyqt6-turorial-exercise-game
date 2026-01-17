from PyQt6.QtCore import Qt, QObject, QTimer
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
import math

class Bullet(QGraphicsPixmapItem, QObject):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/laser_shot.png").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))

        self.timer = QTimer()

        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        step_size = 30
        angle = self.rotation() # degrees
        radians = math.radians(angle)
        dx = step_size * math.cos(radians)
        dy = step_size * math.sin(radians)
        self.setPos(self.pos().x() + dx, self.pos().y() + dy)