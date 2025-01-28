# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(725, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(725, 459))
        MainWindow.setMaximumSize(QSize(725, 459))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 721, 411))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.UserSelection_Page = QWidget()
        self.UserSelection_Page.setObjectName(u"UserSelection_Page")
        self.widget_8 = QWidget(self.UserSelection_Page)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(20, 20, 491, 391))
        self.widget_8.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.UserAccounts_tableView = QTableView(self.widget_8)
        self.UserAccounts_tableView.setObjectName(u"UserAccounts_tableView")
        self.UserAccounts_tableView.setGeometry(QRect(10, 10, 471, 371))
        self.UserAccounts_tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_9 = QWidget(self.UserSelection_Page)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(510, 20, 191, 391))
        self.widget_9.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"")
        self.ADDAccount_pushButton = QPushButton(self.widget_10)
        self.ADDAccount_pushButton.setObjectName(u"ADDAccount_pushButton")
        self.ADDAccount_pushButton.setGeometry(QRect(0, 20, 173, 24))
        self.ADDAccount_pushButton.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.RemoveAccount_pushButton = QPushButton(self.widget_10)
        self.RemoveAccount_pushButton.setObjectName(u"RemoveAccount_pushButton")
        self.RemoveAccount_pushButton.setGeometry(QRect(0, 50, 173, 24))
        self.RemoveAccount_pushButton.setStyleSheet(u"background-color: rgb(170, 123, 123);")
        self.Username_label = QLabel(self.widget_10)
        self.Username_label.setObjectName(u"Username_label")
        self.Username_label.setGeometry(QRect(10, 300, 151, 31))
        self.Username_label.setStyleSheet(u" font: 700 20pt \"Segoe UI\";")
        self.SelectedUsername_label = QLabel(self.widget_10)
        self.SelectedUsername_label.setObjectName(u"SelectedUsername_label")
        self.SelectedUsername_label.setGeometry(QRect(10, 260, 151, 31))
        self.SelectedUsername_label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.widget_10)

        self.SelectAccount_pushButton = QPushButton(self.widget_9)
        self.SelectAccount_pushButton.setObjectName(u"SelectAccount_pushButton")
        self.SelectAccount_pushButton.setStyleSheet(u"background-color: rgb(123, 170, 170);")

        self.verticalLayout.addWidget(self.SelectAccount_pushButton)

        self.stackedWidget.addWidget(self.UserSelection_Page)
        self.AddFinance_Page = QWidget()
        self.AddFinance_Page.setObjectName(u"AddFinance_Page")
        self.widget_7 = QWidget(self.AddFinance_Page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(20, 20, 681, 321))
        self.widget_7.setStyleSheet(u"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    font-family: \"Arial\";\n"
"    padding: 5px;\n"
"}\n"
"QLineEdit {\n"
"    font-size: 14px;\n"
"    font-family: \"Arial\";\n"
"    padding: 5px;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    background-color: #f9f9f9;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078D7; /* Blue border for focus */\n"
"    background-color: #ffffff; /* Slightly brighter background */\n"
"}")
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 200, 171, 31))
        self.Amount_textEdit = QTextEdit(self.widget_7)
        self.Amount_textEdit.setObjectName(u"Amount_textEdit")
        self.Amount_textEdit.setGeometry(QRect(20, 230, 271, 31))
        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 35, 171, 31))
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 120, 171, 31))
        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(350, 30, 171, 31))
        self.Description_textEdit = QTextEdit(self.widget_7)
        self.Description_textEdit.setObjectName(u"Description_textEdit")
        self.Description_textEdit.setGeometry(QRect(350, 65, 291, 201))
        self.FinanceDate_dateEdit = QDateEdit(self.widget_7)
        self.FinanceDate_dateEdit.setObjectName(u"FinanceDate_dateEdit")
        self.FinanceDate_dateEdit.setGeometry(QRect(20, 70, 151, 22))
        self.FinanceCategory_comboBox = QComboBox(self.widget_7)
        self.FinanceCategory_comboBox.addItem("")
        self.FinanceCategory_comboBox.addItem("")
        self.FinanceCategory_comboBox.setObjectName(u"FinanceCategory_comboBox")
        self.FinanceCategory_comboBox.setGeometry(QRect(20, 150, 151, 22))
        self.Today_checkBox = QCheckBox(self.widget_7)
        self.Today_checkBox.setObjectName(u"Today_checkBox")
        self.Today_checkBox.setGeometry(QRect(180, 65, 76, 20))
        self.AddFinanceData_pushButton = QPushButton(self.AddFinance_Page)
        self.AddFinanceData_pushButton.setObjectName(u"AddFinanceData_pushButton")
        self.AddFinanceData_pushButton.setGeometry(QRect(290, 370, 91, 31))
        self.AddFinanceData_pushButton.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.finance_back_pushButton = QPushButton(self.AddFinance_Page)
        self.finance_back_pushButton.setObjectName(u"finance_back_pushButton")
        self.finance_back_pushButton.setGeometry(QRect(10, 0, 75, 24))
        self.finance_back_pushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.stackedWidget.addWidget(self.AddFinance_Page)
        self.Financials_Page = QWidget()
        self.Financials_Page.setObjectName(u"Financials_Page")
        self.widget = QWidget(self.Financials_Page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 691, 134))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TotalIncome_label = QLabel(self.widget_3)
        self.TotalIncome_label.setObjectName(u"TotalIncome_label")
        self.TotalIncome_label.setStyleSheet(u"    background-color: rgb(85, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    text-align: center; /* Center align text */\n"
"    qproperty-alignment: 'AlignCenter'; /* PyQt specific alignment */")

        self.verticalLayout_2.addWidget(self.TotalIncome_label)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"    background-color: rgb(128, 128, 0); /* Slightly lighter shade to complement */\n"
