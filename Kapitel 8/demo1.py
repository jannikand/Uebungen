from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        #self.addToolBar(NavigationToolbar(canvas, self))

        button1 = QPushButton("y=sin(x)")
        button2 = QPushButton("y=cos(x)")

        button1.clicked.connect(self.plot1)
        button2.clicked.connect(self.plot2)

        layout.addWidget(self.canvas)
        layout.addWidget(button1)
        layout.addWidget(button2)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

    def plot1(self):
        plt.clf() # clear figure: löscht die aktuelle Figure
        x = np.linspace(-np.pi, np.pi, 20)
        y = np.sin(x)
        plt.plot(x, y, "ro-")
        plt.axis("equal")

        self.canvas.draw()

    def plot2(self):
        plt.clf() # clear figure
        x = np.linspace(-np.pi, np.pi, 20)
        y = np.cos(x)
        plt.plot(x, y, "ko-")
        plt.axis("equal")
        
        self.canvas.draw()

app = QApplication([])
window = Window()
app.exec()
