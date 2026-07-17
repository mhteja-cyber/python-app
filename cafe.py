import streamlit as st
import pandas as pd

st.set_page_config(page_title="Siri Tea Cafe", layout="wide")

st.title("☕ Siri Tea Cafe Management System")

# Default customers per day
average_customers = 100

# Menu items and prices
menu = {
    "Small Tea": 8,
    "Big Tea" : 10,
    "Coffee": 15,
    "Milk": 15,
    "Boost" : 15,
    "Ginger Milk" : 10,
    "Ragi Java" : 10,
    "Biscuits": 5,
    "Nipatlu" : 5,
    "Cakilalu" : 5,
    "Coca Cola": 20,
    "Thumbs UP" : 20,
    "Sprite" : 20,
    "Water Bottle (1 Liter)": 20,
    "wills": 12,
    "small Gold": 15,
    "Big Gold" : 25,
    "Lights" : 25,
    "American Club" : 20,
    "Classic Connect" : 20,
    "Social" : 20,
    "Silk" : 20,
}

st.header("Today's Sales")

sales_data = {}
total_earnings = 0

# Quantity inputs
for item, price in menu.items():
    qty = st.number_input(
        f"{item} (₹{price}) - Quantity Sold",
        min_value=0,
        step=1,
        key=item,
    )

    sales_data[item] = qty
    total_earnings += qty * price

# Customer count
st.header("Customer Information")

customers_today = st.number_input(
    "Number of Customers Today",
    min_value=0,
    value=50,
    step=1,
)

# Show report button
if st.button("Generate Today's Report"):

    st.success("Today's Report Generated Successfully!")

    st.subheader("Total Earnings")
    st.write(f"₹ {total_earnings}")

    st.subheader("Customers Today")
    st.write(customers_today)

    # Create DataFrame
    df = pd.DataFrame(
        {
            "Item": list(sales_data.keys()),
            "Quantity Sold": list(sales_data.values()),
        }
    )

    st.subheader("Sales Report")
    st.dataframe(df, use_container_width=True)

    # Most sold items
    max_sale = max(sales_data.values())

    if max_sale > 0:
        most_sold = [
            item
            for item, qty in sales_data.items()
            if qty == max_sale
        ]

        st.subheader("Most Selling Item(s)")
        for item in most_sold:
            st.write(f"✅ {item} ({max_sale} sold)")
    else:
        st.warning("No items sold today.")

    # Restock suggestions
    st.subheader("Items to Buy Next (Restock Suggestions)")

    restock_items = []

    for item, qty in sales_data.items():
        if qty >= 10:
            restock_items.append(item)

    if restock_items:
        for item in restock_items:
            st.write(f"🛒 Buy more {item}")
    else:
        st.write("Current stock is sufficient.")

    # Average customers
    st.subheader("Daily Customer Expectation")
    st.write(f"Average Customers Per Day: {average_customers}")

    # Estimated earnings
    if customers_today > 0:
        avg_spending = total_earnings / customers_today

        estimated_monthly = total_earnings * 30

        st.subheader("Business Insights")

        st.write(
            f"Average Spending Per Customer: ₹ {avg_spending:.2f}"
        )

        st.write(
            f"Estimated Monthly Earnings: ₹ {estimated_monthly}"
        )

        if customers_today >= average_customers:
            st.success(
                "Great! Customer count is equal to or above your daily target."
            )
        else:
            st.warning(
                "Customer count is below your daily target of 50 customers."
            )
