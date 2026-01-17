from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt6.QtGui import QMouseEvent, QPixmap, QBrush
from tower import Tower
from bullet import Bullet
from enemy import Enemy
from build_tower_icon import BuildTowerIcon


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(900, 500)

        # create a scene
        self.gamescene = QGraphicsScene(self)
        self.gamescene.setSceneRect(0, 0, 900, 500)

        # set the scene
        self.setScene(self.gamescene)

        # cursor
        self.cursor = None
        self.setMouseTracking(True)

        # build tower buttons
        self.build = None
        self.build_tower_icon = BuildTowerIcon(self)
        self.gamescene.addItem(self.build_tower_icon)        

        # create a tower
        tower = Tower()
        tower.setPos(self.gamescene.width() / 2 - tower.findXYCenter().x(), self.gamescene.height() / 2 - tower.findXYCenter().y())

        # add tower to the scene
        self.gamescene.addItem(tower)


        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # create enemy
        enemy = Enemy()
        self.gamescene.addItem(enemy)

    def mousePressEvent(self, event):
        if not self.build == None:
            for item in self.cursor.collidingItems():
                if type(item) == Tower:
                    return print("space already used")
                
            self.build.setPos(event.pos().toPointF().x() - self.build.boundingRect().width() / 2, event.pos().toPointF().y() - self.build.boundingRect().height() / 2)
            self.gamescene.addItem(self.build)
            self.build = None
            self.cursor = None

        else:
            super().mousePressEvent(event)

    def setCursor(self, filename):
        if self.cursor:
            self.gamescene.removeItem(self.cursor)
            del self.cursor

        self.cursor = QGraphicsPixmapItem()
        self.cursor.setPixmap(QPixmap(filename).scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))
        self.gamescene.addItem(self.cursor)

    def mouseMoveEvent(self, event):
        if self.cursor:
            self.cursor.setPos(event.pos().toPointF().x() - self.cursor.boundingRect().width() / 2, event.pos().toPointF().y() - self.cursor.boundingRect().height() / 2)

