"""
Presenter приложения
"""
from datetime import datetime
from typing import Any
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.models.budget import Budget
from bookkeeper.view.main_window import MainWindow
from bookkeeper.view.new_exp_widget import NewExpWidget
from bookkeeper.repository.sqlite_repository import SqliteRepository


class Presenter:
    """ Класс презентера """

    def __init__(self, view: MainWindow, cat_repo, exp_repo, bud_repo):
        self.view = view

        self.bud_repo = bud_repo
        self.cat_repo = cat_repo
        self.exp_repo = exp_repo

        self.bud_data = self.bud_repo.get_all()
        self.exp_data = self.exp_repo.get_all()
        self.cat_data = self.cat_repo.get_all()

        self.view.on_expense_add_button_clicked(
            self.handle_expense_add_button_clicked)
        self.view.on_edit_button_clicked(
            self.handle_edit_button_clicked)
        self.view.on_add_new_category_clicked(
            self.handle_add_new_category_clicked)
        self.view.on_budget_item_changed(
           self.handle_budget_item_changed)

    def show(self):
        self.view.show()
        self.view.set_category_choice(self.cat_data)
        self.view.set_expense_table(self.exp_data, self.cat_data)
        self.view.set_category_table(self.cat_data)
        self.view.set_parent_choice(self.cat_data)
        # self.view.set_budget_table(self.exp_data, self.bud_data)

    def handle_expense_add_button_clicked(self):
        """ Обработчик кнопки 'Добавить' """
        cat_pk = self.view.get_selected_cat()
        amount = self.view.get_amount()
        comment = self.view.get_comment()
        new_date = self.view.get_datetime()
        if new_date is None:
            exp = Expense(amount=amount, category=cat_pk, comment=comment)
        else:
            exp = Expense(amount=amount, category=cat_pk, comment=comment,
                          expense_date=datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S"))
        self.exp_repo.add(exp)
        self.update_expense_table()

    def handle_edit_button_clicked(self):
        """ Обработчик кнопки 'Редактировать' """
        self.view.open_category_window()

    def handle_add_new_category_clicked(self):
        """ Обработчик нажатия кнопки 'Добавить категорию' """
        cat_name = self.view.get_category_name()
        par_pk = self.view.get_parent_pk()
        if cat_name == '':
            return
        if par_pk == -1:
            cat_new = Category(name=cat_name)
        else:
            cat_new = Category(name=cat_name, parent=par_pk)
        self.cat_repo.add(cat_new)
        self.update_category_window()

    def handle_budget_item_changed(self, item: Any) -> None:
        """Обработчик изменения значения ячеек бюджета"""
        budget = [item.data(1), item.data(0)]
        if budget[0] is not None:
            obj = self.bud_repo.get(budget[0])
            # может приходить "ложный" сигнал от itemChanged при построении таблицы
            if obj.amount == budget[1]:
                return
            obj.amount = budget[1]
            self.bud_repo.update(obj)
            self.bud_data = self.bud_repo.get_all()
            self.exp_data = self.exp_repo.get_all()
            self.view.set_budget_table(self.exp_data, self.bud_data)

    def update_expense_table(self):
        """ Обновить таблицу затрат """
        self.cat_data = self.cat_repo.get_all()
        self.exp_data = self.exp_repo.get_all()
        self.view.set_expense_table(self.exp_data, self.cat_data)

    def update_category_window(self):
        """ Обновить таблицу редактиварония категорий """
        self.cat_data = self.cat_repo.get_all()
        self.view.set_category_table(self.cat_data)
        self.view.set_category_choice(self.cat_data)
        self.view.set_parent_choice(self.cat_data)

    def update_budget_data(self) -> None:
        """Обновление таблицы бюджета"""
        self.bud_data = self.bud_repo.get_all()
        self.exp_data = self.exp_repo.get_all()
        self.view.set_budget_table(self.exp_data, self.bud_data)