"    color: rgb(255, 255, 255); /* White text for readability */\n"
"    font-size: 20px; /* Slightly larger font for emphasis */\n"
"    font-weight: bold; /* Bold text to highlight importance */\n"
"    border-radius: 10px; /* Smooth rounded corners for consistency */\n"
"    padding: 12px; /* Add padding for proper spacing */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    qproperty-alignment: 'AlignCenter'; /* PyQt-specific centering */")

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TotalExpenses_label = QLabel(self.widget_4)
        self.TotalExpenses_label.setObjectName(u"TotalExpenses_label")
        self.TotalExpenses_label.setStyleSheet(u"    background-color: rgb(85, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    text-align: center; /* Center align text */\n"
"    qproperty-alignment: 'AlignCenter'; /* PyQt specific alignment */")

        self.verticalLayout_3.addWidget(self.TotalExpenses_label)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"    background-color: rgb(128, 128, 0); /* Slightly lighter shade to complement */\n"
"    color: rgb(255, 255, 255); /* White text for readability */\n"
"    font-size: 20px; /* Slightly larger font for emphasis */\n"
"    font-weight: bold; /* Bold text to highlight importance */\n"
"    border-radius: 10px; /* Smooth rounded corners for consistency */\n"
"    padding: 12px; /* Add padding for proper spacing */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    qproperty-alignment: 'AlignCenter'; /* PyQt-specific centering */")

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.NetSavings_label = QLabel(self.widget_5)
        self.NetSavings_label.setObjectName(u"NetSavings_label")
        self.NetSavings_label.setStyleSheet(u"    background-color: rgb(85, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    text-align: center; /* Center align text */\n"
"    qproperty-alignment: 'AlignCenter'; /* PyQt specific alignment */")

        self.verticalLayout_4.addWidget(self.NetSavings_label)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"    background-color: rgb(128, 128, 0); /* Slightly lighter shade to complement */\n"
"    color: rgb(255, 255, 255); /* White text for readability */\n"
"    font-size: 20px; /* Slightly larger font for emphasis */\n"
"    font-weight: bold; /* Bold text to highlight importance */\n"
"    border-radius: 10px; /* Smooth rounded corners for consistency */\n"
"    padding: 12px; /* Add padding for proper spacing */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    qproperty-alignment: 'AlignCenter'; /* PyQt-specific centering */")

        self.verticalLayout_4.addWidget(self.label_7)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_2 = QWidget(self.Financials_Page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 170, 711, 251))
        self.Finances_tableView = QTableView(self.widget_2)
        self.Finances_tableView.setObjectName(u"Finances_tableView")
        self.Finances_tableView.setGeometry(QRect(0, 0, 691, 221))
        self.AddFinance_pushButton = QPushButton(self.widget_2)
        self.AddFinance_pushButton.setObjectName(u"AddFinance_pushButton")
        self.AddFinance_pushButton.setGeometry(QRect(640, 200, 51, 41))
        self.AddFinance_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    border: none;\n"
