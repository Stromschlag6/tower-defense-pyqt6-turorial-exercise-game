from PyQt6.QtWidgets import QApplication
from game import Game
import sys


app = QApplication(sys.argv)

game = Game()
game.show()

app.exec()

