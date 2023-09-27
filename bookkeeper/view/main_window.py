import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from bookkeeper.view import new_exp_widget, exp_widget, budget_widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('bookkeeper')
        self.setFixedSize(900, 700)

        self.exp_widget = exp_widget.ExpenseWidget()
        self.budget_button = budget_widget.BudgetWidget()
        self.new_exp_widget = new_exp_widget.NewExpWidget()


        layout = QVBoxLayout()
        layout.addWidget(self.exp_widget)
        layout.addWidget(self.budget_button)
        layout.addWidget(self.new_exp_widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_expense_add_button_clicked(self, slot):
        """ Обработчик нажатия на клавишу "Добавить" """
        self.new_exp_widget.expense_add_button.clicked.connect(slot)

    def set_category_choice(self, data) -> None:
        """Установить значения выпадающего списка Категорий"""
        cat_data_list = [[str(d.pk), d.name] for d in data]
        self.new_exp_widget.set_category_choice(cat_data_list)





