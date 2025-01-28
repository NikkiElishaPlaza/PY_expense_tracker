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