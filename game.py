from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt6.QtGui import QMouseEvent
from tower import Tower
from bullet import Bullet


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()

        # create a scene
        self.gamescene = QGraphicsScene(self)
        self.gamescene.setSceneRect(0, 0, 800, 600)

        # set the scene
        self.setScene(self.gamescene)

        # create a tower
        tower = Tower()
        tower.setPos(self.gamescene.width() / 2 - tower.findXYCenter().x(), self.gamescene.height() / 2 - tower.findXYCenter().y())

        # add tower to the scene
        self.gamescene.addItem(tower)

        self.setFixedSize(800, 600)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def mousePressEvent(self, event):
        bullet = Bullet()
        bullet.setPos(event.pos().toPointF())
        self.gamescene.addItem(bullet)

