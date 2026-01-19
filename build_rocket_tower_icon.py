from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from rocket_tower import RocketTower


class BuildRocketTowerIcon(QGraphicsPixmapItem):
    def __init__(self, game, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/rocket_tower_build_icon.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

        self.game = game


    def mousePressEvent(self, event):
        if not self.game.build:
            self.game.build = RocketTower(self.game)
            self.game.setCursor(":/images/images/rocket_tower.png")