import os
import json

# Initialize budget data structure
budget_data = {
    "income": [],
    "expenses": [],
}

# Define the filename for data persistence
data_filename = "budget_data.json"

# Load data from the file if it exists
if os.path.exists(data_filename):
    with open(data_filename, "r") as file:
        budget_data = json.load(file)


def save_data():
    """Save budget data to a JSON file for data persistence."""
    with open(data_filename, "w") as file:
        json.dump(budget_data, file)


def add_income():
    """Add income to the budget."""
    amount = float(input("Enter the income amount: "))
    description = input("Enter a description: ")
    budget_data["income"].append({"amount": amount, "description": description})
    save_data()


def add_expense():
    """Add an expense to the budget."""
    amount = float(input("Enter the expense amount: "))
    description = input("Enter a description: ")
    budget_data["expenses"].append({"amount": amount, "description": description})
    save_data()


def calculate_budget():
    """Calculate and display the remaining budget."""
    total_income = sum(transaction["amount"] for transaction in budget_data["income"])
    total_expenses = sum(transaction["amount"] for transaction in budget_data["expenses"])
    remaining_budget = total_income - total_expenses
    print(f"\nTotal Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Budget: ${remaining_budget}")


def expense_analysis():
    """Analyze expenses by category and display spending trends."""
    expense_categories = {}
    for expense in budget_data["expenses"]:
        category = input(f"Enter the category for expense '{expense['description']}': ")
        if category not in expense_categories:
            expense_categories[category] = 0
        expense_categories[category] += expense["amount"]

    print("\n===== Expense Analysis =====")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount}")


def display_menu():
    """Display the budget tracker menu."""
    print("\n===== Personal Budget Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Budget")
    print("4. Expense Analysis")
    print("5. Exit")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        calculate_budget()
    elif choice == "4":
        expense_analysis()
    elif choice == "5":
        print("Exiting Personal Budget Tracker. Have a nice day!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
