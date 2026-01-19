from PyQt6.QtCore import Qt, QLineF
from PyQt6.QtGui import QPixmap
from tower import Tower
from missile import Missile


class RocketTower(Tower):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/rocket_tower.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

    def fire(self):
        bullet = Missile(self.game, self)
        bullet.setPos(self.mapToScene(self.findXYCenter().x() - bullet.pixmap().width() / 2, self.findXYCenter().y() - bullet.pixmap().height() / 2))
        bullet.setTransformOriginPoint(bullet.pixmap().width() / 2, bullet.pixmap().height() / 2) # rotation was the problem of not centered bullet

        line = QLineF(self.findXYCenter(), self.attack_dest)
        angle = -1 * line.angle()

        bullet.setRotation(angle)
        self.game.gamescene.addItem(bullet)
