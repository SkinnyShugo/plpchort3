#import statement is used to include external modules or libraries into your program.
#modules and libraries refer to collections of code that provide additional functionality to your programs.
import json

# Initialize variables
income = 0.0
expenses = []
savings = 0.0

# Load transaction data from file
# a function is a named block of reusable code that performs a specific task. 
def load_data():
    global income, expenses, savings #global function is used to indicate that a variable inside a function should be treated as a global variable, meaning it can be accessed and modified from both inside and outside the function's scope.
    try:
        with open("transactions.json", "r") as file:
            data = json.load(file)
            income = data.get("income", 0.0)
            expenses = data.get("expenses", [])
            savings = data.get("savings", 0.0)
    except FileNotFoundError: #statement is used in exception handling to catch and handle a specific type of exception, which in this case is the FileNotFoundError exception.
        pass

# Save transaction data to file
def save_data():
    data = {
        "income": income,
        "expenses": expenses,
        "savings": savings
    }
    with open("transactions.json", "w") as file:
        json.dump(data, file)

#add that income
def add_income():
    global income
    amount = float(input("Enter income amount"))
    income += amount
    print(f"income of {amount} add successfully!!!")

#add that expenses
def add_expense():
    global expenses
    description = input("Enter expense description")
    amount = float(input("Enter expense amount"))
    category = input("Enter expense category")
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully!!!")

#calculate the savings
def calculate_savings():
    global savings
    savings = income - sum(expense["amount"] for expense in expenses)
    print(f"Total savings: {savings}")

#generating report of expenses by the category
def generate_expense_report_by_category():
    category = input("Enter your category: ")
    total_amount = sum(expense["amount"] for expense in expenses if expense["category"] == category)
    print(f"Total for {category} is: {total_amount}")


def main():
    load_data()

    while True:
        print("===== Welcome to the Personal Finanace Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate savings")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            calculate_savings()
        elif choice == "4":
            generate_expense_report_by_category()
        elif choice == "5":
            save_data()
            print("Thank for using PFT but you need to save more")
            break
        else:
            print("Invalid choice. Please call again or try again")

if __name__ == "__main__":
    main()