from Expense import Expense

separator = "=" * 50

def main():
    print(f"""{separator}\n\n Running Expense Tracker!\n""")

    expense_file_path = "expenses.csv"

    #Get user input for expense.
    expense = get_user_expense()

    #Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize expense.
    summarize_expenses(expense_file_path)

    #Repearing the process and continue adding data
    continue_input(expense, expense_file_path)

#Get expense name
def get_use_expense():
    print(f"""{separator}\n\n Getting User Expense\n\n""")

    while True:
        expense_name = input("Enter expense name: ")

        if expense_name and not any(char.isdigit() for char in expense_name):
            break
        else:
            print("Kindly enter a calid name that contains letters and not numbers.")

    print(f"\n{separator}\n")

    while True:
        try:
            expense_amount = float(input("Enter expense amount in PHP: "))
            break
        except ValueError:
            print("Kindly enter a valid number for the expense amount.")


#List categories

expense_categories = [
        "Food"
        "Home"
        "Work"
        "Fun"
        "Miscellaneous"
    ]

print(f"\n{separator}\n")

while True:
    print("Select a category: ")
    for i, category_name in enumerate(expense_categories):
        print(f"\n {i + 1}/ {category_name}\n")
    
    value_range = f"[1 - {len(expense_categories)}]"

    try:
        selected_index = int(input(f"{separator}\n\n Enter a category number {value_range}: "))-1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount= expense_amount)
        else:
            print("Invalid category. Please try again.")

    except ValueError:
        print(f"Kindly enter a valid category between 1 and {len(expense_categories)}.")


#Save the entered Data
def save_expense_to_file(Expense, expense_file_path):


def summarize_expenses():


def continue_input():




if __name__ == "_main_":
    main()