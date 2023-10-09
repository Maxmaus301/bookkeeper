from typing import Callable, Any
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from bookkeeper.view.new_exp_widget import NewExpWidget
from bookkeeper.view.exp_widget import ExpenseWidget
from bookkeeper.view.category_window import CategoryWindow
from bookkeeper.view.budget_widget import BudgetWidget
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.models.budget import Budget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('bookkeeper')
        self.setFixedSize(900, 700)

        self.exp_widget = ExpenseWidget()
        self.budget_button = BudgetWidget()
        self.new_exp_widget = NewExpWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.exp_widget)
        layout.addWidget(self.budget_button)
        layout.addWidget(self.new_exp_widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_expense_add_button_clicked(self, slot):
        """  Нажатие на клавишу "Добавить" """
        self.new_exp_widget.expense_add_button.clicked.connect(slot)

    def set_category_choice(self, data) -> None:
        """Установить значения выпадающего списка Категорий"""
        cat_data_list = [[str(d.pk), d.name] for d in data]
        self.new_exp_widget.set_category_choice(cat_data_list)

    def set_expense_table(self, exp_data: list, cat_data: list[Category]) -> None:
        """ Установить значения таблицы расходов """
        expense_size = len(exp_data)
        cat_dict = {d.pk: d.name for d in cat_data}
        exp_data_list = []
        for data in exp_data:
            if int(data.category) not in cat_dict.keys():
                raise ValueError(f"Cannot find category wit ID {data.category}")
            exp_data_list.append({"pk": data.pk,
                                    "expense_date": data.expense_date,
                                    "amount": data.amount,
                                    "category": cat_dict[int(data.category)],
                                    "comment": data.comment,
                                    })
        self.exp_widget.set_expense_table(exp_data_list, expense_size)

    def on_edit_button_clicked(self, slot):
        """ Нажатие на клавишу 'Редактировать' """
        self.new_exp_widget.edit_button.clicked.connect(slot)

    def get_amount(self):
        return int(self.new_exp_widget.get_amount())

    def get_comment(self):
        return self.new_exp_widget.get_comment()

    def get_selected_cat(self):
        return self.new_exp_widget.get_selected_cat()




