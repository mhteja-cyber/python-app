import streamlit as st

st.set_page_config(page_title="Python Bank", page_icon="🏦")

st.title("🏦 Python Bank")

# Initialize balance
if "balance" not in st.session_state:
    st.session_state.balance = 0

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Choose an Option",
    [
        "Check Balance",
        "Withdraw Amount",
        "Deposit Amount",
        "Money Transfer",
        "Create New Account",
    ],
)

# Check Balance
if menu == "Check Balance":
    st.subheader("💰 Account Balance")
    st.success(f"Your Balance: ₹{st.session_state.balance}")

# Withdraw
elif menu == "Withdraw Amount":
    st.subheader("💸 Withdraw Money")

    amount = st.number_input(
        "Enter Amount",
        min_value=0,
        step=1,
    )

    if st.button("Withdraw"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(f"₹{amount} withdrawn successfully.")
            st.info(f"Remaining Balance: ₹{st.session_state.balance}")
        else:
            st.error("Insufficient Balance!")

# Deposit
elif menu == "Deposit Amount":
    st.subheader("💵 Deposit Money")

    amount = st.number_input(
        "Enter Amount",
        min_value=0,
        step=1,
    )

    if st.button("Deposit"):
        st.session_state.balance += amount
        st.success(f"₹{amount} deposited successfully.")
        st.info(f"Current Balance: ₹{st.session_state.balance}")

# Money Transfer
elif menu == "Money Transfer":
    st.subheader("📤 Money Transfer")

    mobile = st.text_input("Enter Mobile Number")
    amount = st.number_input(
        "Transfer Amount",
        min_value=0,
        step=1,
    )

    if st.button("Transfer"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(
                f"₹{amount} transferred successfully to {mobile}."
            )
            st.info(f"Remaining Balance: ₹{st.session_state.balance}")
        else:
            st.error("Insufficient Balance!")

# Create Account
elif menu == "Create New Account":
    st.subheader("📝 Create New Account")

    name = st.text_input("Enter Your Name")
    mobile = st.text_input("Enter Mobile Number")
    address = st.text_area("Enter Address")

    if st.button("Create Account"):
        if name and mobile and address:
            st.success("🎉 Account Created Successfully!")
            st.write("### Account Details")
            st.write(f"**Name:** {name}")
            st.write(f"**Mobile:** {mobile}")
            st.write(f"**Address:** {address}")
        else:
            st.warning("Please fill all the details.")

st.sidebar.markdown("---")
st.sidebar.write(f"💰 **Balance:** ₹{st.session_state.balance}")
