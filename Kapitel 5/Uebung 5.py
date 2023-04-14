import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

        mapb = QPushButton('Zeige auf Karte')
        loadb = QPushButton('Load')
        save_button = QPushButton('Save')

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow('Geburtstag:', self.geburtstagDateEdit)
        layout.addRow('Adresse:', self.adresseLineEdit)
        layout.addRow('Postleitzahl:', self.plzLineEdit)
        layout.addRow('Ort:', self.ortLineEdit)
        layout.addRow('Land:', self.landComboBox)
        layout.addRow(mapb)
        layout.addRow(loadb)
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

        load_menu = QAction("Load", self)
        save_menu = QAction("Save", self)
        quit = QAction("Quit", self)

        filemenu.addAction(load_menu)
        filemenu.addAction(save_menu)
        filemenu.addAction(quit)


        # CONNECTS
        mapb.clicked.connect(self.map_clicked)
        loadb.clicked.connect(self.load_clicked)
        save_button.clicked.connect(self.save_clicked)
        load_menu.triggered.connect(self.load_clicked)
        save_menu.triggered.connect(self.save_clicked)
        quit.triggered.connect(self.quit_clicked)

        

    #Funktionen
    def quit_clicked(self):
        self.close()  # Hauptfenster schliessen = beenden!


    def map_clicked(self):
        a = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        o = self.ortLineEdit.text()
        l = self.landComboBox.currentText()
        link = f'https://www.google.com/maps/place/{a}+{plz}+{o}+{l}'
        QDesktopServices.openUrl(QUrl(link))

    def load_clicked(self):
        dateipfad, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Adresse Datei (*.txt)")
        file = open(dateipfad, "r")
        daten = file.read()
        daten = daten.split(",")

        self.vornameLineEdit.setText(daten[0])
        self.nameLineEdit.setText(daten[1])

        #Datum einfüllen
        dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
        self.geburtstagDateEdit.setDate(QDate.fromString(daten[2], dformat))

        self.adresseLineEdit.setText(daten[3])
        self.plzLineEdit.setText(daten[4])
        self.ortLineEdit.setText(daten[5])

        #Land einfüllen
        if daten[6] == 'Schweiz':
            landnummer = 0
        elif daten[6] == 'Deutschland':
            landnummer = 1
        elif daten[6] == 'Österreich':
            landnummer = 2
        self.landComboBox.setCurrentIndex(landnummer)

        file.close()


    def save_clicked(self):
        #pfad abgreifen
        dateipfad, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Adresse Datei (*.txt)")

        #Variablen abgreifen
        v = self.vornameLineEdit.text()
        n = self.nameLineEdit.text()
        g = self.geburtstagDateEdit.text()
        a = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        o = self.ortLineEdit.text()
        l = self.landComboBox.currentText()
        
        #Datei schreiben
        file = open(dateipfad, "w")
        file.write(f'{v},{n},{g},{a},{plz},{o},{l}')
        #{v},{n},{g},{a},{plz},{o},{l}
        file.close()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()