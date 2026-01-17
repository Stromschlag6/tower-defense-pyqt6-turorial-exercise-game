from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap

class Tower(QGraphicsPixmapItem, QObject):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/provisional_tower.png"))

        attack_area = QGraphicsPolygonItem()

