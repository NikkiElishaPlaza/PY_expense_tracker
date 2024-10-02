from Expense import Expense

separator = "=" * 50

def main():
    print(f"""{separator}\n\n             🟢 Running Expense Tracker! 🟢\n""")

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
def get_user_expense():
    print(f"""{separator}\n\n              ✨ Getting User Expense ✨\n\n{separator}\n""")

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
            "🍴 Food 🍴"
            "🏠 Home 🏠"
            "💼 Work 💼"
            "🎉 Fun 🎉"
            "🌟 Miscellaneous 🌟"
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
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"""\n{separator}\n\n     ✨ Saving User Expense ✨\n\n{separator}

    Expense name:   {expense.name}\n
    Category:       {expense.category}\n
    Amount:         PHP {expense.amount: .2f}\n
    Saving to:      {expense_file_path}

{separator}\n""")

    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


#Summarize the overall data
def summarize_expenses(expense_file_path):
    print(f"""          ✨ Summarizing User Expense ✨\n\n{separator}""")

    total_amount = 0.0
    total_number_of_expenses = 0

    try:
        with open(expense_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"\n{"Expense Name":<20} {"Amount (PHP)":<15} {"Category"}")

            for line in lines:
                components = line.strip().split(", ")
                if len(components) == 3:
                    name, amount, category = components
                    amount_float = float(amount)
                    total_amount += amount_float
                    total_number_of_expenses += 1

                    print (f"\n{name:<20} {amount_float:<15.2f} {category}")
                else:
                    print(f"Warning: Invalid line format - {line.strip()}")

        print(f"{separator}\n\nTotal Number of Expenses: {total_number_of_expenses}\n"
              f"\nTotal Amount: PHP {total_amount:.2f}\n\n" f"{separator}")
        
    except FileNotFoundError:
        print("No expenses found. Please save some expenses first.")
    except ValueError as ve:
        print(f"An error occured while summarizing expenses: {e}\n\n {separator}")
    except Exception as e:
        print(f"An error occured while summarizing expenses: {e}\n\n")


#Repeating process and adding data
def continue_input(expense: Expense, expense_file_path: str):
    while True:
        input_question = "          ✨Transaction complete ✨\n\n" + \
                        f"{separator}\n\n Would you like to add another expense? (Yes/No): "
        
        user_choice = input(f"\n{input_question} ").strip()

        if user_choice.lower() == "yes":
            print(f"\n{separator}\n\n               ✨ Repeating Process ✨\n")
            main()
            break
        elif user_choice.lower == "no":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


if __name__ == "_main_":
    main()