"    border-radius: 30px;  /* Makes the button round */\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    width: 60px;\n"
"    height: 60px;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease;  /* Smooth transition for color change */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 140, 105);  /* Hover effect color */\n"
"}\n"
"")
        self.Logout_pushButton = QPushButton(self.Financials_Page)
        self.Logout_pushButton.setObjectName(u"Logout_pushButton")
        self.Logout_pushButton.setGeometry(QRect(640, 0, 81, 31))
        self.Logout_pushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.financials_username_label = QLabel(self.Financials_Page)
        self.financials_username_label.setObjectName(u"financials_username_label")
        self.financials_username_label.setGeometry(QRect(10, 0, 621, 16))
        self.financials_username_label.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"text-align: center;")
        self.stackedWidget.addWidget(self.Financials_Page)
        self.PersonalInformation_page = QWidget()
        self.PersonalInformation_page.setObjectName(u"PersonalInformation_page")
        self.SaveInformation_pushButton = QPushButton(self.PersonalInformation_page)
        self.SaveInformation_pushButton.setObjectName(u"SaveInformation_pushButton")
        self.SaveInformation_pushButton.setGeometry(QRect(320, 360, 91, 31))
        self.SaveInformation_pushButton.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.widget_6 = QWidget(self.PersonalInformation_page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(20, 30, 681, 321))
        self.widget_6.setStyleSheet(u"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    font-family: \"Arial\";\n"
"    padding: 5px;\n"
"}\n"
"QLineEdit {\n"
"    font-size: 14px;\n"
"    font-family: \"Arial\";\n"
"    padding: 5px;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    background-color: #f9f9f9;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078D7; /* Blue border for focus */\n"
"    background-color: #ffffff; /* Slightly brighter background */\n"
"}")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 15, 171, 31))
        self.Name_textEdit = QTextEdit(self.widget_6)
        self.Name_textEdit.setObjectName(u"Name_textEdit")
        self.Name_textEdit.setGeometry(QRect(10, 50, 271, 31))
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 165, 171, 31))
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 171, 31))
        self.Password_textEdit = QTextEdit(self.widget_6)
        self.Password_textEdit.setObjectName(u"Password_textEdit")
        self.Password_textEdit.setGeometry(QRect(10, 130, 271, 31))
        self.Address_textEdit = QTextEdit(self.widget_6)
        self.Address_textEdit.setObjectName(u"Address_textEdit")
        self.Address_textEdit.setGeometry(QRect(360, 50, 271, 31))
        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(360, 15, 171, 31))
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 95, 171, 31))
        self.Contact_textEdit = QTextEdit(self.widget_6)
        self.Contact_textEdit.setObjectName(u"Contact_textEdit")
        self.Contact_textEdit.setGeometry(QRect(360, 130, 271, 31))
        self.DateOfBirth_dateEdit = QDateEdit(self.widget_6)
        self.DateOfBirth_dateEdit.setObjectName(u"DateOfBirth_dateEdit")
        self.DateOfBirth_dateEdit.setGeometry(QRect(10, 200, 121, 22))
        self.name_stateViz_label = QLabel(self.widget_6)
        self.name_stateViz_label.setObjectName(u"name_stateViz_label")
        self.name_stateViz_label.setGeometry(QRect(280, 50, 21, 31))
        self.name_stateViz_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.address_stateViz_label = QLabel(self.widget_6)
        self.address_stateViz_label.setObjectName(u"address_stateViz_label")
        self.address_stateViz_label.setGeometry(QRect(630, 50, 21, 31))
        self.address_stateViz_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.contact_stateViz_label = QLabel(self.widget_6)
        self.contact_stateViz_label.setObjectName(u"contact_stateViz_label")
        self.contact_stateViz_label.setGeometry(QRect(630, 130, 21, 31))
        self.contact_stateViz_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.password_stateViz_label = QLabel(self.widget_6)
        self.password_stateViz_label.setObjectName(u"password_stateViz_label")
        self.password_stateViz_label.setGeometry(QRect(280, 130, 21, 31))
        self.password_stateViz_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.bday_stateViz_label = QLabel(self.widget_6)
        self.bday_stateViz_label.setObjectName(u"bday_stateViz_label")
        self.bday_stateViz_label.setGeometry(QRect(130, 200, 21, 31))
        self.bday_stateViz_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.bday_stateViz_label.raise_()
        self.password_stateViz_label.raise_()
        self.contact_stateViz_label.raise_()
        self.address_stateViz_label.raise_()
        self.name_stateViz_label.raise_()
        self.label_2.raise_()
        self.Name_textEdit.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.Password_textEdit.raise_()
        self.Address_textEdit.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.Contact_textEdit.raise_()
        self.DateOfBirth_dateEdit.raise_()
        self.back_pushButton = QPushButton(self.PersonalInformation_page)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setGeometry(QRect(10, 0, 75, 24))
        self.back_pushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.stackedWidget.addWidget(self.PersonalInformation_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 725, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ADDAccount_pushButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.RemoveAccount_pushButton.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.Username_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.SelectedUsername_label.setText(QCoreApplication.translate("MainWindow", u"Selected Name:", None))
        self.SelectAccount_pushButton.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.FinanceCategory_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Income", None))
        self.FinanceCategory_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Expense", None))

        self.Today_checkBox.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.AddFinanceData_pushButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.finance_back_pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.TotalIncome_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Income", None))
        self.TotalExpenses_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Expenses", None))
        self.NetSavings_label.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Net Savings", None))
        self.AddFinance_pushButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.Logout_pushButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.financials_username_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.SaveInformation_pushButton.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.name_stateViz_label.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.address_stateViz_label.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.contact_stateViz_label.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.password_stateViz_label.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.bday_stateViz_label.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.back_pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi