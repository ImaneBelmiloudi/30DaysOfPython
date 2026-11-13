file = "expense.txt"

def welcome():
    print("Personal Expenses Tracker ")
    print("---------------------------")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expenses")
    print("5. Exit")
    print("----------------------------")

def load_expenses():
    expenses = []

    try:
        with open(file, "r") as f:
            for line in f:
                category,amount =line.strip().split(",")
                expenses.append({"category":category , "amount":amount}) 

    except FileNotFoundError:
        print("File doesnt exist")
    except Exception as e:
        print(e)

def save_expenses(expenses):
    with open(file, "w") as f:
        for e in expenses:
            f.write(f"{e["category"]},{e["amount"]}")


def add_expense(expenses):
    try:
        category = input("Enter your category:")
        amount = float(input("Enter your amount :"))
        expenses.append({"category": category , "amount":amount})
        save_expenses(expenses)

    except ValueError:
        print("Invalid amount input.")

    except Exception as e:
        print(e)

def view_expense(expenses):
    print("\nExpense:")
    i = 1
    for e in expenses :
        print(f"{i}.{e["category"]} = {e["amount"]}$")
    print()

def total_expense(expenses):
    total = 0
    for e in expenses:
        total += e["amount"]
    print(f"Your Total Expenditure is : {total}$")

def remove_expense(expenses):
    if not expenses :
        print("\n There are no expenses to remove ")
        return
    
    view_expenses(expenses)
    try:
        number = int(input("Enter your number:"))
        if number >= 1 and number <= len(expenses):
            removed = expenses.pop(number -1)
