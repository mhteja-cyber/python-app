import streamlit as st

st.set_page_config(
    page_title="Siri Tea Cafe",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Siri Tea Cafe")
st.subheader("Daily Sales Management System")

# Menu with prices
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


# Session State
if "orders" not in st.session_state:
    st.session_state.orders = []

if "customers" not in st.session_state:
    st.session_state.customers = 0

if "total_earnings" not in st.session_state:
    st.session_state.total_earnings = 0

if "item_sales" not in st.session_state:
    st.session_state.item_sales = {}

    for item in menu:
        st.session_state.item_sales[item] = 0


# Customer Details
st.markdown("---")
st.header("Customer Order")

food = st.selectbox(
    "Select Item",
    list(menu.keys())
)

qty = st.number_input(
    "Quantity",
    min_value=1,
    value=1
)


# Add Item
if st.button("Add Item"):

    st.session_state.orders.append({
        "food": food,
        "qty": qty,
        "price": menu[food]
    })

    st.session_state.item_sales[food] += qty

    st.success(f"{food} Added Successfully!")


# Current Bill
st.markdown("---")
st.subheader("Current Bill")

if st.session_state.orders:

    total = 0

    for item in st.session_state.orders:

        amount = item["qty"] * item["price"]
        total += amount

        st.write(
            f"{item['food']} x {item['qty']} = ₹{amount}"
        )

    st.markdown(f"## Total = ₹{total}")


    # Generate Bill
    if st.button("Generate Bill"):

        st.success("Bill Generated Successfully!")

        st.write("### Final Bill")

        for item in st.session_state.orders:

            st.write(
                f"{item['food']} x {item['qty']} = ₹{item['qty']*item['price']}"
            )

        st.write("---")
        st.write(f"## Grand Total = ₹{total}")


    # Payment Completed
    if st.button("Payment Completed"):

        st.session_state.total_earnings += total
        st.session_state.customers += 1

        st.session_state.orders = []

        st.success("Payment Completed Successfully!")

        st.rerun()

else:
    st.info("No Items Added Yet.")


# Dashboard
st.markdown("---")
st.header("Today's Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Today's Earnings",
    f"₹{st.session_state.total_earnings}"
)

col2.metric(
    "Customers Today",
    st.session_state.customers
)

col3.metric(
    "Daily Target",
    "50 Customers"
)


# Most Selling Item
st.markdown("---")
st.subheader("Most Selling Item")

max_sale = max(st.session_state.item_sales.values())

if max_sale > 0:

    most_selling = [
        item
        for item, qty in st.session_state.item_sales.items()
        if qty == max_sale
    ]

    for item in most_selling:
        st.success(
            f"{item} is the most selling item ({max_sale} sold)"
        )

else:
    st.info("No sales yet.")


# Restock Suggestions
st.markdown("---")
st.subheader("Items to Buy Next (Restock)")

restock_items = []

for item, qty in st.session_state.item_sales.items():

    if qty >= 5:
        restock_items.append(item)

if restock_items:

    for item in restock_items:
        st.write(f"🛒 Buy more {item}")

else:
    st.write("Stock is sufficient.")


# Customer Target Status
st.markdown("---")
st.subheader("Customer Target")

remaining = 50 - st.session_state.customers

if remaining > 0:

    st.warning(
        f"You need {remaining} more customers to reach today's target."
    )

else:
    st.success(
        "Congratulations! Today's target of 50 customers has been achieved."
    )


# Menu Card
st.markdown("---")
st.subheader("Siri Tea Cafe Menu")

for item, price in menu.items():
    st.write(f"**{item}** - ₹{price}")
