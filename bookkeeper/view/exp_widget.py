import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
QAbstractItemView)
from PySide6.QtCore import Qt, QSize


class ExpenseWidget(QMainWindow):
    """
    Виджет для отображения списка расходов
    """
    def __init__(self):
        super(ExpenseWidget, self).__init__()

        name_horizontal_label = ['Дата', 'Сумма', 'Категория', 'Комментарий'] # Список имен столбцов таблицы расходов

        self.setWindowTitle('expense_widget')
        layout = QVBoxLayout()

        label = QLabel('Последние расходы')
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(label)

        self.table_exp_widget = QTableWidget(0, 4)


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

