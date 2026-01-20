from PyQt6.QtCore import Qt, QLineF
from PyQt6.QtGui import QPixmap
from bullet import Bullet
from enemy import Enemy
import math

class Missile(Bullet):
    def __init__(self, game, tower):
        super().__init__(game, tower)
        
        self.setPixmap(QPixmap(":/images/images/missile.png").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
        self.damage = 2

    def move(self):
        self.distance_traveled = QLineF(self.origin, self.pos()).length()
        # logic for collision with bullet
        if self.collidingItems():
            colliding_items = self.collidingItems()
            for item in colliding_items:
                if type(item) == Enemy:
                    item.health -= self.damage
                    self.game.gamescene.removeItem(self)
                    
                    if item.health < 1:
                        self.game.gamescene.removeItem(item)
                        del item
                        del self

                        return

        elif self.max_range < self.distance_traveled:
            self.game.gamescene.removeItem(self)
            del self

            return
                    
        step_size = 10
        angle = self.rotation() # degrees
        radians = math.radians(angle)
        dx = step_size * math.cos(radians)
        dy = step_size * math.sin(radians)
        self.setPos(self.pos().x() + dx, self.pos().y() + dy)