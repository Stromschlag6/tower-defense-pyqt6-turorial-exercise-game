from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
from tower import Tower


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()

        # create a scene
        self.gamescene = QGraphicsScene(self)

        # set the scene
        self.setScene(self.gamescene)

        # create a tower
        tower = Tower()

        # add tower to the scene
        self.gamescene.addItem(tower)

