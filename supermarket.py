import streamlit as st
import pandas as pd

st.set_page_config(page_title="Super Market", page_icon="🛒", layout="wide")

st.title("🛒 Super Market Billing System")

# ---------------- Products ---------------- #

products = {
    "Fruits": {
        "Apple": 120,
        "Banana": 60,
        "Orange": 100,
        "Mango": 150,
        "Grapes": 90
    },

    "Vegetables": {
        "Tomato": 40,
        "Potato": 35,
        "Onion": 45,
        "Carrot": 60,
        "Cabbage": 50
    },

    "Dairy": {
        "Milk": 60,
        "Curd": 40,
        "Butter": 250,
        "Cheese": 350,
        "Paneer": 300
    },

    "Beverages": {
        "Tea": 180,
        "Coffee": 250,
        "Coca Cola": 40,
        "Pepsi": 40,
        "Juice": 90
    },

    "Snacks": {
        "Chips": 20,
        "Biscuits": 30,
        "Chocolate": 50,
        "Popcorn": 60,
        "Cookies": 80
    },

    "Rice & Grains": {
        "Rice": 70,
        "Wheat Flour": 55,
        "Ragi": 90,
        "Oats": 120,
        "Dal": 110
    },

    "Spices": {
        "Turmeric": 45,
        "Chilli Powder": 70,
        "Coriander Powder": 60,
        "Pepper": 150,
        "Garam Masala": 80
    },

    "Personal Care": {
        "Soap": 40,
        "Shampoo": 180,
        "Toothpaste": 120,
        "Face Wash": 220,
        "Hand Wash": 90
    },

    "Household": {
        "Detergent": 220,
        "Floor Cleaner": 180,
        "Dish Wash": 110,
        "Toilet Cleaner": 160,
        "Garbage Bags": 140
    }
}

# ---------------- Session ---------------- #

if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------- Sidebar ---------------- #

category = st.sidebar.selectbox(
    "Select Category",
    list(products.keys())
)

item = st.sidebar.selectbox(
    "Select Item",
    list(products[category].keys())
)

price = products[category][item]

qty = st.sidebar.number_input(
    "Quantity",
    min_value=1,
    value=1
)

st.sidebar.write(f"### Price : ₹{price}")

if st.sidebar.button("Add To Cart"):
    st.session_state.cart.append({
        "Item": item,
        "Price": price,
        "Quantity": qty,
        "Total": price * qty
    })
    st.sidebar.success("Added Successfully!")

# ---------------- Cart ---------------- #

st.header("🛍 Shopping Cart")

if st.session_state.cart:

    df = pd.DataFrame(st.session_state.cart)

    st.dataframe(df, use_container_width=True)

    grand_total = df["Total"].sum()

    st.subheader(f"Grand Total : ₹{grand_total}")

    remove = st.selectbox(
        "Remove Item",
        ["None"] + list(df["Item"])
    )

    if st.button("Remove Selected"):
        if remove != "None":
            for i in st.session_state.cart:
                if i["Item"] == remove:
                    st.session_state.cart.remove(i)
                    break
            st.rerun()

    if st.button("Generate Bill"):

        bill = df.to_string(index=False)

        st.text(bill)

        st.success(f"Total Amount : ₹{grand_total}")

        st.download_button(
            "Download Bill",
            bill,
            file_name="bill.txt"
        )

    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()

else:
    st.info("Cart is Empty")

# ---------------- Footer ---------------- #

st.markdown("---")
st.markdown("### 🏪 Welcome to Python Super Market")
