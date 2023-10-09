from typing import Any
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
QAbstractItemView, QTableWidgetItem)
from PySide6.QtCore import Qt, QSize


class ExpenseWidget(QMainWindow):
    """
    Виджет для отображения списка расходов
    """
    def __init__(self):
        super(ExpenseWidget, self).__init__()
        self.data: list[Any] = []

        name_horizontal_label = ['Дата', 'Сумма', 'Категория', 'Комментарий'] # Список имен столбцов таблицы расходов

        self.setWindowTitle('expense_widget')
        layout = QVBoxLayout()

        label = QLabel('Последние расходы')
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(label)

        self.table_exp_widget = QTableWidget()
        self.table_exp_widget.setColumnCount(4)


        header = self.table_exp_widget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        self.table_exp_widget.setHorizontalHeaderLabels(name_horizontal_label)

        layout.addWidget(self.table_exp_widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_expense_table(self, data, size):
        """ Заполнить таблицу расходов """
        name_horizontal_label = ['Дата', 'Сумма', 'Категория', 'Комментарий']  # Список имен столбцов таблицы расходов
        self.data = data
        self.data.sort(key=lambda d: d["expense_date"], reverse=True)
        self.table_exp_widget.clear()
        self.table_exp_widget.setRowCount(size)
        for i, row in enumerate(self.data):
            item = QTableWidgetItem(row["expense_date"])
            self.table_exp_widget.setItem(i, 0, item)

            item = QTableWidgetItem(str(row["amount"]))
            self.table_exp_widget.setItem(i, 1, item)

            item = QTableWidgetItem(row["category"].capitalize())
            self.table_exp_widget.setItem(i, 2, item)

            item = QTableWidgetItem(row["comment"])
            self.table_exp_widget.setItem(i, 3, item)

        self.table_exp_widget.setHorizontalHeaderLabels(name_horizontal_label)

