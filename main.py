class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    
    def __str__(self):
        return f"{self.date} - {self.category}: ${self.amount} - {self.description}"

def add_expense(expenses):
    print("Enter the following details for your expense:")
    amount = float(input("Amount: $"))
    category = input("Category (e.g., Food, Utilities, Entertainment): ")
    description = input("Description: ")
    date = input("Date (YYYY-MM-DD): ")

    new_expense = Expense(amount, category, description, date)
    expenses.append(new_expense)
    print("Expense added successfully!")
def display_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    print("\nAll Expenses:")
    for expense in expenses:
        print(expense)
import csv

def save_expenses_to_file(expenses, filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])
        for expense in expenses:
            writer.writerow([expense.date, expense.amount, expense.category, expense.description])

def load_expenses_from_file(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                date, amount, category, description = row
                expense = Expense(float(amount), category, description, date)
                expenses.append(expense)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty expense list.")
    return expenses
def main():
    expenses = load_expenses_from_file()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Save Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            save_expenses_to_file(expenses)
            print("Expenses saved successfully!")
        elif choice == '4':
            save_expenses_to_file(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
def edit_expense(expenses):
    display_expenses(expenses)
    
    # Select the expense to edit
    try:
        expense_index = int(input("Enter the number of the expense you want to edit: ")) - 1
        
        if expense_index < 0 or expense_index >= len(expenses):
            print("Invalid expense number.")
            return
        
        # Get new details from the user
        print("Enter new details (leave empty to keep current value):")
        
        amount = input(f"Amount (${expenses[expense_index].amount}): ")
        category = input(f"Category ({expenses[expense_index].category}): ")
        description = input(f"Description ({expenses[expense_index].description}): ")
        date = input(f"Date ({expenses[expense_index].date}): ")
        
        # Update the expense only if new data is provided
        if amount:
            expenses[expense_index].amount = float(amount)
        if category:
            expenses[expense_index].category = category
        if description:
            expenses[expense_index].description = description
        if date:
            expenses[expense_index].date = date
        
        print("Expense updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
def delete_expense(expenses):
    display_expenses(expenses)
    
    try:
        expense_index = int(input("Enter the number of the expense you want to delete: ")) - 1
        
        if expense_index < 0 or expense_index >= len(expenses):
            print("Invalid expense number.")
            return
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete this expense? (yes/no): ").strip().lower()
        if confirm == 'yes':
            expenses.pop(expense_index)
            print("Expense deleted successfully!")
        else:
            print("Deletion canceled.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
def search_expenses(expenses):
    search_term = input("Enter a search term (category, date, or amount): ").strip()
    
    filtered_expenses = [expense for expense in expenses 
                         if search_term.lower() in expense.category.lower() or
                            search_term in expense.date or
                            search_term in str(expense.amount)]
    
    if filtered_expenses:
        print("\nSearch Results:")
        for expense in filtered_expenses:
            print(expense)
    else:
        print("No matching expenses found.")
from collections import defaultdict
from datetime import datetime

def generate_report(expenses):
    print("\nChoose a report type:")
    print("1. Total spending per category")
    print("2. Total spending in a specific month")
    print("3. Average daily spending")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        category_totals = defaultdict(float)
        for expense in expenses:
            category_totals[expense.category] += expense.amount
        
        print("\nTotal spending per category:")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
    
    elif choice == '2':
        month = input("Enter the month (YYYY-MM): ")
        total_spent = 0
        for expense in expenses:
            if expense.date.startswith(month):
                total_spent += expense.amount
        
        print(f"\nTotal spending for {month}: ${total_spent:.2f}")
    
    elif choice == '3':
        total_spent = sum(expense.amount for expense in expenses)
        unique_dates = {expense.date for expense in expenses}
        average_daily_spending = total_spent / len(unique_dates) if unique_dates else 0
        
        print(f"\nAverage daily spending: ${average_daily_spending:.2f}")
    else:
        print("Invalid choice. No report generated.")
import matplotlib.pyplot as plt

def visualize_expenses(expenses):
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount
    
    categories = list(category_totals.keys())
    totals = list(category_totals.values())
    
    # Pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Spending per Category')
    plt.show()
import shutil

def backup_expenses(expenses, filename="expenses.csv"):
    backup_filename = f"backup_{filename}"
    shutil.copy(filename, backup_filename)
    print(f"Backup created: {backup_filename}")

def restore_expenses(filename="expenses.csv"):
    try:
        backup_filename = f"backup_{filename}"
        shutil.copy(backup_filename, filename)
        print(f"Data restored from: {backup_filename}")
    except FileNotFoundError:
        print("Backup file not found. No data restored.")
def authenticate_user():
    password = "my_secure_password"  # This could be encrypted in real applications
    entered_password = input("Enter password to access the expense tracker: ")
    
    if entered_password == password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False
def main():
    expenses = load_expenses_from_file()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. Display Expenses")
        print("5. Search Expenses")
        print("6. Generate Report")
        print("7. Visualize Expenses (Graph)")
        print("8. Save Expenses")
        print("9. Backup Expenses")
        print("10. Restore Expenses")
        print("11. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            edit_expense(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            display_expenses(expenses)
        elif choice == '5':
            search_expenses(expenses)
        elif choice == '6':
            generate_report(expenses)
        elif choice == '7':
            visualize_expenses(expenses)
        elif choice == '8':
            save_expenses_to_file(expenses)
        elif choice == '9':
            backup_expenses(expenses)
        elif choice == '10':
            restore_expenses()
        elif choice == '11':
            save_expenses_to_file(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
import matplotlib.pyplot as plt
from collections import defaultdict

def visualize_expenses(expenses):
    print("\nChoose a visualization option:")
    print("1. Spending per Category (Pie Chart)")
    print("2. Spending by Category (Bar Chart)")
    print("3. Spending Over Time (Line Chart)")
    choice = input("Enter your choice: ")

    if choice == '1':  # Pie Chart
        category_totals = defaultdict(float)
        for expense in expenses:
            category_totals[expense.category] += expense.amount
        
        categories = list(category_totals.keys())
        totals = list(category_totals.values())
        
        plt.figure(figsize=(8, 6))
        plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Spending per Category')
        plt.show()

    elif choice == '2':  # Bar Chart
        category_totals = defaultdict(float)
        for expense in expenses:
            category_totals[expense.category] += expense.amount
        
        categories = list(category_totals.keys())
        totals = list(category_totals.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(categories, totals, color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Total Spending')
        plt.title('Spending by Category')
        plt.show()

    elif choice == '3':  # Line Chart
        dates = sorted({expense.date for expense in expenses})
        date_totals = {date: 0 for date in dates}
        for expense in expenses:
            date_totals[expense.date] += expense.amount

        plt.figure(figsize=(10, 6))
        plt.plot(list(date_totals.keys()), list(date_totals.values()), marker='o', color='orange')
        plt.xlabel('Date')
        plt.ylabel('Total Spending')
        plt.title('Spending Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    else:
        print("Invalid choice. No visualization created.")
import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + hashed

def verify_password(stored_password, entered_password):
    salt = stored_password[:16]
    stored_hash = stored_password[16:]
    entered_hash = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), salt, 100000)
    return stored_hash == entered_hash

def authenticate_user():
    users_file = "users.csv"
    if not os.path.exists(users_file):
        print("No users found. Please set up an account.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed = hash_password(password)
        with open(users_file, 'w') as file:
            file.write(f"{username},{hashed.hex()}\n")
        print("Account created successfully!")
        return True

    username = input("Username: ")
    password = input("Password: ")

    with open(users_file, 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and verify_password(bytes.fromhex(stored_password), password):
                print("Authentication successful.")
                return True

    print("Authentication failed.")
    return False
import tkinter as tk
from tkinter import messagebox, ttk

def gui_expense_tracker():
    root = tk.Tk()
    root.title("Expense Tracker")

    expenses = load_expenses_from_file()

    # Add Expense
    def add_expense_gui():
        amount = amount_entry.get()
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()

        if not (amount and category and description and date):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        try:
            amount = float(amount)
            new_expense = Expense(amount, category, description, date)
            expenses.append(new_expense)
            update_expense_list()
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")

    # Update Expense List
    def update_expense_list():
        expense_list.delete(*expense_list.get_children())
        for i, expense in enumerate(expenses, 1):
            expense_list.insert("", "end", values=(i, expense.date, expense.category, f"${expense.amount:.2f}", expense.description))

    # GUI Components
    tk.Label(root, text="Amount ($):").grid(row=0, column=0)
    tk.Label(root, text="Category:").grid(row=1, column=0)
    tk.Label(root, text="Description:").grid(row=2, column=0)
    tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0)

    amount_entry = tk.Entry(root)
    category_entry = tk.Entry(root)
    description_entry = tk.Entry(root)
    date_entry = tk.Entry(root)

    amount_entry.grid(row=0, column=1)
    category_entry.grid(row=1, column=1)
    description_entry.grid(row=2, column=1)
    date_entry.grid(row=3, column=1)

    tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2)

    columns = ("#", "Date", "Category", "Amount", "Description")
    expense_list = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        expense_list.heading(col, text=col)
    expense_list.grid(row=5, column=0, columnspan=2, pady=10)

    update_expense_list()

    root.mainloop()

# Call the GUI
gui_expense_tracker()
