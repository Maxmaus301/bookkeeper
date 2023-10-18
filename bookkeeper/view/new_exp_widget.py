from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
                               QGridLayout, QLineEdit, QComboBox, QDateTimeEdit, QPushButton)
from PySide6.QtCore import Qt, QDateTime


class NewExpWidget(QMainWindow):
    """
    Виджет для добавления нового расхода
    """

    def __init__(self):
        super(NewExpWidget, self).__init__()

        layout = QGridLayout()

        amount_label = QLabel('Сумма')
        self.amount_line = QLineEdit()

        category_label = QLabel('Категория')
        self.category_choice = QComboBox()

        self.edit_button = QPushButton('Редактировать')

        comment_label = QLabel('Комментарий')
        self.comment_label_edit = QLineEdit()

        datetime_label = QLabel('Дата')
        self.datetime_label_edit = QDateTimeEdit()
        self.datetime_label_edit.setDateTime(QDateTime.currentDateTime())
        self.datetime_label_edit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.datetime_label_edit.setCalendarPopup(True)

        self.expense_add_button = QPushButton('Добавить')

        layout.addWidget(amount_label, 0, 0)
        layout.addWidget(self.amount_line, 0, 1)
        layout.addWidget(category_label, 1, 0)
        layout.addWidget(self.category_choice, 1, 1)
        layout.addWidget(self.edit_button, 2, 2)
        layout.addWidget(comment_label, 2, 0)
        layout.addWidget(self.comment_label_edit, 2, 1)
        layout.addWidget(datetime_label, 3, 0)
        layout.addWidget(self.datetime_label_edit, 3, 1)
        layout.addWidget(self.expense_add_button, 4, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_category_choice(self, data):
        """Занести список категорий"""
        self.category_choice.clear()
        for tup in data:
            self.category_choice.addItem(tup[1].capitalize(), tup[0])

    def get_amount(self):
        """ Получить сумму новой траты """
        return int(self.amount_line.text())

    def get_comment(self):
        """ Получить комментарий для новой траты """
        return self.comment_label_edit.text()

    def get_selected_cat(self):
        """ Получить категорию новой траты """
        return self.category_choice.itemData(self.category_choice.currentIndex())

    def get_datetime(self):
        """ Получить дату новой траты """
        return self.datetime_label_edit.text()





