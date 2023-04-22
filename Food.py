import streamlit as st

# Title and description
st.title("Restaurant Cost Prediction")
st.write("This app predicts the cost of a restaurant meal based on various factors.")

# Input features
st.sidebar.title("Input Features")
meal_cost = st.sidebar.number_input("Meal Cost ($)", min_value=1.0, max_value=1000.0, value=10.0, step=0.01)
tax_rate = st.sidebar.slider("Tax Rate (%)", min_value=0, max_value=20, value=10, step=1)
tip_percent = st.sidebar.slider("Tip Percent (%)", min_value=0, max_value=50, value=15, step=1)

# Calculations
tax_amount = meal_cost * (tax_rate / 100)
tip_amount = meal_cost * (tip_percent / 100)
total_cost = meal_cost + tax_amount + tip_amount

# Display predicted cost
st.subheader("Predicted Cost")
st.write(f"The predicted cost of the restaurant meal is: ${total_cost:.2f}")
