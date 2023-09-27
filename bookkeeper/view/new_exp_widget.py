import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
                               QGridLayout, QLineEdit, QComboBox, QDateTimeEdit, QPushButton)
from PySide6.QtCore import Qt, QDateTime


class NewExpWidget(QMainWindow):
    """
    Виджет для добавления нового расхода
    """

    def __init__(self):
        super(NewExpWidget, self).__init__()

        self.setWindowTitle('new_exp_widget')
        layout = QGridLayout()

        amount_label = QLabel('Сумма')
        amount_line = QLineEdit()

        category_label = QLabel('Категория')
        self.category_choice = QComboBox()

        edit_button = QPushButton('Редактировать')

        comment_label = QLabel('Комментарий')
        comment_label_edit = QLineEdit()

        datetime_label = QLabel('Дата')
        datetime_label_edit = QDateTimeEdit()
        datetime_label_edit.setDateTime(QDateTime.currentDateTime())
        datetime_label_edit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        datetime_label_edit.setCalendarPopup(True)

        self.expense_add_button = QPushButton('Добавить')

        layout.addWidget(amount_label, 0, 0)
        layout.addWidget(amount_line, 0, 1)
        layout.addWidget(category_label, 1, 0)
        layout.addWidget(self.category_choice, 1, 1)
        layout.addWidget(edit_button, 2, 2)
        layout.addWidget(comment_label, 2, 0)
        layout.addWidget(comment_label_edit, 2, 1)
        layout.addWidget(datetime_label, 3, 0)
        layout.addWidget(datetime_label_edit, 3, 1)
        layout.addWidget(self.expense_add_button, 4, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_category_choice(self, data):
        """Занести список категорий"""
        self.category_choice.clear()
        for tup in data:
            self.category_choice.addItem(tup[1].capitalize(), tup[0])

