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
        
# create a CSV file for each Account
    def create_financial_files(self, source_filename):
        try:
            # define the folder name
            folder_name = "Financials"

            # create the folder if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # check if the source file exists
            if not os.path.exists(source_filename):
                print(f"Error: File {source_filename} does not exist.")
                return

            # open the source CSV file for reading
            with open(source_filename, mode="r", newline="") as source_file:
                reader = csv.DictReader(source_file)

                for row in reader:
                    # extract the Name from the current row
                    name = row.get("Name")
                    if not name:
                        print("Skipping row: Missing 'Name' field.")
                        continue

                    # generate the new file path inside the Financials folder
                    new_filename = os.path.join(folder_name, f"{name}_financials.csv")

                    # check if the financial file already exists
                    if not os.path.exists(new_filename):
                        # create a new file with the custom header
                        with open(new_filename, mode="w", newline="") as new_file:
                            writer = csv.DictWriter(
                                new_file,
                                fieldnames=["Date", "Amount", "Category", "Description"]
                            )
                            writer.writeheader()
                        print(f"Created file with header: {new_filename}")
                    else:
                        print(f"File already exists: {new_filename}")

        except Exception as e:
            print(f"Error: {e}")

    def delete_financial_file(self, name):
        try:
            # define the folder name where financial files are stored
            folder_name = "Financials"

            # construct the file path
            file_path = os.path.join(folder_name, f"{name}_financials.csv")

            # check if the file exists
            if os.path.exists(file_path):
                # delete the file
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted successfully.")
            else:
                print(f"Error: File '{file_path}' does not exist.")
        except Exception as e:
            print(f"Error: {e}")