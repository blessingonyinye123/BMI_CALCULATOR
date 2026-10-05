import streamlit as st

# Title and description for your website
st.title("⚖️ My BMI Calculator Web App")
st.write("Enter your details below to calculate your Body Mass Index.")

# Web inputs replacing input()
weight = st.number_input("Enter your weight in kg:", min_value=0.0, value=0.0, step=0.5)
height_cm = st.number_input("Enter your height in cm:", min_value=0.0, value=0.0, step=1.0)

# Button to trigger your logic
if st.button("Calculate BMI"):
    # Your calculation logic
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    bmi_rounded = round(bmi, 2)

    st.subheader(f"Your BMI is: {bmi_rounded}")

    # Your category conditions
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Category: Normal weight")
    elif 25 <= bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obesity")