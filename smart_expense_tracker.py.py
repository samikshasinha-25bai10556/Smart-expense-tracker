import csv 
import os

FILE = "expenses.csv"

#create file if doesn't exist 
if not os.path.exists(FILE):
    with open(FILE, "w" , newline="") as f :
           writer = csv.writer(f)
           writer.writerow(["Date" , "Amount" , "Category" , "Description"])


#1. Add Expense 

def add_expense():
   date = input("Enter date (DD-MM-YYYY): ")
   amount = input("Enter amount: ")
   category= input("Enter category (Food/Travel)/Bills/Shopping/Other): ")
   description = input("Enter description: ")

   with open(FILE, "a" , newline="") as f:
     writer= csv.writer(f)
     writer.writerow([date, amount, category, description])

print("Expense added successfully ")
 
 #2.view all expense

def view_expenses():
   with open(FILE, "r") as f:
         reader = csv.reader(f)
         data = list(reader)

   if len(data) <=1:
    print("No expenses found!")
    return
 
   print("\n--- all expenses---")
   for i, row in enumerate(data[1:], start=1):
        print(f"{i}. Date: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Description: {row[3]}")
       
#3. edit expense

def edit_expense():
    view_expenses()

    num = int(input("enter expense number to edit:"))

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data=list(reader)

    if num < 1 or num >= len(data):
        print("invalid number")
        return

    print("\n enter new details:")
    data=input("new data:")
    amount=input("new amount:")
    category=input("new category:")
    description=input("new description:")

    data[num] = [data, amount, category, description]

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("expense updated successfully")


  #4. delete expense
  
def delete_expense():
    view_expenses()

    num = int(input("enter expense number to edit: "))

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    if num < 1 and num >= len(data):
        print("invalid number")
        return

    data.pop(num)

    with open(FILE, "w", newline="") as f :
        writer = csv.writer(f)
        writer.writerows(data)

    print("expense deleted successfully")

    #5. Monthly summary 

def monthly_summary():
     month = input("Enter month(MM): ")
     year = input("Enter year(YYYY): ")

     total = 0

     with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            date = row[0]
            if date[3:5] == month and date[6:10] == year:
               total+=float(row[1])

     print(f"Total expenses for {month}-{year}: {total}")

    #MAIN MENUE
while True:
    print("\n--- smart expense tracker---")
    print("1. add expense")
    print("2. view all expense")
    print("3. edit expense ")
    print("4. delete expense ")
    print("5. monthly summary ")
    print("6. exit")

    choice=input("enter your choice:")

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
             print("goodbye")
             break
    else:
         print("invalid choice, try again")

             



















