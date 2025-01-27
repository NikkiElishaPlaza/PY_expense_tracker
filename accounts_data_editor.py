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
    
# write data to csv file
    def Add_Account(self, Name, Password, Birth_Date, Contact_Number, Address):
        filename = self.filename
        fieldname = self.fieldname

        try:
            account = {"Name": str(Name), 
                       "Password": str(Password), 
                       "Birth_Date": str(Birth_Date), 
                       "Contact_Number": str(Contact_Number), 
                       "Address": str(Address)}

            # check if the file exists and is not empty
            file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

            # check for duplicate name
            if file_exists:
                with open(filename, mode="r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["Name"] == Name:
                            # for Debugging purposes
                            print(f"Error: An account with Name = {Name} already exists.")
                            return False# Exit the function without creating the account

            with open(filename, mode="a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldname)

                # only write the header if the file is empty
                if not file_exists:
                    writer.writeheader()

                # aAppend the new account data
                writer.writerow(account)

                # for debugging purposes
                print(f"Account data with Name = {Name} has been written to {filename}")

            # create Financials CSV file
            self.create_financial_files(self.filename)

            return True
        except Exception as e:

            # error handling
            print(f"Error: {e}")

            # call return if there is an error to stop the process
            return