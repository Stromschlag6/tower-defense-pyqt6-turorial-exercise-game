from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from tower import Tower
from enemy import Enemy
from build_basic_tower_icon import BuildBasicTowerIcon
from build_rocket_tower_icon import BuildRocketTowerIcon


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
        button_space = 10
        self.build = None
        self.build_basic_tower_icon = BuildBasicTowerIcon(self)
        self.gamescene.addItem(self.build_basic_tower_icon)

        self.build_rocket_tower_icon = BuildRocketTowerIcon(self)
        self.build_rocket_tower_icon.setPos(0, self.build_basic_tower_icon.boundingRect().height() + button_space)
        self.gamescene.addItem(self.build_rocket_tower_icon)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # create enemy
        enemy = Enemy()
        self.gamescene.addItem(enemy)

        # test code
        """ tower = Tower()
        tower.setPos(210, 410)
        self.gamescene.addItem(tower) """

    def mousePressEvent(self, event):
        if not self.build == None:
            for item in self.cursor.collidingItems():
                if isinstance(item, Tower):
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

