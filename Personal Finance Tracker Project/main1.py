# Expense Tracker Project

expenses = []  # List to store expenses

print("💰 Welcome to Expense Tracker")
print("👉 You should spend less!\n")

while True:
    print("\n====== MENU ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spend")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

    # 1. Add Expense
    if choice == 1:
        date = input("On which date did you spend the money? ")
        category = input("Enter Category (Food, Travel, Shopping, Rent, Bills, Entertainment, Healthcare, Salary, Grocery, Fuel, Others): ")
        description = input("Enter Description (e.g., Lunch, Uber Ride, Monthly Rent, Electricity Bill): ")
        amount = float(input("Enter the amount: ₹"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("\n✅ Expense added successfully!")

    # 2. View All Expenses
    elif choice == 2:

        if len(expenses) == 0:
            print("\n❌ No expenses added. Go spend some money first! 😄")

        else:
            print("\n====== Your Expense History ======")

            count = 1
            for eachspend in expenses:
                print(f"{count}. Date: {eachspend['date']}")
                print(f"   Category   : {eachspend['category']}")
                print(f"   Description: {eachspend['description']}")
                print(f"   Amount     : ₹{eachspend['amount']}")
                print("-" * 35)
                count += 1

    # 3. View Total Spend
    elif choice == 3:

        total = 0

        for eachspend in expenses:
            total += eachspend["amount"]

        print(f"\n💸 Total Spend = ₹{total}")

    # 4. Exit
    elif choice == 4:
        print("\n🙏 Thank you for using Expense Tracker!")
        print("💰 Save More, Spend Wisely. Have a great day!")
        break

    else:
        print("\n❌ Invalid choice! Please try again.")
        