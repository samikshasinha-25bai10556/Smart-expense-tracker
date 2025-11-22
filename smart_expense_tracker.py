import csv
import os

FILE = "expenses.csv"


# Create file if doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Amount", "Category", "Description"])


# -----------------------------
# 1. Add Expense
# -----------------------------
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    amount = input("Enter amount: ")
    category = input("Enter category (Food/Travel/Bills/Shopping/Other): ")
    description = input("Enter description: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!")


# -----------------------------
# 2. View All Expenses
# -----------------------------
def view_expenses():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    if len(data) <= 1:
        print("No expenses found!")
        return

    print("\n--- All Expenses ---")
    for i, row in enumerate(data[1:], start=1):
        print(f"{i}. Date: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Description: {row[3]}")


# -----------------------------
# 3. Edit Expense
# -----------------------------
def edit_expense():
    view_expenses()

    num = int(input("Enter expense number to edit: "))

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    if num < 1 or num >= len(data):
        print("Invalid number!")
        return

    print("\nEnter new details:")
    date = input("New Date: ")
    amount = input("New Amount: ")
    category = input("New Category: ")
    description = input("New Description: ")

    data[num] = [date, amount, category, description]

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("Expense updated successfully!")


# -----------------------------
# 4. Delete Expense
# -----------------------------
def delete_expense():
    view_expenses()

    num = int(input("Enter expense number to delete: "))

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    if num < 1 or num >= len(data):
        print("Invalid number!")
        return

    data.pop(num)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("Expense deleted successfully!")


# -----------------------------
# 5. Monthly Summary
# -----------------------------
def monthly_summary():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header

        for row in reader:
            date = row[0]
            if date[3:5] == month and date[6:10] == year:
                total += float(row[1])

    print(f"Total expenses for {month}-{year}: ₹{total}")


# -----------------------------
# MAIN MENU
# -----------------------------
while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        edit_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        monthly_summary()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")