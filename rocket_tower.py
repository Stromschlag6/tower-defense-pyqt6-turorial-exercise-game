from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from tower import Tower


class RocketTower(Tower):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/rocket_tower.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))
