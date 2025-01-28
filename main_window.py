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
    
    # load Acccounts Data in the Table
        self.load_accounts_data(self.filename)

        # title of Main Windows
        self.setWindowTitle("Personal Finance Tracker")

        # set Index  to Home as Default Dropping page
        self.stackedWidget.setCurrentIndex(0)

        # connecting Buttons and Stuff to Methods
        self.ADDAccount_pushButton.clicked.connect(self.addAccountPage)
        self.SelectAccount_pushButton.clicked.connect(self.financeAccountPage)
        self.RemoveAccount_pushButton.clicked.connect(self.deleteAccount)
        self.back_pushButton.clicked.connect(self.selectAccountPage)
        self.UserAccounts_tableView.selectionModel().selectionChanged.connect(self.on_row_selected)

        # accountAddPage
        self.SaveInformation_pushButton.clicked.connect(self.addAccount)

        # financialsPage
        self.Logout_pushButton.clicked.connect(self.selectAccountPage)
        self.AddFinance_pushButton.clicked.connect(self.addFinancePage)
        self.finance_back_pushButton.clicked.connect(self.financeAccountPage)

        # add Finance Page
        self.Today_checkBox.stateChanged.connect(self.checkBox_Checked)
        self.AddFinanceData_pushButton.clicked.connect(self.addFinanceData)        
 
