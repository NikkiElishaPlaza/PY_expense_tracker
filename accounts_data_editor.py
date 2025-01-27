import csv
import os


class Accounts_Data_Editor:

    def __init__(self):
            
            # File name for account data
            self.filename = "Accounts_Data.csv"

            # Field Name for Account
            self.fieldname = ["Name", "Password", "Birth_Date", "Contact_Number","Address"]
            
            # Create Financials CSV file upon call of this class constructor
            self.create_financial_files(self.filename)
            pass
    
    def getFileName(self):
        print("Filename: ", self.filename)
        return self.filename
    
    def getFieldName(self):
        return self.fieldname