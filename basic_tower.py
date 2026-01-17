from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from tower import Tower


class BasicTower(Tower):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/basic_tower.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

        # connect a timer to attack_target
        self.timer.timeout.connect(self.aquireTarget)
        self.timer.start(1500)