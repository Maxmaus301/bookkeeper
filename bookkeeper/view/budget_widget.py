import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
QAbstractItemView)
from PySide6.QtCore import Qt


class BudgetWidget(QMainWindow):
    """
    Виджет для отображения бюджета
    """
    def __init__(self):
        super(BudgetWidget, self).__init__()

        name_horizontal_label = ['Сумма', 'Бюджет'] # Список имен столбцов таблицы бюджета
        name_vertical_label = ['День', 'Неделя', 'Месяц'] # Список имен строк таблицы бюджета
        self.setWindowTitle('budget_widget')
        layout = QVBoxLayout()

        label = QLabel('Бюджет')
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(label)
        self.table_exp_widget = QTableWidget(3, 2)

        header = self.table_exp_widget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        vertical_header = self.table_exp_widget.verticalHeader()
        vertical_header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        vertical_header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        vertical_header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.table_exp_widget.setHorizontalHeaderLabels(name_horizontal_label)
        self.table_exp_widget.setVerticalHeaderLabels(name_vertical_label)

        layout.addWidget(self.table_exp_widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

