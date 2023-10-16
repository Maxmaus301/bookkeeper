from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
QAbstractItemView, QLineEdit, QGridLayout, QComboBox, QPushButton, QTableWidgetItem)
from PySide6.QtCore import Qt

name_horizontal_label = ['Категория', 'Родитель']


class CategoryWindow(QMainWindow):
    """ Виджет окна категорий """

    def __init__(self):
        super(CategoryWindow, self).__init__()

        self.setWindowTitle('Категории приложения')
        self.setFixedSize(500, 500)
        layout = QVBoxLayout()

        category_window_label = QLabel('Категории')
        # category_window_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.category_table = QTableWidget()
        self.category_table.setColumnCount(2)

        header = self.category_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        self.category_table.setHorizontalHeaderLabels(name_horizontal_label)

        category_window_label_1 = QLabel('Добавить категорию')
        category_window_label_1.setAlignment(Qt.AlignCenter)

        layout_1 = QGridLayout()
        label_new_category = QLabel('Новая категория')
        self.line_new_category = QLineEdit()
        label_parent = QLabel('Родитель')
        self.parent_choice = QComboBox()
        self.add_new_category = QPushButton('Добавить категорию')
        self.add_new_category.setFixedSize(150, 30)

        layout_1.addWidget(label_new_category, 0, 0)
        layout_1.addWidget(self.line_new_category, 0, 1)
        layout_1.addWidget(label_parent, 1, 0)
        layout_1.addWidget(self.parent_choice, 1, 1)

        layout.addWidget(category_window_label)
        layout.addWidget(self.category_table)
        layout.addWidget(category_window_label_1)
        layout.addLayout(layout_1)
        layout.addWidget(self.add_new_category, alignment=Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_category_table(self, data, size):
        """ Занести данные о категориях """
        self.category_table.clear()
        self.category_table.setRowCount(size)
        self.category_table.setHorizontalHeaderLabels(name_horizontal_label)
        for i, row in enumerate(data):
            item = QTableWidgetItem(row['name'])
            self.category_table.setItem(i, 0, item)

            item = QTableWidgetItem(row['parent'])
            self.category_table.setItem(i, 1, item)

    def set_parent_choice(self, data):
        """ Занести список при редактировании категорий """
        self.parent_choice.clear()
        self.parent_choice.addItem('-', -1)
        for tup in data:
            self.parent_choice.addItem(tup[0].capitalize(), tup[2])

    def get_category_name(self):
        return self.line_new_category.text()

    def get_parent_pk(self):
        return int(self.parent_choice.itemData(self.parent_choice.currentIndex()))



