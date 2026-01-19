from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from basic_tower import BasicTower


class BuildBasicTowerIcon(QGraphicsPixmapItem):
    def __init__(self, game, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/basic_tower_build_icon.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

        self.game = game


    def mousePressEvent(self, event):
        if not self.game.build:
            self.game.build = BasicTower(self.game)
            self.game.setCursor(":/images/images/basic_tower.png")

