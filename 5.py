#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
B программе создается анимация круга, который движется от левой
границы холста до правой. Изучите приведенную программу и
самостоятельно запрограммируйте постепенное движение фигуры в ту т
очку холста, где пользователь кликает левой кнопкой мыши. Координаты
события хранятся в его атрибутах x и y (event.x, event.y).
"""

from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPropertyAnimation, QPoint
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5")
        self.setGeometry(100, 100, 400, 300)
        self.child = QWidget(self)
        self.child.setStyleSheet(
            "background-color: green; border-radius: 25%;"
        )
        self.child.resize(50, 50)
        self.animation = QPropertyAnimation(self.child, b"pos")
        self.animation.setDuration(3000)

    def mousePressEvent(self, event):
        self.animation.setEndValue(QPoint(event.x() - 25, event.y() - 25))
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
