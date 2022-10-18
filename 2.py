#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном
текстовом поле приводит к перемещению текста из него в список (экземпляр
Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке
списка, она должна копироваться в текстовое поле.
"""

from PySide2.QtWidgets import QApplication, QWidget, QLineEdit,\
    QVBoxLayout, QListWidget
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2")
        self.setGeometry(100, 100, 200, 200)
        self.lst_wt = QListWidget()
        self.lst_wt.itemDoubleClicked.connect(self.replace_item)
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.replace_text)

    def align(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.lst_wt)
        self.setLayout(vbox)

    def replace_text(self):
        self.lst_wt.addItem(self.line_edit.text())
        self.line_edit.clear()

    def replace_item(self):
        items = self.lst_wt.selectedItems()
        if not items:
            return
        for item in items:
            self.line_edit.setText(item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())
