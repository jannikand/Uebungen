import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *

#für Link
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def clickmap():
    link = f'https://www.google.com/maps/place/{window.length.text()},{window.width.text()}'
    QDesktopServices.openUrl(QUrl(link))

# Eine Qt-Applikation erstellen:
app = QApplication(sys.argv)

window = loadUi("Kapitel 6/Uebung6.ui") # GUI aus ui-File laden:
window.setWindowTitle("Koordinateneingabe")
window.show()

window.buttonmap.clicked.connect(clickmap)

app.exec()


