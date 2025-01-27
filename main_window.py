import sys, csv, os, re
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDate

from accounts_data_editor import accounts_data_editor
from financials_editor import financials_editor

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # customized stuff values
        self.DateOfBirth_dateEdit.setDate(QDate.currentDate())
        # initial colors for push button
        self.SelectAccount_pushButton.setStyleSheet("background-color: rgb(123, 170, 170);")  # light cyan for Select Account
        self.RemoveAccount_pushButton.setStyleSheet("background-color: rgb(170, 123, 123);")  # red for Remove Account

        # global variables here
        # create an object for accounts data editor
        self.AccountManager = accounts_data_editor()
        self.FinanceManager = ""
        self.filename = "Accounts_Data.csv"
        self.selectUserRow = []
        self.selectUserName = ""