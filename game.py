from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
from tower import Tower


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()

        # create a scene
        self.gamescene = QGraphicsScene(self)
        self.setSceneRect(0, 0, 800, 600)

        # set the scene
        self.setScene(self.gamescene)

        # create a tower
        tower = Tower()

        # add tower to the scene
        self.gamescene.addItem(tower)

        self.setFixedSize(800, 600)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

