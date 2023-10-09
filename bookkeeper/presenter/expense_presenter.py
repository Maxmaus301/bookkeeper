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

    def __init__(self, view: MainWindow, cat_repo, exp_repo):
        self.view = view

        self.cat_repo = cat_repo
        self.exp_repo = exp_repo

        self.exp_data = self.exp_repo.get_all()
        self.cat_data = self.cat_repo.get_all()


        self.view.on_expense_add_button_clicked(
            self.handle_expense_add_button_clicked)
        self.view.on_edit_button_clicked(
            self.handle_edit_button_clicked)

    def show(self):
        self.view.show()
        self.view.set_category_choice(self.cat_data)
        self.view.set_expense_table(self.exp_data, self.cat_data)

    def handle_expense_add_button_clicked(self):
        """ Обработчик кнопки 'Добавить' """
        cat_pk = self.view.get_selected_cat()
        amount = self.view.get_amount()
        comment = self.view.get_comment()
        exp = Expense(amount=amount, category=cat_pk, comment=comment)
        self.exp_repo.add(exp)
        self.update_expense_table()

    def handle_edit_button_clicked(self):
        """ Обработчик кнопки 'Редактировать' """
        pass


    def update_expense_table(self):
        """ Обновить таблицу затрат """
        self.cat_data = self.cat_repo.get_all()
        self.exp_data = self.exp_repo.get_all()
        self.view.set_expense_table(self.exp_data, self.cat_data)