import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("Währungsumrechner")

        # Layout erstellen:
        layout = QVBoxLayout()
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QVBoxLayout()

        # Widgets erzeugen:
        label1 = QLabel('Schweizer Franken:')
        self.lineEdit = QLineEdit()
        
        self.label2 = QLabel('Euro:')
        self.label3 = QLabel('')

        button1 = QPushButton("Umrechnen")

        # Widgets dem ersten 1. Layout hinzufügen
        layout_1.addWidget(label1)
        layout_1.addWidget(self.lineEdit)

        # Widgets dem ersten 2. Layout hinzufügen
        layout_2.addWidget(self.label2)
        layout_2.addWidget(self.label3)

        # Widgets dem ersten 3. Layout hinzufügen
        layout_3.addWidget(button1)

        # Dem ersten Layout Layouts hinzufügen!
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addLayout(layout_3)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

        button1.clicked.connect(self.auswertung)


    def auswertung(self):
        Franken = float(self.lineEdit.text())
        Euro = Franken*0.8760
        self.label3.setText(str(Euro))


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()