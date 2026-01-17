from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsSceneMouseEvent
from PyQt6.QtGui import QPixmap
from tower import Tower


class BuildTowerIcon(QGraphicsPixmapItem):
    def __init__(self, game = None, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/basic_tower_build_icon.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

        self.game = game


    def mousePressEvent(self, event):
        if not self.game.build:
            self.game.build = Tower()
            self.game.setCursor(":/images/images/basic_tower.png")

