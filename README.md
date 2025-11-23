# Smart-expense-tracker
The Smart Expense Tracker (SET) allows users to monitor their daily spending, categorize their expenses, and receive monthly summaries of their expenses. The SET aims to improve user spending habits through simple and easy to understand expense tracking.

Objectives
To create an easy way for individuals to log daily expenses
To categorize expenses into several categories, such as Food, Travel, Shopping, Bills, etc.
To allow the user to see, update and delete entries
To create a monthly summary of spending
To store data permanently in a CSV file

*Requirement Analysis
Functional Requirements:

User can enter expense amount User can enter category (food, travel, shopping, etc.)
User can view total expenses
User can view a summary by category
User can display all expenses

Non-functional Requirements:

Easy to use
Fast response
Clear interface
Data is stored in a simple file (CSV)

*Top-Down Design

Break this project up into smaller modules.

*Main program
Input module - retrieve expense data
Storage module - store data to file
Summary module - add totals
Display module - show all expenses

This organization allows for easy and organized code.

*Algorithm Development

1. Add Expense Algorithm
    1. Ask user amount 
    2. Ask user category 
    3. Ask user description 
    4. Output all data to CSV

2. View Total Expense Algorithm 
    1. Read all expenses from file
    2. Add all amounts
    3. Output total
   
   
3. View Summary by Category Algorithm 
   1. Read data from file
   2. Group expenses by category
   3. Sum each category
   4. Output summary
  
 
4. Output All Expense Algorithm 
   1. Open file using CSV.
   2. Read each row
   3. Diplay each row in table format
