from PyQt6.QtCore import Qt, QObject, QPointF, QLineF
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QColor
import res

class Tower(QGraphicsPixmapItem, QObject):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setPixmap(QPixmap(":/images/images/provisional_tower.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))

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
        tower_center = QPointF(self.pixmap().width() / 2, self.pixmap().height() / 2)
        delta = QLineF(poly_center, tower_center)
        attack_area.setPos(attack_area.x() + delta.dx(), attack_area.y() + delta.dy())