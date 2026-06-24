# write the code for main app and first screen
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel,QListWidget ,QLineEdit
)

from instr import*


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        #Contenedor Vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignament=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.layout(self.layout)

    def set_appear(self):
        self.setWindowTitle("Nombre")
        self.resize(win_width, win_height)

    def main():
        app = QApplication([])
        ex = MainWin()
        app.exec_()