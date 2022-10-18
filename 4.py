#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Создайте на холсте изображение """

from PySide2.QtCore import Qt, QPoint, QRectF
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon
from PySide2.QtWidgets import QApplication, QWidget
import sys
import random


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("4")
        self.setGeometry(100, 100, 500, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.cyan)
        painter.drawRect(130, 142, 250, 250)
        painter.setBrush((QBrush(Qt.white)))
        painter.drawRect(215, 204, 70, 70)
        painter.setBrush((QBrush(Qt.cyan)))
        points = QPolygon([
            QPoint(110, 140),
            QPoint(255, 40),
            QPoint(400, 140)
        ])
        painter.drawPolygon(points)
        painter.begin(self)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.yellow, 1, Qt.SolidLine))
        painter.drawEllipse(390, 6, 80, 80)
        self.drawGrass(painter)
        self.drawCat(painter)

    def drawGrass(self, painter):
        painter.begin(self)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(Qt.green)
        for i in range(30):
            painter.drawArc(random.randint(1, 2), 220,
                            i * 20, 360, 0 * 100, random.randint(35, 35) * 10)

    def drawCat(self, painter):
        painter.begin(self)
        painter.setBrush((QBrush(Qt.gray)))
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        points = QPolygon([
            QPoint(127, 290),
            QPoint(120, 380),
            QPoint(160, 360),
        ])
        painter.drawPolygon(points)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        points = QPolygon([
            QPoint(25, 380),
            QPoint(55, 245),
            QPoint(70, 285),
            QPoint(95, 285),
            QPoint(115, 245),
            QPoint(130, 380),
        ])
        painter.drawPolygon(points)

        painter.setPen(QPen(Qt.white))

        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(50, 295, 25, 25)
        painter.drawEllipse(90, 295, 25, 25)

        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(51, 305, 10, 10)
        painter.drawEllipse(93, 305, 10, 10)

        painter.setPen(QPen(Qt.red))
        painter.setBrush(QBrush(Qt.red))
        painter.drawEllipse(78, 321, 7, 7)

        rectangle = QRectF(78, 340, 8, 8)
        start_angle = 140 * 16
        span_angle = 270 * 16
        painter = QPainter(self)
        painter.drawArc(rectangle, start_angle, span_angle)

        painter.setBrush(QBrush(Qt.gray))
        painter.drawEllipse(44, 370, 25, 15)
        painter.drawEllipse(78, 370, 25, 15)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
