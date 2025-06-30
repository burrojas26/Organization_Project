import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Graphics")

        button = QPushButton("Click Me")
        button.setCheckable(True)
        button.clicked.connect(self.btnFunc)
        
        self.setCentralWidget(button)
        
    def btnFunc(self):
        print("Button clicked!")
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()  