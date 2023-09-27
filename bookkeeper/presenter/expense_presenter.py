"""
Presenter приложения
"""
from datetime import datetime
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.view.main_window import MainWindow
from bookkeeper.view.new_exp_widget import NewExpWidget
from bookkeeper.repository.sqlite_repository import SqliteRepository

class Presenter:
    """ Класс презентера """

    def __init__(self, view: MainWindow, cat_repo):
        self.view = view

        self.cat_repo = cat_repo

        self.cat_data = self.cat_repo.get_all()


        self.view.on_expense_add_button_clicked(
            self.handle_expense_add_button_clicked)


    def show(self):
        self.view.show()
        self.view.set_category_choice(self.cat_data)

    def handle_expense_add_button_clicked(self):
        print(123)