# load table data ---------------
    def load_accounts_data(self, csv_file):
        # Create a model for the table view
        model = QStandardItemModel()
        
        with open(csv_file, mode="r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader)  # First row is assumed to be the headers
            model.setHorizontalHeaderLabels(headers)

            # Add rows to the model
            for row in reader:
                items = [QStandardItem(field) for field in row]
                model.appendRow(items)

        # set the model to the QTableView
        self.UserAccounts_tableView.setModel(model)

    def load_financial_data(self, name):
        # define the folder where financial CSV files are stored
        folder_name = "Financials"
        csv_file = os.path.join(folder_name, f"{name}_financials.csv")

        # summary Date
        summary_Data = self.FinanceManager.get_Summary()

        # For Debugging Purposes
        print(summary_Data)
        print("Total Income: ${:.2f}".format(summary_Data['Total Income']))
        print("Total Expenses: ${:.2f}".format(summary_Data['Total Expense']))
        print("Net Savings: ${:.2f}".format(summary_Data['Net Savings']))

        self.TotalIncome_label.setText(str(summary_Data['Total Income']))
        self.TotalExpenses_label.setText(str(summary_Data['Total Expense']))
        self.NetSavings_label.setText(str(summary_Data['Net Savings']))

        # create a model for the table view
        model = QStandardItemModel()

        try:
            with open(csv_file, mode="r", newline="") as file:
                reader = csv.reader(file)
                headers = next(reader)  # First row is assumed to be the headers
                model.setHorizontalHeaderLabels(headers)

                # Add rows to the model
                for row in reader:
                    items = [QStandardItem(field) for field in row]
                    model.appendRow(items)

            # set the model to the table view
            self.Finances_tableView.setModel(model)
            
        except Exception as e:
            print(f"Error loading financial data: {e}")

    def on_row_selected(self, selected, deselected):
        indexes = self.UserAccounts_tableView.selectionModel().selectedRows()
        for index in indexes:
            row_data = []
            for column in range(self.UserAccounts_tableView.model().columnCount()):
                row_data.append(self.UserAccounts_tableView.model().data(self.UserAccounts_tableView.model().index(index.row(), column)))
            
            print("Selected Row Data:", row_data)

            self.selectUserRow = row_data
            self.selectUserName = row_data[0]
            self.Username_label.setText(self.selectUserName)

            # highlight Pushbutton
            self.SelectAccount_pushButton.setStyleSheet("background-color: rgb(0, 255, 255);")  # Light Cyan for Select Account
            self.RemoveAccount_pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")  # Red for Remove Account

    def checkBox_Checked(self):
        # check if Today_checkBox is checked
        if self.Today_checkBox.isChecked():
            # disable the FinanceDate_dateEdit field
            self.FinanceDate_dateEdit.setEnabled(False)

            # set the date to today's date
            today = QDate.currentDate()  # Get today's date
            self.FinanceDate_dateEdit.setDate(today)

        else:
            # enable the FinanceDate_dateEdit field if checkbox is unchecked
            self.FinanceDate_dateEdit.setEnabled(True)

    # pages ----------------
    def selectAccountPage(self):
        # if current index is in Financials Page
        if self.stackedWidget.currentIndex() == 2:
            # create a confirmation dialog
            reply = QMessageBox.warning(self, 'Logging Out',
                                        f"Are you sure you want to logout?",
                                        QMessageBox.Yes, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                # reset Selected UserName
                self.selectUserName = ""
                self.refreshStuff()
            else:
                return
        
        self.stackedWidget.setCurrentIndex(0)

    def financeAccountPage(self):
        # if no account is selected. produce an error
        if self.selectUserRow == []:
            # create a confirmation dialog
            reply = QMessageBox.warning(self, 'No Account Selected',
                                        f"Please select a User Account!",
                                        QMessageBox.Ok)
            return
        
        # set Username State Visualization
        self.financials_username_label.setText(f"{self.selectUserName}'s Finances")

        self.FinanceManager = financials_editor(self.selectUserName)
        # load User Data
        self.load_financial_data(self.selectUserName)

        # finance Account form is index 2
        self.stackedWidget.setCurrentIndex(2)

    def addAccountPage(self):
        # add Account form is index 3
        self.stackedWidget.setCurrentIndex(3)

    def addFinancePage(self):
        # add Finance Page
        self.stackedWidget.setCurrentIndex(1)
    
        data = self.FinanceManager.get_Summary()
        print(data)
    
    # account stuff --------
    def addAccount(self):
        # get the input data
        name = self.Name_textEdit.toPlainText()
        password = self.Password_textEdit.toPlainText()
        dateOfBirth = self.DateOfBirth_dateEdit.date().toString('MM-dd-yyyy')
        contactNO = self.Contact_textEdit.toPlainText()
        address = self.Address_textEdit.toPlainText()

        # debugging purposes
        print(f"Name: {name} \nPassword: {password} \nDate Of Birth: {dateOfBirth} \nContact Number: {contactNO} \nAddress: {address}")

        # data Validations ---------------------
        # validate Name: Only letters and numbers
        if not re.match("^[a-zA-Z0-9]+$", name):
            self.show_error_dialog("Name", "Name can only contain letters and numbers.")
            # clear Data since mali naman
            self.Name_textEdit.setText("")
            return 
        
        # check for empty fields and show a dialog
        if not name:
            self.show_error_dialog("Name", "Name field doesn't contain data.")
            return 
        
        if not password:
            self.show_error_dialog("Password", "Password field doesn't contain data.")
            return 
        
        if not dateOfBirth:
            self.show_error_dialog("Date of Birth", "Date of Birth field doesn't contain data.")
            return 
        
        if not contactNO:
            self.show_error_dialog("Contact Number", "Contact Number field doesn't contain data.")
            return
        
        if not address:
            self.show_error_dialog("Address", "Address field doesn't contain data.")
            return

        # call the method to add the account
        isSuccess = self.AccountManager.Add_Account(name, password, dateOfBirth, contactNO, address)

        if not isSuccess:
                        # create a confirmation dialog
            reply = QMessageBox.warning(self, 'Existing Account Detected',
                                        f"Please enter a different Name!",
                                        QMessageBox.Ok)
            return

        # if nakalusot dito then it means that this is successful
        self.Name_textEdit.setText("")
        self.Password_textEdit.setText("")
        self.DateOfBirth_dateEdit.setDate(QDate.currentDate())
        self.Contact_textEdit.setText("")
        self.Address_textEdit.setText("")

        # refresh Stuff Here ---------------------------------
        self.refreshStuff()

    def deleteAccount(self):

        # if no account is selected. produce an error
        if self.selectUserRow == []:
            # create a confirmation dialog
            reply = QMessageBox.warning(self, 'No Account Selected',
                                        f"Please select a User Account!",
                                        QMessageBox.Ok)
            return
        
        # assuming selectUserRow is already defined elsewhere
        SelectedRowData = self.selectUserRow
        
        # get the selected name
        SelectedName = SelectedRowData[0]
        print(f"SelectedName: {SelectedName}")

        # create a confirmation dialog
        reply = QMessageBox.warning(self, 'Confirm Deletion',
                                    f"All Data of the account '{SelectedName}' will be deleted forever\n" +
                                    "Are you sure you want to delete?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # if Yes is clicked, proceed with the deletion
        if reply == QMessageBox.Yes:
            # delete Data
            self.AccountManager.Delete_Account(SelectedName)
            
            # refresh stuff here ---------------------------------
            self.refreshStuff()

    # finance suff --------

    def addFinanceData(self):
        date = self.FinanceDate_dateEdit.date().toString('MM-dd-yyyy') 
        category = self.FinanceCategory_comboBox.currentText()  
        description = self.Description_textEdit.toPlainText() 

        try:
            amount = float(self.Amount_textEdit.toPlainText())
        except ValueError:
            reply = QMessageBox.warning(self, 'Value Error',
                                        f"Please input integer or decimal for the amount",
                                        QMessageBox.Ok)
            self.Amount_textEdit.setText()
            
            print("Invalid amount input")
            return
        
        self.FinanceManager.add_entry(date, amount, category, description)

        # if nakalusot dito ibigsahin tama ang porcess
        self.Amount_textEdit.setText("")
        self.FinanceDate_dateEdit.setDate(QDate(2000, 1, 1)) 
        self.FinanceCategory_comboBox.setCurrentIndex(0)
        self.Description_textEdit.setText("")
        self.Today_checkBox.setChecked(False)

        self.financeAccountPage()
        print(date, category, amount, description)

    def show_error_dialog(self, field, message):
        # message box to show the error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Input Error")
        msg.setText(message)

        # contents of the Message Box
        msg.setInformativeText(f"Please provide a valid {field}.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def refreshStuff(self):
        
        # refresh variable
        self.selectUserRow = []
        # refresh userlabel selected
        self.Username_label.setText("-")

        # reset push buttons
        self.SelectAccount_pushButton.setStyleSheet("background-color: rgb(123, 170, 170);")  # Light Cyan for Select Account
        self.RemoveAccount_pushButton.setStyleSheet("background-color: rgb(170, 123, 123);")  # Red for Remove Account
        
        # reload data
        self.load_accounts_data(self.filename)
        # refresh the row selector
        self.UserAccounts_tableView.selectionModel().selectionChanged.connect(self.on_row_selected)

        # if current page is not financials page
        if not self.stackedWidget.currentIndex() == 2:
            # after adding an Account go back to the select account page
            self.selectAccountPage()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())