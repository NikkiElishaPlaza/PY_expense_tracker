import csv

# Sample data for accounts
accounts = [
    {"Name": "Milo", "Password": "BrownWhite", "Birth_Date": "01-01-1999", "Contact_Number":"12345", "Address": "#1 Zone 1 Bahay ni Nikki Brgy. Old QC"},
    {"Name": "Choco", "Password": "Black", "Birth_Date": "01-01-2022", "Contact_Number":"54321", "Address": "#1 Zone 1 Bahay ni Nikki Brgy. Young QC"}
]

fieldname = ["Name", "Password", "Birth_Date", "Contact_Number","Address"]

# File name for account data
filename = "Accounts_Data.csv"

# Write data to CSV file
with open(filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(accounts)

print(f"Sample account data written to {filename}")