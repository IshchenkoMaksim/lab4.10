#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу по описанию. Размеры многострочного текстового
поля определяются значениями, введенными в однострочные текстовые поля.
Изменение размера происходит при нажатии мышью на кнопку,  а также при
нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый (lightgrey),
когда поле не в фокусе,  и белый, когда имеет фокус. Событие получения
фокуса обозначается как <FocusIn> , потери – как <FocusOut>.
"""


import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QApplication.instance().focusChanged.connect(self.on_focus)
        self.setWindowTitle("3")
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.text_box = QTextEdit()
        self.btn1 = QPushButton("Edit")
        self.btn1.clicked.connect(self.edit_size)
        self.line_edit2.returnPressed.connect(self.edit_size)
        self.display_widgets()

    def display_widgets(self):
        h_box = QHBoxLayout()
        v_box = QVBoxLayout()
        h_box.addWidget(self.line_edit1)
        h_box.addWidget(self.line_edit2)
        h_box.addWidget(self.btn1)
        v_box.addLayout(h_box)
        v_box.addWidget(self.text_box)
        self.setLayout(v_box)

    def on_focus(self, old, new):
        if self.text_box == new:
            self.text_box.setStyleSheet("background-color: #fff;")
        elif self.text_box == old:
            self.text_box.setStyleSheet("background-color: #d3d3d3;")

    def edit_size(self):
        self.text_box.resize(int(self.line_edit1.text()),
                             int(self.line_edit2.text()))


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
