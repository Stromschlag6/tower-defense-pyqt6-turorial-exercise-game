from PyQt6.QtCore import Qt, QObject, QPointF, QLineF, QTimer
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem
from PyQt6.QtGui import QPolygonF, QPen, QPixmap
from bullet import Bullet
from enemy import Enemy
import res

class Tower(QGraphicsPixmapItem, QObject):
    def __init__(self, parent = None):
        super().__init__(parent)

        #self.setPixmap(QPixmap(":/images/images/basic_tower.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

        self.attack_dest = QPointF()
        self.timer = QTimer()

        # create a polygon from these points
        polygon = QPolygonF()
        polygon << QPointF(1,0) << QPointF(2,0) << QPointF(3,1) << QPointF(3,2) << QPointF(2,3) << QPointF(1,3) << QPointF(0,2) << QPointF(0,1)

        # scale points
        scale_factor = 80
        for point in polygon:
            point *= scale_factor

        # create the QGraphicsPolygonItem
        self.attack_area = QGraphicsPolygonItem(polygon, self)
        self.attack_area.setPen(QPen(Qt.PenStyle.DotLine))

        # move the polygon
        # TODO Potential problem with coordinates because of potential differentiating origins(scene, polygon or polygon item)
        poly_center = QPointF(1.5, 1.5)
        poly_center *= scale_factor
        poly_center = self.mapToScene(poly_center)
        delta = QLineF(poly_center, self.findXYCenter())
        self.attack_area.setPos(self.attack_area.x() + delta.dx(), self.attack_area.y() + delta.dy()) # TODO position set before tower placed(made visible), question: why polygon near tower then?
        # probably because not centered right, will have to look into it

        print(f"poly_center:{poly_center} tower center:{self.findXYCenter()}")

        self.has_target = False

        # connect a timer to attack_target
        self.timer.timeout.connect(self.aquireTarget)
        self.timer.start(1500)

    def fire(self):
        """ Reference(here actually parent) in this case actually working, because tower also QGraphicsItem, as of my understanding now same classes or classes with same parent can take each other as children
        (of course just one the other) """
        bullet = Bullet(self)
        bullet.setPos(self.findXYCenter().x() - bullet.pixmap().width() / 2, self.findXYCenter().y() - bullet.pixmap().height() / 2)
        bullet.setTransformOriginPoint(bullet.pixmap().width() / 2, bullet.pixmap().height() / 2) # rotation was the problem of not centered bullet

        line = QLineF(self.findXYCenter(), self.attack_dest)
        angle = -1 * line.angle()

        bullet.setRotation(angle)

    def aquireTarget(self):
        # get a list of all items colliding with attack_area
        colliding_items = self.attack_area.collidingItems()

        closest_dist = 400
        closest_point = None

        # all positions are being aimad at top left of respective objects, need to be centered
        for object in colliding_items:
            if type(object) == Enemy:
                this_distance = self.distanceTo(object)
                if this_distance < closest_dist:
                    closest_dist = this_distance
                    closest_point = QPointF(object.pos().x() + object.pixmap().width() / 2, object.pos().y() + object.pixmap().height() / 2)
                    self.has_target = True
                    self.attack_dest = self.mapFromScene(closest_point)
                
                self.fire()
        
    def findXYCenter(self):
        return QPointF(self.pixmap().width() / 2, self.pixmap().height() / 2)
    
    def distanceTo(self, item):
        line = QLineF(self.pos(), item.pos())

        return line.length()