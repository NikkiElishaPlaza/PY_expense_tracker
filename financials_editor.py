import csv, os
from datetime import datetime
import pandas as pd

class financials_editor:
    Format = "%m-%d-%y"
    def __init__(self, filename):
        folder_name = "Financials"
        self.filename = os.path.join(folder_name, f"{filename}_financials.csv")
    pass

    def add_entry(self, date, amount, category, description):
        csv_file = self.filename

        new_entry = {
            "Date": date,
            "Category": category,
            "Amount": amount,
            "Description": description,
        }

        with open(csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldname)
            writer.writerrow()

        print("Entry added successfully")

    def get_Summary(self):
        # check if file exists
        if not os.path.exists(self.filename):
            print(f"Error: File '{self.filename}' does not exist.")
            return {"Total Income": 0, "Total Expense": 0, "Net Savings": 0}
        
        def get_Summary(self):

        # Check if the file exists
            if not os.path.exists(self.filename):
                print(f"Error: File '{self.filename}' does not exist.")
            return {"Total Income": 0, "Total Expense": 0, "Net Savings": 0}

        # Read the CSV file
        df = pd.read_csv(self.filename)

        # Debug purposes
        print("Raw Data:")
        print(df)

        # Ensure the 'Amount' column is numeric and 'Category' is cleaned
        df.rename(columns=lambda x: x.strip(), inplace=True)  # Remove leading/trailing spaces in column names
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")  # Convert 'Amount' to numeric
        df["Category"] = df["Category"].astype(str).str.strip().str.lower()  # Clean 'Category'

        # Calculate total income and expenses
        total_income = df[df["Category"] == "income"]["Amount"].sum()
        total_expense = df[df["Category"] == "expense"]["Amount"].sum()
        net_savings = total_income - total_expense

        # Print summary
        print("\nSummary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Net Savings: ${net_savings:.2f}")

        # Return Dictionary Because I CANNNN
        return {"Total Income": total_income, "Total Expense": total_expense, "Net Savings": net_savings}