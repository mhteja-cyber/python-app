import streamlit as st

st.set_page_config(page_title="South Indian Restaurant", page_icon="🍽️", layout="wide")

st.title("🍽️ South Indian Restaurant")
st.subheader("Table Order Management System")

# South Indian Menu
menu = {
    "Idli": 40,
    "Vada": 35,
    "Plain Dosa": 60,
    "Masala Dosa": 80,
    "Onion Dosa": 90,
    "Rava Dosa": 100,
    "Pesarattu": 90,
    "Uttapam": 90,
    "Poori": 70,
    "Pongal": 80,
    "Upma": 60,
    "Curd Rice": 70,
    "Lemon Rice": 75,
    "Tomato Rice": 80,
    "Vegetable Biryani": 140,
    "Sambar Rice": 90,
    "Meals": 180,
    "Filter Coffee": 30,
    "Tea": 20,
    "Buttermilk": 25
}

# Create session state for tables
if "tables" not in st.session_state:
    st.session_state.tables = {}

    for i in range(1, 11):
        st.session_state.tables[f"Table {i}"] = {
            "occupied": False,
            "orders": []
        }

# Sidebar
st.sidebar.title("🍴 Tables")

selected_table = st.sidebar.selectbox(
    "Select Table",
    list(st.session_state.tables.keys())
)

table = st.session_state.tables[selected_table]

st.header(selected_table)

status = "🟢 Available" if not table["occupied"] else "🔴 Occupied"
st.write("### Status:", status)

st.markdown("---")

st.subheader("Add Food")

food = st.selectbox("Select Food", list(menu.keys()))
qty = st.number_input("Quantity", min_value=1, value=1)

if st.button("Add to Order"):
    table["occupied"] = True
    table["orders"].append({
        "food": food,
        "qty": qty,
        "price": menu[food]
    })
    st.success(f"{food} added successfully!")

st.markdown("---")

st.subheader("Current Bill")

if table["orders"]:

    total = 0

    for item in table["orders"]:
        amount = item["qty"] * item["price"]
        total += amount

        st.write(
            f"{item['food']}  x {item['qty']}  = ₹{amount}"
        )

    st.markdown("## Total : ₹{}".format(total))

    if st.button("Generate Bill"):
        st.success("Bill Generated Successfully!")

        st.write("### Final Bill")

        for item in table["orders"]:
            st.write(
                f"{item['food']} x {item['qty']} = ₹{item['qty']*item['price']}"
            )

        st.write("---")
        st.write(f"## Grand Total : ₹{total}")

    if st.button("Payment Completed / Clear Table"):
        table["orders"] = []
        table["occupied"] = False
        st.success("Table Cleared Successfully!")
        st.rerun()

else:
    st.info("No orders yet.")

st.markdown("---")

st.subheader("Restaurant Dashboard")

col1, col2 = st.columns(2)

occupied = sum(
    1 for t in st.session_state.tables.values() if t["occupied"]
)

available = 10 - occupied

col1.metric("Occupied Tables", occupied)
col2.metric("Available Tables", available)

st.markdown("---")

st.subheader("Menu Card")

for item, price in menu.items():
    st.write(f"**{item}** - ₹{price}")
