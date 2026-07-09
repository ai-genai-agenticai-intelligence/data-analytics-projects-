import streamlit as st
import pandas as pd

st.set_page_config(page_title="Expense Tracker", page_icon="💰")

st.title("💰 Expense Tracker")
st.write("Track your daily expenses easily!")

# Store data in session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Choose an Option",
    ["Add Expense", "View Expenses", "Total Spend"]
)

# ---------------- ADD EXPENSE ---------------- #
if menu == "Add Expense":

    st.header("➕ Add Expense")

    date = st.date_input("Select Date")

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Rent",
            "Bills",
            "Entertainment",
            "Healthcare",
            "Salary",
            "Grocery",
            "Fuel",
            "Others",
        ],
    )

    description = st.text_input("Description")

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=1.0,
        format="%.2f",
    )

    if st.button("Add Expense"):

        st.session_state.expenses.append(
            {
                "Date": str(date),
                "Category": category,
                "Description": description,
                "Amount": amount,
            }
        )

        st.success("✅ Expense Added Successfully!")

# ---------------- VIEW EXPENSES ---------------- #
elif menu == "View Expenses":

    st.header("📋 Expense History")

    if len(st.session_state.expenses) == 0:
        st.warning("No expenses added yet.")
    else:
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df, use_container_width=True)

# ---------------- TOTAL SPEND ---------------- #
elif menu == "Total Spend":

    st.header("💸 Total Spending")

    if len(st.session_state.expenses) == 0:
        st.warning("No expenses found.")
    else:
        df = pd.DataFrame(st.session_state.expenses)

        total = df["Amount"].sum()

        st.metric("Total Expense", f"₹ {total:,.2f}")

        st.subheader("Category-wise Spending")
        category_total = (
            df.groupby("Category")["Amount"]
            .sum()
            .reset_index()
        )

        st.bar_chart(category_total.set_index("Category"))