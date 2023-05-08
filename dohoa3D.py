import sys
from PyQt5 import QtWidgets, uic
from simple3d import *
# app = QtWidgets.QApplication(sys.argv)

# window1 = uic.loadUi("embed3D.ui")
# # window = Window()
# window1.show()
# app.exec()
app = QGuiApplication(sys.argv)
view = Window()
view.show()
sys.exit(app.exec())