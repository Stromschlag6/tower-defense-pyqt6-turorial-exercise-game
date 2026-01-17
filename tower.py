from PyQt6.QtCore import Qt, QObject, QPointF, QLineF, QTimer
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF
from bullet import Bullet
import res

class Tower(QGraphicsPixmapItem, QObject):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/provisional_tower_maybe_not_centered.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))
        self.attack_dest = QPointF()
        self.timer = QTimer()

        # create a polygon from these points
        polygon = QPolygonF()
        polygon << QPointF(1,0) << QPointF(2,0) << QPointF(3,1) << QPointF(3,2) << QPointF(2,3) << QPointF(1,3) << QPointF(0,2) << QPointF(0,1)

        # scale points
        scale_factor = 60
        for point in polygon:
            point *= scale_factor

        # create the QGraphicsPolygonItem
        attack_area = QGraphicsPolygonItem(polygon, self)

        # move the polygon
        # TODO Potential problem with coordinates because of potential differentiating origins(scene, polygon or polygon item)
        poly_center = QPointF(1.5, 1.5)
        poly_center *= scale_factor
        poly_center = self.mapToScene(poly_center)
        delta = QLineF(poly_center, self.findXYCenter())
        attack_area.setPos(attack_area.x() + delta.dx(), attack_area.y() + delta.dy())

        # connect a timer to attack_target
        self.timer.timeout.connect(self.attackTarget)
        self.timer.start(1500)

    def attackTarget(self):
        bullet = Bullet(self)
        bullet.setPos(self.findXYCenter().x() - bullet.pixmap().width() / 2, self.findXYCenter().y() - bullet.pixmap().height() / 2)
        
        """ TODO As soon as enemy within game possible solution with coords -> game as towers parent, therefore tower should be able to acces enemys position(probably created by game) and
        then set self.attack_dest = self.mapToScene(game.enemy)"""
        line = QLineF(self.findXYCenter(), self.attack_dest)
        angle = -1 * line.angle()

        bullet.setRotation(angle)

    def findXYCenter(self):
        return QPointF(self.pixmap().width() / 2, self.pixmap().height() / 2)