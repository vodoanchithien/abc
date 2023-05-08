import sys
from PySide6.QtWidgets import QApplication
import pyqtgraph as pg

uiclass, baseclass = pg.Qt.loadUiType("embed1.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()