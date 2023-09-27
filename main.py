import sys
from PySide6.QtWidgets import QApplication
from bookkeeper.view.main_window import MainWindow
from bookkeeper.repository.sqlite_repository import SqliteRepository
from bookkeeper.presenter.expense_presenter import Presenter
from bookkeeper.models.budget import Budget
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category

DB_NAME = 'database/main.db'

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = MainWindow()
    cat_repo = SqliteRepository[Category](DB_NAME, Category)
    # exp_repo = SqliteRepository[Expense](DB_NAME, Expense)
    # bud_repo = SQLiteRepository[Budget](DB_NAME, Budget)

    window = Presenter(view, cat_repo)
    window.show()
    app.exec()