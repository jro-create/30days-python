# ---------------------------------------
# 🧩 Mini Project: Expense Tracker
# ---------------------------------------

import json
import os

# File where we’ll store data
FILE_PATH = "expenses.json"

# ---------------------------------------
# Helper: Load existing data
# ---------------------------------------
def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []  # No file yet → return empty list
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("⚠️ Corrupted file detected. Starting fresh.")
            return []

# ---------------------------------------
# Helper: Save data
# ---------------------------------------
def save_expenses(expenses):
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)
    print("💾 Expenses saved successfully!")

# ---------------------------------------
# Core: Add new expense
# ---------------------------------------
def add_expense(expenses):
    try:
        description = input("Enter expense description: ").strip()
        amount = float(input("Enter amount ($): "))
        category = input("Enter category (food, rent, etc.): ").strip().lower()

        expense = {"description": description, "amount": amount, "category": category}
        expenses.append(expense)
        print(f"✅ Added: {description} (${amount:.2f}) in {category}")
    except ValueError:
        print("⚠️ Invalid amount. Please enter a number.")

# ---------------------------------------
# Core: View all expenses
# ---------------------------------------
def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses recorded yet.")
        return
    print("\n--- Expense List ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['description']} - ${e['amount']:.2f} ({e['category']})")
    print("--------------------")

# ---------------------------------------
# Core: Total spending
# ---------------------------------------
def show_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"💰 Total spending: ${total:.2f}")

# ---------------------------------------
# Menu loop
# ---------------------------------------
def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("👋 Exiting. See you next session!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# ---------------------------------------
# Entry point
# ---------------------------------------
if __name__ == "__main__":
    main()

