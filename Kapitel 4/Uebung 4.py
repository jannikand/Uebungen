import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI Programmierung")

        # Layouts erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagDateEdit = QDateEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()

        self.landComboBox = QComboBox()
        self.landComboBox.addItems(["Schweiz", "Deutschland", "Österreich"])

        save_button = QPushButton('Save')

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow('Geburtstag:', self.geburtstagDateEdit)
        layout.addRow('Adresse:', self.adresseLineEdit)
        layout.addRow('Postleitzahl:', self.plzLineEdit)
        layout.addRow('Ort:', self.ortLineEdit)
        layout.addRow('Land:', self.landComboBox)
        layout.addRow(save_button)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

        # Menubar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save_menu = QAction("Save", self)
        quit = QAction("Quit", self)

        filemenu.addAction(save_menu)
        filemenu.addAction(quit)


        # CONNECTS
        save_button.clicked.connect(self.save_clicked)
        save_menu.triggered.connect(self.save_clicked)
        quit.triggered.connect(self.quit_clicked)

    #Funktionen
    def quit_clicked(self):
        self.close()  # Hauptfenster schliessen = beenden!


    def save_clicked(self):
        #Variablen abgreifen
        vorname = self.vornameLineEdit.text()
        name = self.nameLineEdit.text()
        geburtstag = self.geburtstagDateEdit.text()
        adresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.landComboBox.currentText()

        #Datei schreiben
        file = open("output.txt", "w")
        file.write(f'{vorname},{name},{geburtstag},{adresse},{plz},{ort},{land}')
        file.close()

        print(f'{vorname},{name},{geburtstag},{adresse},{plz},{ort},{land}')

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()