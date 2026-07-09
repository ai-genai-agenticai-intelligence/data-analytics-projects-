# Expence Tracker Project

expenses = [] #list of expenses in form of dictionary
print('Welcome to Expense Tracker : You should spend less')

while True:
    print("====MENU====")
    print("1 .Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spend")
    print("4. Exit")

    choise =int(input("Please Enter Your Choise: "))


# Add Expense
    if(choise ==1):
        date = input("On which date did you spend the money?")
        category = input("Enter Category (Food, Travel, Shopping, Rent, Bills, Entertainment, Healthcare, Salary, Grocery, Fuel, Others): ")
        description = input("Enter Description (e.g., Lunch, Uber Ride, Monthly Rent, Electricity Bill, Salary, Grocery Shopping): ")
        amount = float(input("Enter the amount : "))


        expense ={
            "date" :date,
            "category" :category,
            "description" :description,
            "amount" :amount
        }

        expenses.append(expense)
        print("\n DONE bro .Expenses is addded succesfully")


#2.VIEW ALL EXPENSES
    if(choise == 2):
        if (len (expenses) ==0):
            print("No Expenses Added . Go spend some money first! 😄")
        else:
            print("====== These are all your expenses ======.")
            count =1
            for eachspend in expenses:
                print(f"Spend Number {count} -> {eachspend['date']}, {eachspend['category']}, {eachspend['description']}, ₹{eachspend['amount']}")
                count =count+1


# 3.View total Spending
    elif(choice ==3):
        total= 0
        for eschspend in expensesList:
            total  =total + eachspend["amount"]

            print("\n TOTAL SPEND =",total)

#4. EXIT  
    elif(choice ==4 ):
        print("Thank you! We hope to see you again.")
        break
    
    else:
        print("INVALID CHOICE TRY AGAIN")

