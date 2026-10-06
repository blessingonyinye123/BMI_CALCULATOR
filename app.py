import streamlit as st

# Title and description for your website
st.title("⚖️ My BMI Calculator Web App")
st.write("Enter your details below to calculate your Body Mass Index.")

# Web inputs replacing input()
weight = st.number_input("Enter your weight in kg:", min_value=0.0, value=0.0, step=0.5)
height_cm = st.number_input("Enter your height in cm:", min_value=0.0, value=0.0, step=1.0)

# Button to trigger your logic
if st.button("Calculate BMI"):
    if height_cm <= 0 or weight <= 0:
        st.error("Please enter height and weight values greater than 0.")
    else:
        # Your calculation logic
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        st.subheader(f"Your BMI is: {bmi_rounded}")

        # Expanded WHO category conditions
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 25.0:
            st.success("Category: Normal weight")
        elif 25.0 <= bmi < 30.0:
            st.warning("Category: Overweight")
        elif 30.0 <= bmi < 35.0:
            st.error("Category: Obesity Class 1 (Moderate)")
        elif 35.0 <= bmi < 40.0:
            st.error("Category: Obesity Class 2 (Severe)")
        else:
            st.error("Category: Obesity Class 3 (Very Severe / High Risk)")