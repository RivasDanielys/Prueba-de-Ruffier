from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # comprobar los tipos de los valores de entrada
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.set_appear()

        self.show()

    def initUI(self):
        # Botones
        self.btn_next =  QPushButton(txt_sendresults)
        self.btn_test1 =  QPushButton(txt_starttest1)
        self.btn_test2 =  QPushButton(txt_starttest2)
        self.btn_test3 =  QPushButton(txt_starttest3)

        # Etiquetas
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        # Inputs
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        # Contenedores
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        # Nombre
        self.l_line.addWidget(self.text_name,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name,  alignment = Qt.AlignLeft)

        # Edad 
        self.l_line.addWidget(self.text_age,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age,  alignment = Qt.AlignLeft)

        # Test 1
        self.l_line.addWidget(self.text_test1,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1,  alignment = Qt.AlignLeft)

        # Test 2
        self.l_line.addWidget(self.text_test2,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2,  alignment = Qt.AlignLeft)
        
        # Test 3
        self.l_line.addWidget(self.text_test3,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3,  alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3,  alignment = Qt.AlignLeft)

        # Boton siguiente
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)

        # Contenedores
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)