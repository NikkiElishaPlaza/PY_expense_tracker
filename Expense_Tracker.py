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
        expense_amount = floar(input("Enter expense amount in PHP: "))
        break
    except ValueError:
        print("Kindly enter a valid number for the expense amount.")



def save_expense_to_file():


def summarize_expenses():


def continue_input():




if __name__ == "_main_":
    main()