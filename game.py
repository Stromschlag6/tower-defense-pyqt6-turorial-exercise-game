from PyQt6.QtCore import Qt, QTimer, QPointF, QLineF
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsLineItem
from PyQt6.QtGui import QPixmap, QPen
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
        self.timer = QTimer()
        self.enemies_spawned = None
        self.max_number_of_enemies = None
        self.points_to_follow = [QPointF(800, 0), QPointF(450, 450), QPointF(0, 300)]
        self.createEnemies(5)

        # create road
        self.createRoad()

        # test code
        """ tower = Tower()
        tower.setPos(210, 410)
        self.gamescene.addItem(tower) """

    def setCursor(self, filename):
        if self.cursor:
            self.gamescene.removeItem(self.cursor)
            del self.cursor

        self.cursor = QGraphicsPixmapItem()
        self.cursor.setPixmap(QPixmap(filename).scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))
        self.gamescene.addItem(self.cursor)

    def createEnemies(self, number_of_enemies):
        self.enemies_spawned = 0
        self.max_number_of_enemies = number_of_enemies
        self.timer.timeout.connect(self.createEnemy)
        self.timer.start(1500)

    def createEnemy(self):
        # spawn an enemy
        enemy = Enemy(self.points_to_follow)
        enemy.setPos(self.points_to_follow[0].x() - enemy.boundingRect().width() / 2, self.points_to_follow[0].y() - enemy.boundingRect().height() / 2)
        self.gamescene.addItem(enemy)
        self.enemies_spawned += 1
        if self.enemies_spawned >= self.max_number_of_enemies:
            self.timer.disconnect()

    def createRoad(self):
        i = 0
        for point in self.points_to_follow:
            # create a line connecting the two points
            if i < len(self.points_to_follow) - 1:
                i += 1
                line = QLineF(point, self.points_to_follow[i])
                line_item = QGraphicsLineItem(line)

                pen = QPen()
                pen.setWidth(2)
                pen.setColor(Qt.GlobalColor.red)

                line_item.setPen(pen)
                self.gamescene.addItem(line_item)

    # events
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

    def mouseMoveEvent(self, event):
        if self.cursor:
            self.cursor.setPos(event.pos().toPointF().x() - self.cursor.boundingRect().width() / 2, event.pos().toPointF().y() - self.cursor.boundingRect().height() / 2)

