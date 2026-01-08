from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()

        scene = QGraphicsScene()


